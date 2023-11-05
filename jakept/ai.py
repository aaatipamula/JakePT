from langchain.chat_models import ChatOpenAI
from langchain.prompts import PromptTemplate 
from langchain.schema.output_parser import StrOutputParser
from langchain.schema.runnable import RunnablePassthrough
from requests import request

information_grabbing_template = """Given the following question from a potential customer who is inquiring on small business insurance loans, select a few of the following categories that would fit the kind of insurance they are looking for.

Your response should be the following URL: {url} formatted with the 'keys' and 'budget' parameters.

keys: should be the relevant categories seperated by commas e.g. "categoryA,categoryB..."
budget: should be the budget provided by the user rounded to the nearest integer e.g. "10" or "200"

Categories to Choose From:
["business personal property","building property","business liability","completed operations","mobile equipment","installation floater","property of others","commercial auto","commercial liability umbrella policy","workers compensation","surety bonds"],

Question: {question}"""

info_prompt = PromptTemplate.from_template(information_grabbing_template)

customer_rec_template = """You are Jake from State Farm. Given the following information about a customer and information on policies and certain coverages give them the best recommendation you can offer. Filter out policies outside of their price bracket and suggest policies that see a high percentage of claims.

Policy Data:
{data}

Customer Info:
{customer_info}"""

rec_prompt = PromptTemplate.from_template(customer_rec_template)

model = ChatOpenAI(model='gpt-3.5-turbo', temperature=0, verbose=True)

def create_chain():
    category_response = (
        info_prompt
        | StrOutputParser()
    )
    full_response = (
        RunnablePassthrough.assign(data=category_response)
        | RunnablePassthrough.assign(
            data=lambda data: request('GET', data['url']),
        )
        | rec_prompt
        | model
    )

    return full_response


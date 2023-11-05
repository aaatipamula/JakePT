from langchain.chat_models import ChatOpenAI
from langchain.prompts import PromptTemplate 
from langchain.schema.output_parser import StrOutputParser
from langchain.schema.runnable import RunnablePassthrough
from requests import request

information_grabbing_template = """Given the following question from a potential customer who is inquiring on small business insurance loans, select a few of the following categories that would fit the kind of insurance they are looking for. Give your response in comma seperated values. e.g. "categoryA,categoryB,categoryC"

Categories to Choose From:
{topic_categories}

Question: {question}"""

info_prompt = PromptTemplate.from_template(information_grabbing_template)

customer_rec_template = """You are Jake from State Farm. Given the following information about a customer and information on policies and certain coverages give them the best recommendation you can offer. 

Policy and Coverage Data:
{data}

Customer Info:
{customer_info}"""

rec_prompt = PromptTemplate.from_template(customer_rec_template)

model = ChatOpenAI()

def create_chain(base_url, customer_info, categories):
    category_response = (
        RunnablePassthrough.assign(topic_categories=categories)
        | info_prompt
        | StrOutputParser()
    )
    full_response = (
        RunnablePassthrough.assign(data=category_response)
        | RunnablePassthrough.assign(
            data=lambda data: request('GET', base_url + data['data']),
            customer_info=customer_info
        )
        | rec_prompt
        | model
    )

    return full_response



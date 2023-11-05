# JakePT
HackUTD 2023 Project

# Setup

## Local Machine

1. Setup a [Virtual Environment](https://docs.python.org/3/library/venv.html)

If you have Python > 3 installed you can run the following *In the root of the project*:

```bash
python3 -m venv .venv
```

This will create a folder named `.venv` in your directory, you can activate it if you are using *bash* with:

```bash
source .venv/bin/activate
```

Deactivate it with:

```bash
deactivate
```

2. Install the required packages

```bash
pip3 install -r requirements.txt
```

3. Run the app with:

```bash
python3 -m flask --app jakept/main.py run
```

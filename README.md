# Local LLM Chat Project

This project provides a simple interface to interact with a local large language model (LLM) using Docker Model Runner. It allows both programmatic access via Python functions and interactive chat through a command-line interface.

## Project Structure

- `llm_client.py` - Contains a reusable function to send prompts to the LLM.
- `chat_llm.py` - Provides an interactive chat interface with the LLM.
- `requirements.txt` - Python dependencies.

## Setup Instructions

1. **Clone the repository**
```
   git clone git@github.com:anandavii/local-llm-chatbot.git
   cd llm_chat_project
```

2. **Set up Python environment**
```
    python -m venv venv
    source venv/bin/activate   # On Mac/Linux

    # OR venv\Scripts\activate  # On Windows
    pip install -r requirements.txt
``` 

3. **Run interactive chat**
```
    uv run main.py
```

## Notes
- Ensure the local LLM model is running in Docker Model Runner and is accessible at the correct URL.
- Messages follow the standard roles: system, user, assistant.


### Example Chat

#### Example 1
![example1](/demo/example1.png)

#### Example 2
![example2](/demo/example2.png)
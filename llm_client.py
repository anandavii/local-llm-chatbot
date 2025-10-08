from openai import OpenAI
import os

BASE_URL = "http://localhost:12434/engines/llama.cpp/v1"

# Instantiate the OpenAI client
client = OpenAI (base_url=BASE_URL, api_key="dummy-key")

# Define the model and prompt
MODEL_NAME = "ai/smollm2" 

def ask_model(prompt, model_name=MODEL_NAME, system_prompt="You are a helpful assistant."):
    """
    Send a single-turn or multi-turn prompt to the local LLM and return its response.
    """
    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": prompt}
    ]

    response = client.chat.completions.create(
        model=model_name,
        messages=messages
    )

    return response.choices[0].message.content
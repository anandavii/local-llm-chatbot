from openai import OpenAI

# Base URL for Docker Model Runner
BASE_URL = "http://localhost:12434/engines/llama.cpp/v1"

# Initialize client (Docker Model Runner ignores API key)
client = OpenAI(base_url=BASE_URL, api_key="dummy-key")

MODEL_NAME = "ai/smollm2"

def main():
    print("🤖 Local Chat with", MODEL_NAME)
    print("Type 'exit' or 'quit' to end the chat.\n")

    # Keep a running message history (context-aware chat)
    messages = [
        {"role": "system", "content": "You are a helpful assistant."}
    ]

    while True:
        user_input = input("You: ").strip()
        if user_input.lower() in ["exit", "quit"]:
            print("--------Ending chat--------")
            break

        # Add user message
        messages.append({"role": "user", "content": user_input})

        try:
            # Send to local LLM
            response = client.chat.completions.create(
                model=MODEL_NAME,
                messages=messages
            )

            reply = response.choices[0].message.content
            print(f"🤖: {reply}\n")

            # Add model reply to history
            messages.append({"role": "assistant", "content": reply})

        except Exception as e:
            print("⚠️ Error communicating with model:", e)
            break


if __name__ == "__main__":
    main()

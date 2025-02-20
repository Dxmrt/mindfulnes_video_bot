import openai

openai.api_key = "your_openai_api_key"

def generate_mindfulness_script():
    """Generates a short mindfulness script using OpenAI GPT-4."""
    prompt = "Generate a short mindfulness script for relaxation and meditation."

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}]
    )

    return response['choices'][0]['message']['content'].strip()

if __name__ == "__main__":
    print(generate_mindfulness_script())

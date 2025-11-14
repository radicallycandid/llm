"""National Capitals Lookup using OpenAI API.

This script demonstrates basic usage of the OpenAI Chat Completions API
to answer factual questions (country capitals).

Official Documentation:
- API Reference: https://platform.openai.com/docs/api-reference/chat
- Chat Guide: https://platform.openai.com/docs/guides/chat-completions
- Models: https://platform.openai.com/docs/models
"""

import openai
from openai import OpenAIError


# Initialize the OpenAI client (reads OPENAI_API_KEY from environment)
client = openai.OpenAI()


def get_capital(country_name: str) -> str:
    """Get the capital of a country using GPT-5 Nano.

    Args:
        country_name: Name of the country

    Returns:
        The capital city name or an error message
    """
    try:
        # Create a completion using GPT-5 Nano (fastest, most cost-effective)
        response = client.chat.completions.create(
            model="gpt-5-nano",  # Most affordable model for simple tasks
            messages=[
                {
                    "role": "system",
                    "content": "When the user says the name of a country, return its capital city name only. If you don't know, respond with 'I don't know'."
                },
                {"role": "user", "content": country_name}
            ]
        )
        return response.choices[0].message.content

    except OpenAIError as e:
        return f"API Error: {e}"
    except Exception as e:
        return f"Error: {e}"


def main():
    """Run the interactive capital lookup loop."""
    print("=== National Capitals Lookup ===")
    print("Enter a country name to get its capital.")
    print("Type 'exit' or 'quit' to end the program.\n")

    while True:
        user_input = input("Country: ").strip()

        if user_input.lower() in ['exit', 'quit', '']:
            print("Goodbye!")
            break

        capital = get_capital(user_input)
        print(f"Capital: {capital}\n")


if __name__ == "__main__":
    main()

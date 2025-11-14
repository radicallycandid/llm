"""Text Summarization using OpenAI API.

This script demonstrates how to use the OpenAI Chat Completions API
to summarize text files into concise paragraphs.

Official Documentation:
- API Reference: https://platform.openai.com/docs/api-reference/chat
- Chat Guide: https://platform.openai.com/docs/guides/chat-completions
- Models: https://platform.openai.com/docs/models
"""

import openai
from openai import OpenAIError


# Initialize the OpenAI client (reads OPENAI_API_KEY from environment)
client = openai.OpenAI()


def summarize_text(file_path: str) -> str:
    """Summarize a text file using GPT-4.1 Mini.

    Args:
        file_path: Path to the text file to summarize

    Returns:
        A one-paragraph summary or an error message
    """
    # Read the file
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
    except FileNotFoundError:
        return "❌ File not found. Please provide a valid file path."
    except UnicodeDecodeError:
        return "❌ Unable to read file. Please ensure it's a text file (UTF-8 encoded)."
    except Exception as e:
        return f"❌ File error: {e}"

    # Check if file is too large (GPT-5 has token limits)
    if len(content) > 100000:  # Rough character limit
        return "❌ File is too large. Please use a smaller file (< 100KB)."

    # Call OpenAI API
    try:
        response = client.chat.completions.create(
            model="gpt-4.1-mini-2025-04-14",  # Good balance of cost and capability for summarization
            messages=[
                {
                    "role": "system",
                    "content": "You are a helpful assistant that summarizes text concisely. Create a clear, comprehensive one-paragraph summary."
                },
                {
                    "role": "user",
                    "content": f"Please summarize the following text in one paragraph:\n\n{content}"
                }
            ],
            temperature=0.3,  # Low temperature for consistent, focused summaries
            max_completion_tokens=500    # Reasonable limit for one-paragraph summaries
        )
        return response.choices[0].message.content

    except OpenAIError as e:
        return f"❌ API Error: {e}"
    except Exception as e:
        return f"❌ Error: {e}"


def main():
    """Run the interactive text summarization loop."""
    print("=== Text File Summarizer ===")
    print("Enter the path to a text file to get a summary.")
    print("Type 'exit' or 'quit' to end the program.\n")
    print("💡 Tip: Try summarizing 'great_work.txt' or 'managers_schedule_makers_schedule.txt'\n")

    while True:
        user_input = input("File path: ").strip()

        if user_input.lower() in ['exit', 'quit', '']:
            print("Goodbye!")
            break

        print("\n⏳ Summarizing...\n")
        summary = summarize_text(user_input)
        print(f"📝 Summary:\n{summary}\n")
        print("-" * 80 + "\n")


if __name__ == "__main__":
    main()

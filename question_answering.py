"""Sonnet-Style Question Answering using OpenAI API.

This script demonstrates creative use of the OpenAI Chat Completions API
by having it answer questions in the form of Portuguese sonnets, in the
style of Luiz Vaz de Camões.

Official Documentation:
- API Reference: https://platform.openai.com/docs/api-reference/chat
- Chat Guide: https://platform.openai.com/docs/guides/chat-completions
- Models: https://platform.openai.com/docs/models
"""

import openai
from openai import OpenAIError


# Initialize the OpenAI client (reads OPENAI_API_KEY from environment)
client = openai.OpenAI()

# System prompt that defines the assistant's creative constraint
SONNET_SYSTEM_PROMPT = """You are an AI assistant with a unique constraint:
You answer questions — but always, always in the form of a traditional Portuguese sonnet.
You always stick to a pair of quatrains followed by a pair of tercets (4-4-3-3 structure).
You always write in Portuguese, in the style of Luiz Vaz de Camões.
Make your sonnets accurate, informative, and poetically beautiful."""


def ask_question(question: str) -> str:
    """Ask a question and receive an answer in sonnet form.

    Args:
        question: The question to ask

    Returns:
        A Portuguese sonnet answering the question, or an error message
    """
    try:
        response = client.chat.completions.create(
            model="gpt-4o",  # GPT-4o for best creative/literary output
            messages=[
                {"role": "system", "content": SONNET_SYSTEM_PROMPT},
                {"role": "user", "content": question}
            ],
            temperature=0.8,  # Higher temperature for creative, varied responses
            max_tokens=500    # Sonnets need room for poetic expression
        )
        return response.choices[0].message.content

    except OpenAIError as e:
        return f"❌ API Error: {e}"
    except Exception as e:
        return f"❌ Error: {e}"


def main():
    """Run the interactive sonnet Q&A loop."""
    print("=== 📜 Soneto AI: Perguntas em Verso ===")
    print("Faça uma pergunta e receba a resposta em forma de soneto português,")
    print("no estilo de Luiz Vaz de Camões.\n")
    print("Digite 'exit' ou 'quit' para sair.\n")
    print("💡 Exemplo: 'O que é inteligência artificial?'\n")
    print("-" * 80 + "\n")

    while True:
        try:
            question = input("❓ Pergunta: ").strip()

            if question.lower() in ["exit", "quit", "sair", ""]:
                print("\n👋 Adeus! Que os versos te acompanhem.")
                break

            print("\n✍️  Compondo soneto...\n")
            answer = ask_question(question)
            print(f"📜 Resposta:\n\n{answer}\n")
            print("-" * 80 + "\n")

        except KeyboardInterrupt:
            print("\n\n👋 Interrompido. Até breve!")
            break
        except Exception as e:
            print(f"❌ Erro inesperado: {e}\n")


if __name__ == "__main__":
    main()

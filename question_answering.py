from tiny_ai_client import AI  # Import the AI class from the tiny_ai_client module

# Initialize the AI client
ai = AI(
    model_name="gpt-4-turbo",  # Specify the model to use
    system="""You are an AI assistant.
You answer questions — but always, always in the form of a traditional sonnet.
You always stick to a pair of quatrains followed by a pair of tercets.
You always write in Portuguese, in the style of Luiz Vaz de Camões.""",  # System prompt to guide the AI's responses
    max_new_tokens=300,  # Maximum number of tokens (words/pieces of words) in the response
)


def main():
    # Q&A loop: repeatedly asks the user for input and responds until the user decides to quit
    while True:
        try:
            query = input(
                "Ask a question (alternatively, type 'exit' or 'quit' to quit): "
            )  # Prompt the user for a question
            if query.lower() in ["exit", "quit"]:  # Check if the user wants to exit
                print("Exiting the Q&A program.")  # Print exit message
                break  # Exit the loop and end the program

            response = ai(
                query
            )  # Send the user's question to the AI and get the response
            print(f"Answer:\n{response}")  # Print the AI's response
        except Exception as e:  # Handle any errors that occur
            print(f"An error occurred: {e}")  # Print an error message


if __name__ == "__main__":
    main()  # Run the main function if this script is executed directly

import openai  # Import the OpenAI library to interact with the OpenAI API

# Initialize the OpenAI client
client = openai.OpenAI()

# Function to get the capital of a country
def get_capital(country_name):
    # Create a completion using the GPT-3.5-turbo model
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            # System message to instruct the assistant on how to respond
            {"role": "system", "content": "When the `user` says the name of a country, `assistant` returns its capital, and ONLY it. If you don't know the capital, respond with 'I don't know'."},
            # User message with the name of the country
            {"role": "user", "content": country_name}
        ]
    )
    # Extract the assistant's response (the capital) from the API response
    return response.choices[0].message.content

# Main function to run the script
def main():
    print("Enter the name of a country to get its capital. Type 'exit' to end the program.")
    while True:  # Infinite loop to continuously prompt the user for input
        user_input = input("Country: ")  # Get user input
        if user_input.lower() == 'exit':  # Exit the loop if the user types 'exit'
            break
        capital = get_capital(user_input)  # Get the capital of the country
        print(f"Capital: {capital}")  # Print the capital

# Entry point of the script
if __name__ == "__main__":
    main()  # Call the main function to start the script

import openai  # Import the OpenAI library to interact with the OpenAI API

# Initialize the OpenAI client
client = openai.OpenAI()

# Function to summarize the content of a text file
def summarize_text(file_path):
    try:
        # Try to open the file at the given file path in read mode with UTF-8 encoding
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()  # Read the entire content of the file
    except FileNotFoundError:
        return "File not found. Please provide a valid file path."  # Return an error message if the file is not found
    except Exception as e:
        return f"An error occurred: {e}"  # Return an error message for any other exception that occurs

    # Create a completion using the GPT-3.5-turbo model
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            # System message to instruct the assistant on how to respond
            {"role": "system", "content": "Summarize the following text into one paragraph."},
            # User message with the content of the text file
            {"role": "user", "content": content}
        ]
    )
    # Extract the assistant's response (the summary) from the API response
    return response.choices[0].message.content

# Main function to run the script
def main():
    print("Enter the local path of a text file to get its summary. Type 'exit' to end the program.")
    while True:  # Infinite loop to continuously prompt the user for input
        user_input = input("File path: ")  # Get user input
        if user_input.lower() == 'exit':  # Exit the loop if the user types 'exit'
            break
        summary = summarize_text(user_input)  # Get the summary of the text file
        print(f"Summary: {summary}")  # Print the summary

# Entry point of the script
if __name__ == "__main__":
    main()  # Call the main function to start the script

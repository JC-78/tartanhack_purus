import openai
import json

# Load your API key from the JSON file
try:
    with open('key.json', 'r') as file:
        api_key_data = json.load(file)
        api_key = api_key_data.get('api_key', '')

    # Set your OpenAI API key
    openai.api_key = api_key

    # Text to be summarized
    with open('output.txt', 'r', encoding='utf-8') as file:
        text_to_summarize = file.read()

    # Ask OpenAI to summarize the text
    response = openai.Completion.create(
        engine="davinci-002",
        prompt=text_to_summarize+". now summarize the ingredients",
        max_tokens=100
    )

    # Print the summarized text
    print("Original Text:")
    print(text_to_summarize)
    print("\nSummarized Text:")
    print(response['choices'][0]['text'])

except FileNotFoundError:
    print("Error: 'key.json' file not found. Make sure the file exists in the correct location.")
except json.JSONDecodeError:
    print("Error: 'key.json' is not a valid JSON file.")
except openai.error.InvalidRequestError as e:
    print(f"OpenAI API request error: {e}")
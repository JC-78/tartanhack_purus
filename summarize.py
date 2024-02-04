from openai import OpenAI
import json
import re

def summarize():
    # Load your API key from the JSON file
    try:
        with open('/Users/joonghochoi/Desktop/Music2P/key.json', 'r') as file:
            api_key_data = json.load(file)
            api_key = api_key_data.get('api_key', '')

        # Set your OpenAI API key
        client = OpenAI(api_key=api_key)
        
        # Text to be summarized
        with open('/Users/joonghochoi/Desktop/Music2P/output.txt', 'r', encoding='utf-8') as file:
            text_to_summarize = file.read()

        # Ask OpenAI to summarize the text
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role":"user", "content": text_to_summarize+". give me ingredients in a python list format."}],
            )

        # Print the summarized text
        # print("Original Text:")
        # print(text_to_summarize)
        # print("\nSummarized Text:")
        raw = response.choices[0].message.content
        # print("gpt answer")
        # print(raw)
        pattern = r"['\"]([^'\"]*)['\"]"
        matches = re.findall(pattern, raw)
        # print("matches",matches)
        # concatenated_string = '\n'.join(matches)
        # print("concatenated_string",concatenated_string)
        # return concatenated_string
        return matches

    except FileNotFoundError:
        print("Error: 'key.json' file not found. Make sure the file exists in the correct location.")
    except json.JSONDecodeError:
        print("Error: 'key.json' is not a valid JSON file.")
    # except openai.error.InvalidRequestError as e:
    #     print(f"OpenAI API request error: {e}")
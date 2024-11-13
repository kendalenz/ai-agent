from openai import OpenAI
import os
from dotenv import load_dotenv
from actions import get_seo_page_report
from prompts import system_prompt
from json_helpers import extract_json

# Load environment variables
load_dotenv()

# Create an instance of the OpenAI class
openai_client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def generate_text_with_conversation(messages, model = "gpt-3.5-turbo"):
    response = openai_client.chat.completions.create(
        model=model,
        messages=messages
        )
    return response.choices[0].message.content

# Define a list of messages to simulate a conversation
#test_messages = [
   # {"role": "user", "content": "Hello, how are you?"},
   # {"role": "system", "content": "You are a helpful AI assistant"}
#]

# Call the function with the test messages
#response = generate_text_with_conversation(test_messages)
#print("AI Response:", response)

#available_actions = {
    #"get_response_time": get_response_time
#}

available_actions = {
    "get_seo_page_report": get_seo_page_report
}

user_prompt = "What is the response time for learnwithhasan.com?"

messages = [
    {"role": "system", "content": system_prompt},
    {"role": "user", "content": user_prompt},
]

turn_count = 1
max_turns = 5

#testing one two

#whyisthisnotworking
while turn_count < max_turns:
    print (f"Loop: {turn_count}")
    print("----------------------")
    turn_count += 1

    response = generate_text_with_conversation(messages, model="gpt-4")

    print(response)

    json_function = extract_json(response)

    if json_function:
            function_name = json_function[0]['function_name']
            function_parms = json_function[0]['function_parms']
            if function_name not in available_actions:
                raise Exception(f"Unknown action: {function_name}: {function_parms}")
            print(f" -- running {function_name} {function_parms}")
            action_function = available_actions[function_name]
            #call the function
            result = action_function(**function_parms)
            function_result_message = f"Action_Response: {result}"
            messages.append({"role": "user", "content": function_result_message})
            print(function_result_message)
    else:
         break
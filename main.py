import os
from dotenv import load_dotenv
from openai import OpenAI
from actions import get_seo_page_report
from prompts import react_system_prompt
from json_helpers import extract_json

# Load environment variables
load_dotenv()

# Initialize OpenAI
openai_client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def generate_text_with_conversation(messages, model="gpt-4"):
    """
    Sends a conversation to OpenAI and retrieves the response.
    """
    try:
        response = openai_client.chat.completions.create(
            model=model,
            messages=messages
        )
        # Correctly access the response content
        return response.choices[0].message.content
    except AttributeError:
        return "Error: OpenAI response structure has changed or is invalid."
    except Exception as e:
        return f"Error communicating with GPT: {e}"


def main():
    # Input URL for analysis
    user_prompt = input("Enter the URL for SEO analysis: ")
    
    # Initialize the conversation messages
    messages = [
        {"role": "system", "content": react_system_prompt},
        {"role": "user", "content": f"Analyze the following website: {user_prompt}"}
    ]

    # Get the SEO report from RapidAPI
    seo_report = get_seo_page_report(user_prompt)
    if "error" in seo_report:
        print(f"Error fetching SEO report: {seo_report['error']}")
        return

    # Add the SEO report to the conversation
    messages.append({
        "role": "assistant",
        "content": f"Here is the SEO report for {user_prompt}: {seo_report}"
    })

    # Send to GPT for further analysis
    gpt_response = generate_text_with_conversation(messages, model="gpt-4")
    if "Error" in gpt_response:
        print(gpt_response)  # Print error message if GPT fails
    else:
        print(f"\nGPT's Analysis:\n{gpt_response}")

if __name__ == "__main__":
    main()

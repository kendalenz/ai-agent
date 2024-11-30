from flask import Flask, request, jsonify, send_from_directory
from actions import get_seo_page_report
from prompts import react_system_prompt
from openai import OpenAI
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize OpenAI
openai_client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Initialize Flask app
app = Flask(__name__)

def generate_text_with_conversation(messages, model="gpt-4"):
    """
    Sends a conversation to OpenAI and retrieves the response.
    """
    try:
        response = openai_client.chat.completions.create(
            model=model,
            messages=messages
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Error communicating with GPT: {e}"

@app.route('/analyze', methods=['POST'])
def analyze():
    """
    Analyze a URL and return GPT's response.
    """
    data = request.json
    url = data.get('url')

    if not url:
        return jsonify({"error": "URL is required"}), 400

    # Get the SEO report
    seo_report = get_seo_page_report(url)
    if "error" in seo_report:
        return jsonify({"error": seo_report["error"]}), 500

    # Prepare messages for GPT
    messages = [
        {"role": "system", "content": react_system_prompt},
        {"role": "user", "content": f"Analyze the following website: {url}"},
        {"role": "assistant", "content": f"Here is the SEO report for {url}: {seo_report}"}
    ]

    # Get GPT's analysis
    gpt_response = generate_text_with_conversation(messages, model="gpt-4")
    return jsonify({"gpt_response": gpt_response})

# Serve the index.html file
@app.route('/')
def index():
    return send_from_directory('.', 'index.html')

if __name__ == "__main__":
    app.run(debug=True)

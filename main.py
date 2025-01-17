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
def truncate_seo_report(seo_report, limit=500):
    """
    Truncate the SEO report to reduce its size for GPT.
    """
    import json  # Ensure the JSON module is imported
    report_text = json.dumps(seo_report, indent=2)  # Convert to a readable JSON string
    if len(report_text) > limit:
        return report_text[:limit] + "... (truncated)"
    return report_text
@app.route('/analyze', methods=['POST'])
def analyze():
    data = request.json
    url = data.get('url')
    if not url:
        return jsonify({"error": "URL is required"}), 400

    # Get the SEO report
    seo_report = get_seo_page_report(url)
    if "error" in seo_report:
        return jsonify({"error": seo_report["error"]}), 500
    # Truncate the SEO report
    truncated_report = truncate_seo_report(seo_report)
    # Prepare messages for GPT
    messages = [
        {"role": "system", "content": react_system_prompt},
        {"role": "user", "content": f"Analyze the following website: {url}"},
        {"role": "assistant", "content": f"Here is the SEO report for {url}: {truncated_report}"}
    ]
    # Get GPT's analysis
    gpt_response = generate_text_with_conversation(messages, model="gpt-4")

    # Return both GPT response and raw SEO report
    return jsonify({
        "gpt_response": gpt_response,
        "seo_report": seo_report  # Include raw SEO report for debugging
    })
@app.route('/')
def index():
    return send_from_directory('.', 'index.html')
if __name__ == "__main__":
    app.run(debug=True)

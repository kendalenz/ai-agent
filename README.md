# AI-Agent: SEO Analyzer & Assistant

AI-Agent is a python-based application that utilizes the **RapidAPI SEO API** and **OpenAI's ChatGPT API** to analyze URLs, provide SEO analysis and generate actionable feedback. This project combines robust API integrations with an intuitive web interface to simplify the process of improving your website's SEO.

---

## Features

- **URL Analysis**: Input any URL to fetch detailed SEO-related data using the RapidAPI SEO API.
- **AI-Powered Feedback**: Leverages ChatGPT to generate insightful and actionable recommendations.
- **Web Interface**: User-friendly interface built with HTML, CSS and JavaScript.

---

## Technologies Used

### Programming
- **Python**: Core programming language.

### APIs
- **RapidAPI SEO API**: For extracting SEO metrics and details.
- **OpenAI ChatGPT API**: For generating human-like feedback and recommendations.

### Web
- **HTML/CSS**: Frontend design for the web interface.
- **Bootstrap**: Responsive and modern styling (CDN linked).

---

## Requirements

- **Python**: 3.7 or higher
- **API Keys**: Obtain and configure API keys for:
  - RapidAPI SEO API
  - OpenAI API
- **Dependencies**: Listed in `requirements.txt`:
  - `requests`
  - `dotenv`
  - `Flask` (if a server is required for running the app)
  - Add any others if missing.

---

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/AI-Agent.git
   cd AI-Agent
2. Set up a Python virtual environment:
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
3. Install dependencies:
   pip install -r requirements.txt
4. Configure your .env file:
   RAPIDAPI_KEY=your_rapidapi_key
   OPENAI_API_KEY=your_openai_api_key
   
---

## Usage
1. Run the Application:
   python main.py
2. Access the Web Interface: Open a browser and navigate to: http://localhost:5000 (http://127.0.0.1:5000/)
3. Analyze a URL:
* Enter the URL into the form and click "Analyze".
* Review the generated SEO analysis and feedback.



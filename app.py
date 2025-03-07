from flask import Flask, render_template, request, redirect, url_for
import google.generativeai as genai
import webbrowser
import os
from dotenv import load_dotenv

# Load API key from .env for security
load_dotenv()
API_KEY = os.getenv("GOOGLE_API_KEY")  # Ensure you store API key in a .env file

app = Flask(__name__)

# Configure Google AI Studio with your API key
genai.configure(api_key=API_KEY)

# Generation settings
generation_config = {
    "temperature": 1,
    "top_p": 0.95,
    "top_k": 40,
    "max_output_tokens": 8192,
    "response_mime_type": "text/plain",
}

# Updated model with your tuned model ID
model = genai.GenerativeModel(
    model_name="tunedModels/ecommerceai50prompts-tihe1qo0s03z",  # Updated model
    generation_config=generation_config,
)

# Function to interact with AI model
def chat_bot(prompt):
    try:
        response = model.generate_content(prompt)
        return response.text  
    except Exception as e:
        return f"Error: {e}"

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/track_package', methods=['GET', 'POST'])
def track_package():
    if request.method == 'POST':
        tracking_id = request.form['tracking_id']
        webbrowser.open('https://www.indiapost.gov.in/')
        return redirect(url_for('home'))
    return render_template('track_package.html')

@app.route('/view_offers')
def view_offers():
    offers = "Here are the latest offers: \n1. 20% off on electronics \n2. Buy 1 Get 1 Free on shoes \n3. Free shipping on orders over $50"
    return render_template('view_offers.html', offers=offers)

@app.route('/chat', methods=['GET', 'POST'])
def chat():
    if request.method == 'POST':
        user_input = request.form['user_input']
        if user_input.lower() == 'exit':
            return redirect(url_for('home'))
        response = chat_bot(user_input)
        return render_template('index.html', user_input=user_input, response=response)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)

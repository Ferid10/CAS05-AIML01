from flask import Flask, render_template, request, redirect, url_for
import google.generativeai as genai
import webbrowser

app = Flask(__name__)

API_KEY = "AIzaSyBX4MtAHWRU0_5xwCocs8GvqYWnsAdH_PE"
genai.configure(api_key=API_KEY)
model = genai.GenerativeModel("gemini-1.5-pro")

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
        return render_template('chat.html', user_input=user_input, response=response)
    return render_template('chat.html')

if __name__ == '__main__':
    app.run(debug=True)

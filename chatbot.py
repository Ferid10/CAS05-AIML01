import google.generativeai as genai
import webbrowser
from flask import Flask, render_template, request, jsonify

API_KEY = "AIzaSyBX4MtAHWRU0_5xwCocs8GvqYWnsAdH_PE"  # Replace with your actual API key
genai.configure(api_key=API_KEY)

model = genai.GenerativeModel("gemini-1.5-pro")

app = Flask(__name__)

def chat_bot(prompt):
    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"Error: {e}"

def track_package():
    webbrowser.open('https://www.indiapost.gov.in/')
    return "Opened India Post tracking website. Please enter your tracking ID there."

def view_offers():
    return "Here are the latest offers: <br>1. 20% off on electronics <br>2. Buy 1 Get 1 Free on shoes <br>3. Free shipping on orders over $50"

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/process", methods=["POST"])
def process():
    choice = request.form["choice"]

    if choice == "1":
        result = track_package()
    elif choice == "2":
        result = view_offers()
    elif choice == "3":
        user_input = request.form.get("user_input", "")
        if user_input.lower() == "exit":
            result = "Returning to the main menu..."
        else:
            result = chat_bot(user_input)
    else:
        result = "Invalid choice. Please try again."

    return jsonify({"result": result})

if __name__ == "__main__":
    app.run(debug=True)

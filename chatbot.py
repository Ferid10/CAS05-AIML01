import google.generativeai as genai

API_KEY = "AIzaSyBX4MtAHWRU0_5xwCocs8GvqYWnsAdH_PE" 
genai.configure(api_key=API_KEY)


model = genai.GenerativeModel("gemini-1.5-pro")

def chat_with_gemini(prompt):
    try:
        response = model.generate_content(prompt)
        return response.text  
    except Exception as e:
        return f"Error: {e}"

print("Gemini AI Chatbot (type 'exit' to quit)")
while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        print("Chatbot: Goodbye!")
        break
    response = chat_with_gemini(user_input)
    print("Chatbot:", response)

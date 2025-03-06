import google.generativeai as genai

API_KEY = "AIzaSyBX4MtAHWRU0_5xwCocs8GvqYWnsAdH_PE" 
genai.configure(api_key=API_KEY)

model = genai.GenerativeModel("gemini-1.5-pro")

def chat_bot(prompt):
    try:
        response = model.generate_content(prompt)
        return response.text  
    except Exception as e:
        return f"Error: {e}"

def track_package():
    tracking_id = input("Enter your tracking ID: ")
    return f"Tracking details for {tracking_id}: (Fetching details...)"

def view_offers():
    return "Here are the latest offers: \n1. 20% off on electronics \n2. Buy 1 Get 1 Free on shoes \n3. Free shipping on orders over $50"
print("I'm Ecommerce Chatbot")
while True:
    print("\nChoose an option:")
    print("1. Track Package")
    print("2. View Offers")
    print("3. Enable AI Chat")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        print(track_package())
    elif choice == "2":
        print(view_offers())
    elif choice == "3":
        print("AI Chat Enabled. Type 'exit' to return to the main menu.")
        while True:
            user_input = input("You: ")
            if user_input.lower() == "exit":
                print("Returning to the main menu...")
                break
            response = chat_bot(user_input)
            print("Chatbot:", response)
    elif choice == "4":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")

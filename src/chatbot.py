MY_API_KEY = "AIzaSyBzuHppLy47Su7vLxBYcNuMeMY_R8IEY2Q"
import google.generativeai as genai

genai.configure(api_key=MY_API_KEY)

def chat_bot():
    model = genai.GenerativeModel('gemini-pro')
    chat = model.start_chat(history=[])

    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            break

        response = chat.send_message(user_input, stream=True)
        for chunk in response:
            if chunk.text:
                print(chunk.text)

if __name__ == "__main__":
    chat_bot()
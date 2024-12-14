MY_API_KEY = "AIzaSyBzuHppLy47Su7vLxBYcNuMeMY_R8IEY2Q"
import google.generativeai as genai
from linkedin_api import Linkedin

genai.configure(api_key=MY_API_KEY)

linkedin_api = Linkedin('harshivkovur@gmail.com', 'H@rsh1N1blue')

# LinkedIn Profile fetch function
def get_linkedin_profile(profile_name):
    try:
        profile = linkedin_api.get_profile(profile_name)
        return profile
    except Exception as e:
        return f"Error fetching LinkedIn profile: {e}"

# Chatbot function
def chat_bot():
    model = genai.GenerativeModel('gemini-pro')
    chat = model.start_chat(history=[])

    while True:
        user_input = input("User: ")
        if user_input.lower() == 'exit':
            break
        
        if user_input.lower().startswith('linkedin'):
            profile_name = user_input.split(' ')[1]  # Get the profile name after 'linkedin'
            profile = get_linkedin_profile(profile_name)
            print(f"LinkedIn Profile for {profile_name}: {profile}")
        else:
            response = chat.send_message(user_input, stream=True)
            for chunk in response:
                if chunk.text:
                    print(chunk.text)

if __name__ == "__main__":
    chat_bot()
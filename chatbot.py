import os
from dotenv import load_dotenv
import google.generativeai as genai
from linkedin_api import Linkedin 

# Load environment variables from a .env file
load_dotenv()
'''
print("GOOGLE_API_KEY:", os.getenv("GOOGLE_API_KEY"))
print("LINKEDIN_EMAIL:", os.getenv("LINKEDIN_EMAIL"))
print("LINKEDIN_PASSWORD:", os.getenv("LINKEDIN_PASSWORD")) '''

class SecureChatbot:
    def __init__(self):
        # Securely load API keys and credentials from environment variables
        google_api_key = os.getenv('GOOGLE_API_KEY')
        linkedin_email = os.getenv('LINKEDIN_EMAIL')
        linkedin_password = os.getenv('LINKEDIN_PASSWORD')

        # Check if the required variables are set
        if not all([google_api_key, linkedin_email, linkedin_password]):
            raise ValueError("Missing one or more environment variables.")

        # Configure Google Generative AI
        genai.configure(api_key=google_api_key)
        self.model = genai.GenerativeModel('gemini-pro')
        self.chat = self.model.start_chat(history=[])

        # Initialize LinkedIn API
        self.linkedin_api = Linkedin(linkedin_email, linkedin_password)

    def get_linkedin_profile(self, profile_identifier):
        """
        Retrieve LinkedIn profile information
        
        :param profile_identifier: LinkedIn profile URL or ID
        :return: Profile information or None
        """
        try:
            profile = self.linkedin_api.get_profile(profile_identifier)
            return profile
        except Exception as e:
            print(f"Error retrieving LinkedIn profile: {e}")
            return None

    def chat_interaction(self):
        """
        Start an interactive chat session
        """
        print("Chatbot: Hello! Type 'exit' to end the conversation.")
        print("You can also type 'linkedin [profile]' to fetch a LinkedIn profile.")

        while True:
            user_input = input("You: ").strip()

            if user_input.lower() == 'exit':
                print("Chatbot: Goodbye!")
                break

            if user_input.startswith('linkedin '):
                profile_id = user_input.split(' ', 1)[1]
                profile = self.get_linkedin_profile(profile_id)
                if profile:
                    print("LinkedIn Profile:", profile)
                else:
                    print("Chatbot: Could not retrieve the LinkedIn profile.")
                continue

            # Send message to Gemini AI
            response = self.chat.send_message(user_input, stream=True)
            print("Chatbot:", end=" ")
            for chunk in response:
                if chunk.text:
                    print(chunk.text, end="", flush=True)
            print()  # New line after response

def main():
    chatbot = SecureChatbot()
    chatbot.chat_interaction()

if __name__ == "__main__":
    main()

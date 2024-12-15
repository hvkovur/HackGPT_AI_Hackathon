# HackGPT_AI_Hackathon

## Project Title
AI Chatbot for Course Recommendations Based on LinkedIn Profiles

## Prompt
Create an AI-driven chatbot that scrapes data from professional networks like LinkedIn and suggests relevant AI courses or learning paths on our platform. The bot should analyze user profiles to match their skills, job titles, and past experiences with courses that could enhance their careers.

## Installation
This project has not been deployed so testers need to create a .env files that contains environment variables. Here are the steps to running the project:

1. git clone https://github.com/hvkovur/HackGPT_AI_Hackathon.git
2. Create a ".env" file outside of the static and template folder
3. In the .env file you will need to enter your google API key, linkedin username, and linkedin password. Format it as shown: 
    GOOGLE_API_KEY=your_api_key
    LINKEDIN_EMAIL=your_linkedin_email
    LINKEDIN_PASSWORD=linkedin_password 
4. Once saving the ".env" file, run the project by opening your terminal and typing in "python flask_app.py". (You may need to do python3 flask_app.py based on the verison you have)
5. The terminal should output a http link that you can open in your browser and run. 
6. Enter "linkedin [profile]" to have the chatbot send out recommended courses. 
    For example the SVP at Apple is John Giannandrea. If you were to run "linkedin johngiannandrea" the chatbot will output courses that are suggested for him based on hsi profile. 
7. If you have any questions, please reach out to us! Thank you!

## Usage
This AI chatbot helps companies encourage LinkedIn users to explore relevant courses and resources to advance their knowledge and strengthen their candidacy in their field. The chatbot scrapes public LinkedIn profiles based on the user-inputted LinkedIn page URL and provides a list of recommended courses that can help users improve their skills and career prospects.

## Authors
- **Keerthi Surisetty** – (keerthisurisetty11@gmail.com)
- **Harshini Kovur** – (harshivkovur@gmail.com)
- **Sreenidhi Kannan** – (sreenidhikannan@gmail.com)

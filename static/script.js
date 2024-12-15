// Function to send the user input to the Flask backend and display the response
function sendMessage() {
    const userInput = document.getElementById('user-input').value;

    if (userInput.trim() !== "") {
        // Append the user's message to the chat box
        const chatBox = document.getElementById('chat-output');
        const userMessage = document.createElement('div');
        userMessage.className = 'user-message';
        userMessage.textContent = userInput;
        chatBox.appendChild(userMessage);

        const isLinkedInRequest = userInput.toLowerCase().startsWith('linkedin ');

        // Send the message to the /chat route
        fetch('/chat', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ 
                "user_input": userInput,
                "is_linkedin": isLinkedInRequest
             })
        })
        .then(response => response.json())
        .then(data => {
            const botMessage = document.createElement('div');
            botMessage.className = 'bot-message';
            if (data.response) {
                if(isLinkedInRequest) {
                    botMessage.innerHTML = `LinkedIn Profile Analysis:<br>${data.response}`;
                } else {
                    botMessage.innerHTML = data.response;
                }
            } else {
                botMessage.textContent = 'Sorry, I didn\'t get that!';
            }
            chatBox.appendChild(botMessage);

            chatBox.scrollTop = chatBox.scrollHeight;
        })
        .catch(error => {
            console.error('Error:', error);
            const errMessage = document.createElement('div');
            errMessage.className = 'bot-message';
            errMessage.textContent = 'An error occurred while processing your request.';
            chatBox.appendChild(errMessage);
        });

        // Clear the input field after sending the message
        document.getElementById('user-input').value = "";
    }
}

document.getElementById('user-input').addEventListener('keypress', function(event) {
    if (event.key === 'Enter') {
        sendMessage();
    }
});

// Event listener to display the initial greeting when the page loads
document.addEventListener('DOMContentLoaded', () => {
    const chatBox = document.getElementById('chat-output');
    const greetingMessage = document.createElement('div');
    greetingMessage.className = 'bot-message';
    greetingMessage.textContent = 'Hello! I will be your AI Assistant, ask me anything!';
    chatBox.appendChild(greetingMessage);
});

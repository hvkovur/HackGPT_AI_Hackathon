const chatInput = document.getElementById("chat-input");
const chatbox = document.getElementById("chatbox");

chatInput.addEventListener("keydown", function(event) {
    if (event.key === "Enter") {
        const userMessage = chatInput.value.trim();
        if (userMessage) {
            appendMessage(userMessage, "user");
            chatInput.value = ""; 

            // Send the LinkedIn profile to the backend
            fetch("/chat", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                },
                body: JSON.stringify({ message: userMessage }),
            })
            .then((response) => response.json())
            .then((data) => {
                const botMessage = data.message;
                // Add bot's response
                appendMessage(botMessage, "bot");  
            })
            .catch((error) => {
                console.error("Error:", error);
            });
        }
    }
});

// Function to append messages to chat container
function appendMessage(message, sender) {
    const messageElement = document.createElement("div");
    messageElement.classList.add("message", sender);
    messageElement.textContent = message;
    chatbox.appendChild(messageElement);
}

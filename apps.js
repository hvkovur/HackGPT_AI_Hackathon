document.getElementById("send-btn").addEventListener("click", () => {
    const userInput = document.getElementById("user-input").value.trim();
    if (userInput) {
        appendMessage("user", userInput);
        document.getElementById("user-input").value = ""; // Clear the input field
        getBotResponse(userInput);
    }
});

document.getElementById("user-input").addEventListener("keypress", (e) => {
    if (e.key === "Enter") {
        document.getElementById("send-btn").click();
    }
});

document.getElementById("fetch-btn").addEventListener("click", () => {
    const profile = document.getElementById("linkedin-profile").value.trim();
    if (profile) {
        fetchLinkedInProfile(profile);
    }
});

function appendMessage(sender, message) {
    const chatbox = document.getElementById("chatbox");
    const messageElement = document.createElement("div");
    messageElement.classList.add("chat-message");
    messageElement.classList.add(sender === "user" ? "user-message" : "bot-message");
    messageElement.textContent = sender === "user" ? `You: ${message}` : `Chatbot: ${message}`;
    chatbox.appendChild(messageElement);
    chatbox.scrollTop = chatbox.scrollHeight; // Scroll to the latest message
}

function getBotResponse(userInput) {
    // Simulate a bot response (You can replace this with an API call in real use)
    setTimeout(() => {
        if (userInput.toLowerCase().includes("linkedin")) {
            appendMessage("bot", "Chatbot: Please provide the LinkedIn profile username.");
        } else {
            appendMessage("bot", `Chatbot: You said: ${userInput}`);
        }
    }, 1000);
}

function fetchLinkedInProfile(profile) {
    // This is a placeholder. Replace this with a real API call to LinkedIn (via backend).
    setTimeout(() => {
        if (profile) {
            appendMessage("bot", `Chatbot: Fetching profile information for "${profile}"...`);
            // Simulate suggesting courses based on the profile
            appendMessage("bot", `Chatbot: Based on this profile, here are some course suggestions: \n- Data Science Specialization\n- Python for Beginners`);
        } else {
            appendMessage("bot", "Chatbot: No LinkedIn profile found.");
        }
    }, 1500);
}

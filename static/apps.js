// app.js
const chatForm = document.getElementById("chat-form");
const chatInput = document.getElementById("chat-input");
const chatContainer = document.getElementById("chat-container");

chatForm.addEventListener("submit", (event) => {
  event.preventDefault();

  const userMessage = chatInput.value;
  chatInput.value = "";

  appendMessage(userMessage, "user");

  // Send the message to the Flask backend
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
      appendMessage(botMessage, "bot");
    })
    .catch((error) => {
      console.error("Error:", error);
    });
});

// Function to append messages to chat container
function appendMessage(message, sender) {
  const messageElement = document.createElement("div");
  messageElement.classList.add("message", sender);
  messageElement.textContent = message;
  chatContainer.appendChild(messageElement);
  chatContainer.scrollTop = chatContainer.scrollHeight; // Auto-scroll
}

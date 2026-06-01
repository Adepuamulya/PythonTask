async function sendMessage() {

    const messageInput = document.getElementById("message");
    const chatBox = document.getElementById("chat-box");

    const message = messageInput.value.trim();

    if (message === "") return;

    // Display user message
    chatBox.innerHTML += `
        <div class="user">
            <span>${message}</span>
        </div>
    `;

    // Clear input
    messageInput.value = "";

    // Show loading animation
    chatBox.innerHTML += `
        <div id="loading" class="bot">
            <div class="loader">
                <span></span>
                <span></span>
                <span></span>
            </div>
        </div>
    `;

    chatBox.scrollTop = chatBox.scrollHeight;

    try {

        const response = await fetch("/chat", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                message: message
            })
        });

        const data = await response.json();

        // Remove loader
        const loader = document.getElementById("loading");
        if (loader) {
            loader.remove();
        }

        // Display bot response
        chatBox.innerHTML += `
            <div class="bot">
                <span>${data.response}</span>
            </div>
        `;

    } catch (error) {

        const loader = document.getElementById("loading");
        if (loader) {
            loader.remove();
        }

        chatBox.innerHTML += `
            <div class="bot">
                <span>❌ Error connecting to server</span>
            </div>
        `;

        console.error("Error:", error);
    }

    chatBox.scrollTop = chatBox.scrollHeight;
}

// Send message on Enter key
document.addEventListener("DOMContentLoaded", () => {

    const input = document.getElementById("message");

    input.addEventListener("keypress", function(event) {

        if (event.key === "Enter") {
            sendMessage();
        }

    });

});
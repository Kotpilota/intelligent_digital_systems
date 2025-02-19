document.addEventListener('DOMContentLoaded', function() {
    const userItems = document.querySelectorAll('.user-item');
    const chatHeader = document.querySelector('.chat-header h3');
    const messageInput = document.querySelector('.message-input');
    const sendButton = document.querySelector('.send-button');
    const messagesContainer = document.querySelector('.messages-container');
    const inputArea = document.querySelector('.input-area');

    userItems.forEach(item => {
        item.addEventListener('click', function() {
            // Remove active class from all users
            userItems.forEach(user => user.classList.remove('active'));
            // Add active class to clicked user
            this.classList.add('active');
            // Update chat header
            chatHeader.textContent = this.textContent;
            // Clear messages and remove no-chat message
            messagesContainer.innerHTML = '';
            // Show input area
            inputArea.classList.remove('hidden');
            // Reset messages container styles
            messagesContainer.style.justifyContent = 'flex-start';
            messagesContainer.style.alignItems = 'flex-start';
        });
    });

    function sendMessage() {
        const message = messageInput.value.trim();
        if (message) {
            const messageElement = document.createElement('div');
            messageElement.classList.add('message', 'sent');
            messageElement.textContent = message;
            messagesContainer.appendChild(messageElement);
            messageInput.value = '';
            messagesContainer.scrollTop = messagesContainer.scrollHeight;
        }
    }

    sendButton.addEventListener('click', sendMessage);
    messageInput.addEventListener('keypress', function(e) {
        if (e.key === 'Enter') {
            sendMessage();
        }
    });
});
const conversationDiv = document.getElementById('conversation');
const pauseButton = document.getElementById('pause-button');
let autoScroll = true;
const md = window.markdownit();
let currentPersonality = 'bot1';
let paused = false;
let eventSource = null;

function createEventSource() {
    eventSource = new EventSource('/events');
    eventSource.onmessage = function(event) {
        if (!paused) {
            const message = event.data ? event.data.trim() : '';
            if (message) {
                const botClass = currentPersonality;
                const messageDiv = document.createElement('div');
                messageDiv.className = botClass;
                messageDiv.innerHTML = message;  // Directly use HTML content
                conversationDiv.appendChild(messageDiv);

                currentPersonality = (currentPersonality === 'bot1') ? 'bot2' : 'bot1';

                if (autoScroll) {
                    conversationDiv.scrollTop = conversationDiv.scrollHeight;
                }
            }
        }
    };
    eventSource.onerror = function() {
        console.error('EventSource failed.');
    };
}

async function togglePause() {
    paused = !paused;
    await fetch('/pause', { method: 'POST' });
    if (paused) {
        pauseButton.textContent = 'Resume';
        pauseButton.classList.add('resume');
        pauseButton.classList.remove('paused');
    } else {
        pauseButton.textContent = 'Pause';
        pauseButton.classList.remove('resume');
        pauseButton.classList.add('paused');
    }
}

document.addEventListener('keydown', function(event) {
    if (event.code === 'Space') {
        event.preventDefault();
        togglePause();
    }
});

pauseButton.addEventListener('click', togglePause);

conversationDiv.addEventListener('scroll', function() {
    const isScrolledToBottom = conversationDiv.scrollHeight - conversationDiv.clientHeight <= conversationDiv.scrollTop + 1;
    autoScroll = isScrolledToBottom;
});

createEventSource();

window.addEventListener('beforeunload', function() {
    if (eventSource) {
        eventSource.close();
    }
});

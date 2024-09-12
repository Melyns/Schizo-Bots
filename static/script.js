const conversationDiv = document.getElementById('conversation');
const pauseButton = document.getElementById('pause-button');

let autoScroll = true;
const md = window.markdownit();
let currentPersonality = 'bot1';

function createEventSource() {
    const eventSource = new EventSource('/events');
    eventSource.onmessage = function(event) {
        const message = event.data.trim();
        if (message) {
           
            const botClass = currentPersonality;

           
            const formattedMessage = md.render(message);
            const styledMessage = `<div class="${botClass}">${formattedMessage}</div>`;
            conversationDiv.innerHTML += styledMessage;

            currentPersonality = (currentPersonality === 'bot1') ? 'bot2' : 'bot1';

            if (autoScroll) {
                conversationDiv.scrollTop = conversationDiv.scrollHeight;
            }
        }
    };
    eventSource.onerror = function() {
        console.error('EventSource failed.');
    };
}

function togglePause() {
    fetch('/pause', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' }
    })
    .then(response => response.json())
    .then(data => {
        if (data.paused) {
            pauseButton.classList.add('visible');
            pauseButton.textContent = 'Paused';
        } else {
            pauseButton.classList.remove('visible');
            pauseButton.textContent = 'Pause';
        }
    });
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

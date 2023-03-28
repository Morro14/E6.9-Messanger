console.log('chat.js activated');

let inputElement = document.querySelector(".chat-input");
let chatOutputElement = document.querySelector(".chat-window");
let inputSubmitElement = document.querySelector("#id-message-submit");


const chatName = JSON.parse(document.getElementById('chatName').textContent);
const username = JSON.parse(document.getElementById('userName').textContent);
console.log(username)

inputElement.focus();

inputElement.onkeyup = function (e) {
    if (e.keyCode == 13) {
        inputSubmitElement.click();
    }
};

inputSubmitElement.onclick = function (e) {
    if (inputElement.value.length === 0) return;
    chatSocket.send(JSON.stringify({
        "message": inputElement.value,
        "username": username
    }));
    inputElement.value = "";
};

let chatSocket = null;

function chatWebSocket() {
    chatSocket = new WebSocket("ws://" + window.location.host + "/ws/chat/" + chatName + "/");

    chatSocket.onopen = function (e) {
        console.log("Connection is on!");

    };

    chatSocket.onclose = function (e) {
        console.log("Something unexpected happened..");
        // setTimeout(function () {
        //     console.log("Reconnecting..");
        //     chatWebSocket();
        // }, 2000);
    };

    chatSocket.onmessage = function (e) {
        const data = JSON.parse(e.data);
        console.log(data);

        switch (data.type) {
            case "chat_message":
                let div = document.createElement("div");
                div.innerHTML = data.username + ":" + data.message;
                chatOutputElement.appendChild(div);
                break;
            default:
                console.error("Unknown message type!");
                break;
        }

        chatOutputElement.scrollTop = chatOutputElement.scrollHeight;
    };

    chatSocket.onerror = function (err) {
        console.log("WebSocket encountered an error: " + err.message);
        console.log("Closing the socket.");
        chatSocket.close();
    }
}

chatWebSocket();


// const output = document.querySelector(".chat-window");
// const submitValue = document.querySelector(".chat-input");




// function submit() {
//     text = submitValue.firstElementChild.innerHTML;
//     console.log(text);
//     submitValue.addEventListener("keyup", (eve) => {
//         if (eve.key === 'Enter') {
//             sendMessage(text);
//         }
//     });
// }

// function sendMessage(content) {
//     console.log("Trying to send the message..")
//     let xhr = new XMLHttpRequest();
//     xhr.open('POST', 'http://127.0.0.1:8000/messages/');
//     xhr.setRequestHeader("Accept", "application/json");
//     xhr.setRequestHeader("Content-Type", "application/json");

//     xhr.onreadystatechange = function () {
//         if (xhr.readyState === 4) {
//             console.log(xhr.status);
//             console.log(xhr.responseText);
//         }
//     };
//     let data = { "body": content };
//     xhr.send(data);
// }
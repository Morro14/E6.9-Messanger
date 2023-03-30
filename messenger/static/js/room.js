console.log('room.js activated');

let inputElement = document.querySelector(".chat-input");
let chatOutputElement = document.querySelector(".chat-window");
let inputSubmitElement = document.querySelector("#id-message-submit");
let userList = document.querySelector('#online-user-list');


const roomPk = JSON.parse(document.getElementById('roomPk').textContent);
const username = JSON.parse(document.getElementById('userName').textContent);


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
    }));
    inputElement.value = "";
};

// user list

function userListAdd(value) {
    let newOption = document.createElement("option");
    newOption.value = value;
    newOption.innerHTML = value;
    userList.appendChild(newOption);
}

function userListRemove(value) {
    let oldOption = document.querySelector("option[value='" + value + "']");
    if (oldOption !== null) oldOption.remove();
}

// websocket

let chatSocket = null;

function chatWebSocket() {
    chatSocket = new WebSocket("ws://" + window.location.host + "/ws/room/" + roomPk + "/");

    chatSocket.onopen = function (e) {
        console.log("Connection is on!");

    };

    chatSocket.onclose = function (e) {
        console.log("Something unexpected happened..");
    };

    chatSocket.onmessage = function (e) {
        const data = JSON.parse(e.data);

        switch (data.type) {
            case "room_message":
                let div = document.createElement("div");
                div.innerHTML = data.username + ": " + data.message;
                chatOutputElement.appendChild(div);
                break;
            case "user_list":
                for (let i = 0; i < data.users.length; i++) {
                    userListAdd(data.users[i]);
                }
                break;
            case "user_join":
                chatOutputElement.value += data.user + "joined the room. \n";
                userListAdd(data.user);
                break;
            case "user_leave":
                chatOutputElementvalue += data.user + "has left the room. \n"
                userListRemove(data.user);
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


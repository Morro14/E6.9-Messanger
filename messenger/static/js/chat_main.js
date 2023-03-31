console.log('chat_main.js is active')

// user list
function requestUserList(url, callback) {
    const xhr = new XMLHttpRequest();

    xhr.open('GET', url, true);

    xhr.onload = function () {
        if (xhr.status != 200) {
            console.log('Status:', xhr.status);
        } else {
            const result = JSON.parse(xhr.response);
            if (callback) {
                callback(result);
            }
        }
    };
    xhr.onerror = function () {
        console.log('Error! Status:', xhr.status);
    };
    xhr.send();
};


const resultNode = document.querySelector('.user-list-result');


function displayResults(apiData) {
    let names = '';
    apiData.results.forEach(item => {
        const userName = `<tr><td class="item-list"><a href="/chat/${item.username}" %}">${item.username}</a></td></tr>`;
        names = names + userName;
    });
    resultNode.innerHTML = names;
}


requestUserList('http://127.0.0.1:8000/users/', displayResults);

// chat select/create
async function getChatRoom(name) {
    let data = await fetch('http://127.0.0.1:8000/rooms/', {
        headers: {
            'Accept': 'application/json',
            'Content-Type': 'application/json',
        },
        method: 'GET',
    })
        .then((response) => {
            return response.json();
        });
    let chat_name = null;
    data.results.forEach(item => {
        if (item['name'] == name) {
            chat_name = name;
        }
    });
    return chat_name;
};

let searchButton = document.querySelector("#search-button");
let searchBar = document.querySelector("#search-bar");
let linkSearch = document.querySelector('#search-link');
let linkCreate = document.querySelector('#create-link');
let createButton = document.querySelector("#create-button");
let createBar = document.querySelector("#create-bar");

searchButton.onclick = function (e) { roomSearch(searchBar.value, linkSearch); }
createButton.onclick = function (e) { roomCreate(createBar.value, linkCreate); }

// room search function
async function roomSearch(input, linkElem) {
    let chatName = await getChatRoom(input);
    console.log(chatName);
    if (chatName !== null) {
        linkElem.setAttribute("href", `http://127.0.0.1:8000/chat/room/${input}`);
        linkElem.click();
    } else { alert("This room doesen't exist."); }

}

// room create function
async function roomCreate(input, linkElem) {
    let chatName = await getChatRoom(input);
    if (chatName == null) {
        linkElem.setAttribute("href", `http://127.0.0.1:8000/chat/room/${input}`);
        linkElem.click();
    } else { alert("This name is already taken."); }
}







let nameValue = document.querySelector("#name-change");
let nameChangeButton = document.querySelector("#name-change-button");
let user = JSON.parse(document.querySelector("#username").textContent);




function requestPost(name) {
    fetch(`http://127.0.0.1:8000/users/${user}/`, {
        method: "PATCH",
        headers: {
            'Accept': 'application/json',
            'Content-Type': 'application/json',
        },
        body: { "username": name.value },
        csrfmiddlewaretoken: '{{ csrf_token }}',
    }).then(console.log('Request has been sent.')).catch((e) => console.log(`Error ${e}`))
}


// nameChangeButton.onclick = function (e) {
//     requestPost(nameValue);
// };
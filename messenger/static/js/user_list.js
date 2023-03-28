console.log('user_list.js is active')


function useRequest(url, callback) {
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


useRequest('http://127.0.0.1:8000/users/', displayResults);




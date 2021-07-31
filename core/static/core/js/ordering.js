function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

async function incPosition(url) {
    const csrftoken = getCookie('csrftoken')
    const request = new Request(url, {
        headers: {'X-CSRFToken': csrftoken}
    })
    const result = await fetch(request, {method: 'POST', mode: 'same-origin'})

    console.log(result)

}

function decPosition() {
    console.log("DEC")

}
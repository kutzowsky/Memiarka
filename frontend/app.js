API_URL = "https://dl430cgr4b.execute-api.eu-central-1.amazonaws.com/Prod/meme"

let onFormSubmit = event => {
    event.preventDefault();
    generate();
}

let onResetButtonClick = _ => {
    toggleView();
}

let generate = _ => {
    let button = document.getElementById('generate-button');
    let firstLineInput = document.getElementById('first-line');
    let secondLineInput = document.getElementById('second-line');

    let firstLine = firstLineInput.value;
    let secondLine = secondLineInput.value;

    button.ariaBusy = 'true';

    let url = `${API_URL}?firstLine=${firstLine}&secondLine=${secondLine}`;

    fetch(url)
        .then(response => {
            if (response.ok) {
                return response.json();
            }
            console.error(response);
            throw new Error('Response code is not 200');
        })
        .then(responseJson => {
            console.log(responseJson.memeUrl);

            firstLineInput.value = '';
            secondLineInput.value= '';

            setImagrUrl(responseJson.memeUrl);
            toggleView();

            button.ariaBusy = 'false';
        })
        .catch((error) => {
            button.ariaBusy = 'false';
            showErrorText();
            console.error(error);
        });
}

let toggleView = _ => {
    const NOT_VISIBLE_CLASS = 'not-visible';

    let generatorElement = document.getElementById('generator-container');
    let resultElement = document.getElementById('result-container');

    let formIsVisible = !generatorElement.classList.contains(NOT_VISIBLE_CLASS);

    if (formIsVisible) {
        generatorElement.classList.add(NOT_VISIBLE_CLASS);
        resultElement.classList.remove(NOT_VISIBLE_CLASS);
    } else {
        generatorElement.classList.remove(NOT_VISIBLE_CLASS);
        resultElement.classList.add(NOT_VISIBLE_CLASS);
    }
}

let setImagrUrl = imageUrl => {
    let memeImage = document.getElementById('meme-image');
    let downloadButton = document.getElementById('download-button');

    memeImage.src = imageUrl;
    downloadButton.href = imageUrl;
}

let showErrorText = _ => {
    const errorTextContainer = document.getElementById('error-text-container');
    errorTextContainer.classList.remove('not-visible');
}

const form = document.getElementById('generator-form');
form.addEventListener('submit', onFormSubmit);
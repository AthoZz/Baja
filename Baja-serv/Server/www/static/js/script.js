document.addEventListener('DOMContentLoaded', function() {
    const startButton = document.getElementById('startButton');
    const stopButton = document.getElementById('stopButton');
    const currentState = document.getElementById('currentState');
    const resetButton = document.getElementById('resetButton');
    const resetResult = document.getElementById('resetResult');
    const updateGraphsButton = document.getElementById('updateGraphsButton');
    const rpm1Graph = document.getElementById('rpm1Graph');
    const rpm2Graph = document.getElementById('rpm2Graph');
    const strainGageGraph = document.getElementById('strainGageGraph');

    function fetchWithRetry(url, options = {}, retries = 5) {
        return fetch(url, options)
            .then(response => {
                if (!response.ok) throw new Error('Network response was not ok');
                return response.json();
            })
            .catch(error => {
                if (retries > 0) {
                    console.error('Retrying fetch:', error);
                    return fetchWithRetry(url, options, retries - 1);
                } else {
                    console.error('Max retries reached:', error);
                    throw error;
                }
            });
    }

    startButton.addEventListener('click', function() {
        fetchWithRetry('/Start')
            .then(data => {
                currentState.textContent = 'Running';
            })
            .catch(error => console.error('Error:', error));
    });

    stopButton.addEventListener('click', function() {
        fetchWithRetry('/Stop')
            .then(data => {
                currentState.textContent = 'Stopped';
            })
            .catch(error => console.error('Error:', error));
    });

    resetButton.addEventListener('click', function() {
        fetchWithRetry('/delete-all-tables')
            .then(data => {
                resetResult.textContent = data.result;
                return fetchWithRetry('/creat'); // Chaînez le second appel ici
            })
            .then(data => {
                resetResult.textContent += ` ${data.result}`; // Ajoutez le résultat du second appel
            })
            .catch(error => console.error('Error:', error));
    });

    updateGraphsButton.addEventListener('click', function() {
        const cacheBuster = new Date().getTime(); // Cache-buster basé sur l'heure actuelle
        updateImageWithDelay(rpm1Graph, `/get-RPM1-5min?cb=${cacheBuster}`, 0);
        updateImageWithDelay(rpm2Graph, `/get-RPM2-5min?cb=${cacheBuster}`, 500); // 500 millisecondes de délai après le premier
        updateImageWithDelay(strainGageGraph, `/get-strain_gage-5min?cb=${cacheBuster}`, 1000); // 1000 millisecondes de délai après le premier
    });

    function updateImageWithDelay(imgElement, url, delay) {
        setTimeout(() => {
            const newImg = new Image();
            newImg.onload = function() {
                imgElement.src = newImg.src;
            };
            newImg.onerror = function() {
                console.error('Error loading image:', newImg.src);
            };
            newImg.src = url;
        }, delay);
    }

    function updateCurrentState() {
        fetchWithRetry('/get-current-state')
            .then(data => {
                currentState.textContent = data.state;
            })
            .catch(error => console.error('Error:', error));
    }

    // Mettre à jour l'état actuel toutes les 5 secondes
    setInterval(updateCurrentState, 2000);

    // Mise à jour initiale de l'état
    updateCurrentState();
});

// Retrieve selectedText from local storage and update the input
chrome.storage.local.get(['selectedText'], function(result) {
    const selectedText = result.selectedText || 'No text selected.';
    const inputEl = document.getElementById('userprompt');
    inputEl.value = selectedText;
});

// Function to clear the input content and local storage
function clearInputAndLocalStorage() {
    const inputEl = document.getElementById('userprompt');
    const resultDisplay = document.getElementById('resultDisplay');

    // Check if the input is empty
    if (inputEl.value.trim() === '') {
        resultDisplay.innerText = 'Please enter content to analyze.';
    } else {
        // Placeholder logic, replace with your actual analysis
        const isTrue = Math.random() < 0.5; // Replace with your analysis logic
        resultDisplay.innerText = isTrue ? 'Our Model Says It\'s Fake' : 'Our Model Says It\'s Not Fake';

        // Clear the input content
        inputEl.value = '';

        // Clear selectedText from local storage
        chrome.storage.local.remove('selectedText', function() {
            console.log('selectedText removed from local storage');
        });
    }
}

// Attach the clearInputAndLocalStorage function to the button click event
document.getElementById('processButton').addEventListener('click', clearInputAndLocalStorage);

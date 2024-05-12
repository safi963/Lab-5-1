// Generate a random number between 1 and 100
const secretNumber = Math.floor(Math.random() * 100) + 1;
let attempts = 0;

// Get DOM elements
const guessInput = document.getElementById('guessInput');
const guessButton = document.getElementById('guessButton');
const resultElement = document.getElementById('result');
const attemptsElement = document.getElementById('attempts');

// Add event listener to the guess button
guessButton.addEventListener('click', function() {
    const guess = parseInt(guessInput.value);

    // Check if the guess is valid
    if (isNaN(guess) || guess < 1 || guess > 100) {
        resultElement.textContent = 'Please enter a valid number between 1 and 100.';
        return;
    }

    attempts++;

    if (guess === secretNumber) {
        resultElement.textContent = `Congratulations! You guessed the number ${secretNumber} in ${attempts} attempts.`;
        guessInput.disabled = true;
        guessButton.disabled = true;
    } else if (guess < secretNumber) {
        resultElement.textContent = 'Your guess is too low. Try again!';
    } else {
        resultElement.textContent = 'Your guess is too high. Try again!';
    }

    attemptsElement.textContent = `Attempts: ${attempts}`;
});

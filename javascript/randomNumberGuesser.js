const prompt = require("prompt-sync")();

// min value *  the rounded value of the difference of our max value - min value
const target = 10 + Math.round(Math.random() * 90); //in it's default mode, math.random will gen random # b/t 0-1 (a long decimal value)

console.log(target);

let guesses = 0;

while (true) { 
    guesses ++;
    //Number converts the user input string to a number
    const guess = Number(prompt("Guess the number (0-100): ")); // NaN = not a number (a special type in js)
    if (guess > target) {  //!== is the not equal to operator
        console.log("Your guess is too high.");
    } else if (guess < target) {
        console.log("Your guess is too low.");
    } else {
        console.log("You guessed it!");
        break //exits the closest internal loop and goes to what happens after it
        //continue will restart the loop
    }
}

console.log("You guessed the number in", guesses, "tries!");
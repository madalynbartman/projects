// you don't need ; for it to run. they just represent a line break
const prompt = require("prompt-sync")(); //loads the module and declares a const equal to it

console.log("Welcome to the computer hardware quiz!");

let correctAnswers = 0;
const totalQuestions = 3;

const answer1 = prompt("What is the brain of the computer? "); // let creates a dynamic variable. const is immutable
const correctAnswer1 = "CPU";

if (answer1.toUpperCase === correctAnswer1) { // === compares equivalent. == works a bit differently
    console.log("You got it correct!");
    correctAnswers ++ // += 1 will add one to whatever the value of correctAnswers is. ++ just increments it
} else {
    console.log("You got it wrong..");
}

const answer2 = prompt("What is better a 3090ti or a 4060? "); // let creates a dynamic variable. const is immutable
const correctAnswer2 = "3090ti";

if (answer1.toLowerCase === correctAnswer1) { // === compares equivalent. == works a bit differently
    console.log("You got it correct!");
} else {
    console.log("You got it wrong..");
}

const answer3 = prompt("What is the reccomended amount of RAM in 2023? "); // let creates a dynamic variable. const is immutable
const correctAnswer3 = "16GB";

if (answer3.toLowerCase === correctAnswer3) { // === compares equivalent. == works a bit differently
    console.log("You got it correct!");
} else {
    console.log("You got it wrong..");
}

const percent = Math.round((correctAnswers / totalQuestions) * 100);

console.log("You got", correctAnswers, "questions correct!");
console.log("You scored", percent.toString + "%"); //toString doesnt modify the variable, it gives us the string representation of it so we can cat it
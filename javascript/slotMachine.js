// 1. Deposit some money
// 2. Determine number o flines to bet on
// 3. Collect a bet amount
// 4. spin the slot machine & transpose the slot machine (matrix)
// 5. Check if the user won
// 6. Give the user their winnings
// 7. Play again or handle a situation where the user has no money left

// two ways to write a function
// ex 1 regular style
// function deposit() {
//     return 1
// }

// const x = deposit()

// ES6 style (used more widely than the first way)
// const desposit = () => {

// }

const prompt = require("prompt-sync")(); // the second set of () gives access to function for user input

//order of program
// imports & libraries 
// global variables 
// classes and functions
// main line or other aspects of your program


// global vars are all caps
const ROWS = 3;
const COLS = 3;

// snake case is the convention for all caps instead of camel case
// objects in js allow you to have key value pairs
const SYMBOLS_COUNT = {
    A: 2,
    B: 4,
    C: 6,
    D: 8
}

//SYMBOLS_COUNT["A"] //will give you the value 2

const SYMBOL_VALUES = {
    A: 5,
    B: 4,
    C: 3,
    D: 2
}

const deposit = () => {
    while (true) {
        const depositAmount = prompt("Enter a deposit amount: ");
            const numberDepositAmount = parseFloat(depositAmount);

            if (isNaN(numberDepositAmount) || numberDepositAmount <= 0) {
                console.log("Invalid deposit amount, try again.:");
            } else {
                return numberDepositAmount;
            }

    }
};

const getNumberOfLines = () => {
    while (true) {
        const lines = prompt("Enter the number of lines to bet on (1-3): ");
            const numberOfLines = parseFloat(lines);

            if (isNaN(numberOfLines) || numberOfLines <= 0 || numberOfLines > 3) {
                console.log("Invalid number of lines, try again.:");
            } else {
                return numberOfLines;
            }

    }
}

//balance is a parameter and needs to be passed when the getBet code is called
const getBet = (balance) => {
    while (true) {
        const bet = prompt("Enter the bet per line: ");
            const numberBet = parseFloat(bet);

            if (isNaN(numberBet) || numberBet <= 0 || numberBet > balance / bet) {
                console.log("Invalid bet, try again.:");
            } else {
                return numberBet;
            }

    }
}

const spin = () => { // an array is just a colelction of multiple elements
    const symbols = []; // it's a ref to an array so you can add values to it even though it's an array
    for (const [symbol, count] of Object.entries(SYMBOLS_COUNT)) {
        for (let i = 0; i < count; i++) {
            symbols.push(symbol); // push is append in js
        }
    }

    const reels = [];
    for (let i = 0; i < COLS; i++) {
        reels.push([]);
        const reelSymbols = [...symbols];
        for (let j =0; j < ROWS; j++){
            const randomIndex = Math.floor(Math.random() * reelSymbols.length); // the max poss number is however many symbols we have. math.floor rounds down to nearest int (because math.random generates a float). we need to round down so we don't accidentally round up to a number out of the array. This is becuase we can only possibly work with the length of our reels minus one.
            const selectedSymbol = reelSymbols[randomIndex];
            reels[i].push(selectedSymbol);
            reelSymbols.splice(randomIndex, 1);
        }
    }

    return reels;
};

const transpose = (reels) => {
    const rows = [];

    for (let i = 0; i < ROWS; i++) {
        rows.push([]);
        for (let j = 0; j < COLS; j++) {
            rows[i].push(reels[j][i])
        }
    }

    return rows
}

const printRows = (rows) => {
    for (const row of rows) {
        let rowString = ""
        for (const [i, symbol] of row.entries()) {
            rowString += symbol
            if (i != row.length - 1) {
                rowString += " | "
            }
        }
        console.log(rowString)
    }
}

const getWinnings = (rows, bet, lines) => {
    let winnings = 0;

    for (let row = 0; row < lines; row ++) {
        const symbols = rows[row];
        let allSame = true;

        for (const symbol of symbols) {
            if (symbol != symbols[0]) {
                allSame = false;
                break;
            }
        }

        if (allSame) {
            winnings += bet * SYMBOL_VALUES[symbols[0]]
        }
    }

    return winnings;
};

const game = () => {
    // const stands for constant and that's how you declare a constant variable
    // let allows you to adjust the value of the variable. It's not a constant
    let balance = deposit();

    while (true) {
        console.log("You have a balance of $" + balance);
        const numberOfLines = getNumberOfLines();
        const bet = getBet(balance, numberOfLines);
        balance -= bet * numberOfLines;
        const reels = spin();
        const rows = transpose(reels); //flips the orientation of the matrix
        printRows(rows);
        const winnings = getWinnings(rows, bet, numberOfLines);
        balance += winnings;
            console.log("You won, $" + winnings.toString()); // console.log is print in js

            if (balance <= 0) {
                console.log("You ran out of money!");
                break;
            }

            const playAgain = prompt("Do you want to play again (y/n)? ");

            if (playAgain != "y") break;
    }
}

game();



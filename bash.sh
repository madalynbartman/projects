#!/usr/bin/env bash

# shebang makes the script executable. it knows to run bash. you dont have to specify: bash scrippy.sh just scrippy.sh

cat << EOF
This is a 
multiline
text string
EOF

echo Hello

printf hello

command echo hello

builtin echo hello #builtins are different than commands

command -V df

command -V echo

enable -n echo

enable echo 

help echo

help # list of the builtins bash provides

# ~ is always set to the current values of $HOME

# Brace expansion creates sets or ranges

echo {1..10}

echo {10..1}

echo {01..100}

echo {a..z}

echo {Z..A}

echo {1..30..3}

echo {a..z..2}

touch file_{01..12}{a..d}

ll

rm file_*

echo {cat,dog,fox}

echo {cat,dog,fox}_{1..5}

clear

head -n1 {dir,dir2,dir3}/lorem.txt

# Parameter expansion retrieves and transforms stored values

greeting="hello"
echo $greeting

echo ${greeting:2:3}

echo ${greeting/ll/zz}

echo ${greeting/e/_}

# $*(...) Command substitution puts the output of one command inside another. Older representation: `...`

uname -r

echo "The kernel is $(uname -r)."

echo "The Python version is $(python -V)."

echo "Result: $(python3 -c 'print("Hello from Python!")' | tr [a-z] [A-Z])"

# $((...)) Arithmetic expansion does calculations. Older representations: $[...]

echo $(( 2 + 2 ))

echo $(( 4 - 2 ))

echo $(( 4 * 5 ))

echo $(( 4 / 5 ))

# echo prints text to the standard output

echo hello world

worldsize=big

echo hello $worldsize world

echo "The kernel is $(uname -r)."

# using single quotes (strong quotes) means everything inside is literal text. Double quotes will allow for expansion nad mixing literal text with values (and spaces). 

mygreeting=hello

mygreeting2="Good morning!"

number=16

echo $mygreeting

echo $mygreeting2

echo $number

myname=biggie

echo "The value of the myname variable is: $myname"

declare -l lowerstring="This is some TEXT!"
echo "The value of the lowerstring variable is: $lowerstring"
lowerstring="Let's CHANGE the VALUE!"
echo "The value of the lowerstring variable is: $lowerstring"

declare -u upperstring="This is some TEXT"
echo "The value of the upperstring variable is: $upperstring"
upperstring="Let's CHANGE the VALUE!"
echo "The value of the upperstring variable is: $upperstring"

declare -p # lists the variables you've declared in that session

echo $USER

# $((...)) Arithmetic expansion returns the result of mathematical operations. Older representation: $[...]

# ((...)) Arithmetic evaluation performs calculations and changes the value of variables.

echo $((4+4))

echo $((8-5))

echo $((2*3))

echo $((8/4))

echo $(( (3+6) - 5 * (5*2) ))

a=3

((a+=3))
echo $a

((a++))
echo $a

((a++))
echo $a

((a--))
echo $a

((a+=2))
echo $a

((a-=3))
echo $a

((a*=2))
echo $a

((a/=2))
echo $a

b=5
echo $b

b=$b+2

declare -i b=3
echo $b
b=$b+4
echo $b

echo $((1/3))

# bc and awk can handle floats

declare -i c=1
declare -i d=3

e=$(echo "scale=3; $c/$d" | bc)
echo $e

echo $RANDOM

echo $(( 1 + RANDOM % 10 ))

echo $(( 1 + RANDOM % 20 ))

#[ ... ] is an alias for the test built-in and is used to test or evaluate expressions

help test | less

[ -d ~ ]

# The shell returns a status code after a command completes

# 0 means sucess, and 1 means failure

# 0 and 1 can be trated as truth values ( 0=true, 1=false)

# With truth values, we can apply logic to our scripts

# The return status is trated as the value of the command

# We can look at the return status of the most recent command with $?

echo $?

[ -d /bin/bash ]; echo $?

[ -d /bin ]; echo $?

[ "cat" = "dog" ]; echo $?

[ "cat" = "cat" ]; echo $?

[ 4 -lt 5 ]; echo $?

[ 4 -lt 3 ]; echo $?

[ ! 4 -lt 3 ]; echo $?

# [[ ... ]]] extended test

[[ 4 -lt 3 ]]; echo $?

[[ -d ~ && -a /bin/bash ]]; echo $?

[[ -d ~ && -a /bin/mash ]]; echo $?

[[ -d ~ || -a /bin/mash ]]; echo $?

# If the test returns success, it will run the echo statement 
# If the test fails, the echo statement doesn't run.
[[ -d /bin/bash ]] && echo /bin/bash ~ is a directory

ls && echo "listed the directory"

true && echo "success!"

false && echo "success!"

[[ "cat" =~ c. * ]]; echo $?

[[ "bat" =~ c. * ]]; echo $?

# There are regex courses by this author on LinkedIn Learning

# Extended test is BASH specific. Test can run with sh 

# echo -e Interprets escaped characters like \n, \t, \a, and other control characters

echo -e "Name\t\Number"; echo -e "bigiie\t\t123"

echo -e "This text\nbreaks over\nthree lines"

echo -e "\a"

# 033 = text formatting
echo -e "\033[33;44mColor Text\033[0m"

ulinered="\033[4;31;40m"
red="\033[31;40m"
none="\033[0m"

echo -e $ulinered"ERROR:"$none$red" Something went wrong. xP"$none

# printf "..." ... Outputs text using placeholders and formatting
# (without relying on command substitution)

echo "The results are: $(( 2 + 2 )) and $(( 3 / 1 ))"

printf "The results are: %d and %d\n" $(( 2 + 2 )) $(( 3 / 1 ))

# %d is digit and %s is string

# Arrays in Bash
# store multiple values
# Two types of arryas in BASH
# Indexed array (refer to index in list) 

declare -a snacks=("apple" "banana" "orange")
echo ${snacks[2]}

snacks[5]="grapes"
snacks+=("mango")

echo ${snacks[@]} # @ tells BASH to display the whole array

for i in {0..6}; do echo "$i: ${snacks[i]}"; done

# Associative Array
# Can specified key value pairs instaed of just an indexed list

declare -A office
office[city]="San Fransisco"
office["building name"]="HQ West"
echo ${office["building name"]} is in ${office [city]}

# They have courses on awk and sed on LinkedinLearning too

# Control Structures in BASH
# Run specified code based on conditions

# If statement: 
# executes code based on a conditional expression that returns a truth value
# Commands always return with a 0 or non-zero status interpreted as true or false

declare -i a=3

if [[ $a -gt 4 ]]
then 
    echo "$a is greater than 4!"
else 
    echo "$a is not greater than 4!
fi

if (($a>4))
then 
    echo "$a is greater than 4!"
elif (($a>2))
then
    echo "$a is greater tahn 2."
else 
    echo "$a is not greater than 4!
fi

# Loops are control structures that run a specific piece of code until its told to end

# While Loops
# run as long as their condition is true

# until Loops
# run as long as their condition is false

echo "While Loop"

declare -i n=0
while ((n<100))
do 
    echo "n:$n"
    ((n++))
done


echo -e "\n Until Loop"

declare -i m=0
until ((m==10)); do
    echo m:$m
    ((m++))
done

# For Loops iterate through a list of items, running code once for each item

for i in 1 2 3
do
    echo $i
done

for i in 1 2 3; do echo $1; done # one line ver

for i in (( i=1; i<=10; i++ ))
do 
    echo $i
done

declare -a fruits=("apple" "banana" "cherry")
for i in ${fruits[@]}
do 
    echo $i
done

declare -A arr 
arr["name"] = "biggie"
arr["id"]="1234"
for i in "${!arr[@]}"
do
    echo $i: "${arr[$i]}"
done

for i in $(ls)
do
    echo "Found a file: $i"
done

# Case statement
# Checks an input against a set of predefined vales
# Runs code when an input matches a condition
# The test condition comes before a right parenthesis to indicate the end of the test
# Need to wrap a condition that has spaces in quotes
animal="dog"
case $animal in
  bird) echo "Avian";; # ;; indicates "done with this contiion". You can still add more condtions
  dog|puppy) echo "Canine";; 
  *) echo "No match!";; # can use wildcards
esac

# Functions
# Allow us to repeatedly call a piece of code 
# Older ver: function fname { ... }
# Often placed at the top of the script

greet() {
    echo "Hello!"
}

echo "And now, a greeting!"
greet

greet() {
    echo "Hello $1!"
}
echo "And now, a greeting!"
greet biggie

greet() {
    echo "Hello $1! What a nice $2"
}
echo "And now, a greeting!"
greet biggie morning
greet everybody day

numberthings() {
    i=1
    for f in "$@"; do
        echo $i: "$f"
        ((i++))
    done
    echo "This counting was brought to you by the function $FUNCNAME!"  
}
numberthings # calls the function

var1="I'm variable 1"

myfunction() {
    var2="I'm variable 2"
    local var3="I'm variable 3"
}
myfunction
echo $var1
echo $var2
echo $var3 # won't be printed since's it's local to the function

# Input reditrection
# > output
# >> append

for i in 1 2 3 4 5
do  
    echo "This is line $i" > textfile.txt
done

for i in 1 2 3 4 5
do  
    echo "This is line $i" >> textfile.txt
done

# read keyword
# reads through text 
while read f
    do echo "I read a libe and it says: $f"
done < textfile.txt

# Arguments
# Allow us to pass information into a script from the CLI
# Are text that represent a string, a filename, and so on
# Are represented by numbered variables ($1, $2, and so on)
# Assigned in the order they're provided
# An argument with spaces needs quotes

echo "The $0 script got the argument: $1"
echo "Argument 2 is: $2"

for i in "$@"
do
    echo $1
done

echo "There were $# arguments."

# Options
# Allow us to pass info into a script from the CLI
# Are a combo of a dash and a letter (like -u or -p)
# Are accessed using the getopts keyword
# Can accept arguments of their own
# Can be specified and used in any order
# Flexible order = more user-friendly 

while getopts u:p: option; do
    case $option in
        u) user=$OPTARG;;
        p) pass=$OPTARG;;
    esac
done

echo "user: $user / pass: $pass"

while getopts u:p: option; do
    case $option in
        u) user=$OPTARG;;
        p) pass=$OPTARG;;
        a) echo "got the 'a' flag";;
        b) echo "got the 'b' flag";;
        ?) echo "I don't know what $OPTARG is!"
    esac
done

echo "user: $user / pass: $pass"

# Read 
# Scripts often nees input
# The read keyword allows us to gather input, pausing the script until input is provided
# This is the same read command that was used earlier to read a text file. 
# It can read from the CLI too

echo "What's your name?"
read name

echo "What's your password?"
read -s pass # -s won't show the text the user inputs

read -p "What's your favorite animal?" animal

echo name: $name, pass: $pass, animal: $animal

# Select
# Users can choose form a list of options
select animal in "bird" "dog" "fish"
do 
    case $animal in
       bird) echo "Birds like to fly!";;
       dog) echo "Dogs like to play catch.";;
       fish) echo "Fish like to swim.";;
       quit) break;;
       *) echo "Not sure what that is!"
    esac
done
# Typing the number of the option will equate to that option
# For ex, you can type 1 or "bird." It will run the same.

# suggest a response to the user
read -ep "Favorite color? " -i "Blue" favcolor
echo "$favcolor"

# if the user doesn't specified the required number of args
if (($#<3)); then 
    echo "This command takes three arguments:"
    echo "username, userid, and favorite number":
else 
    echo "username: $1"
    echo "userid: $2"
    echo "favorite number: $3"
fi

# if the user supplies an empty string
read -p "Favorite animal? " fav
while [[ -z $fav ]]
do
    read -p "I need an answer! " fav
done
echo "$fav was selected."

# Assumes the default answer if the user just presses enter
read -p "Favorite animal? [dog] " fav # Square brackets indicate default value
if [[ -z $fav ]]; then
    fav="cat"
fi
echo "$fav was selected."

# Can do basic validation of input
# Reject an answet that doesn't match a particular condition
read -p "What year? [nnnn] " year
until [[ $year =~ [0-9] {4} ]]; do
    read -p "A four-digit year, please! [nnnn] " year
done
echo "Selected year: $year"

# troubleshooting strategies:
# read the errors carefully
# observe line numbers in errors  
# check quotes and escaping
# check spacing in tests
# check closure of expansions and substitutions
# variables are case-sensitive
# use set -x to display commands as they run
# add echo statements to keep track of program flow
# use true and false built-ins to troubleshoot logic
# break down complex scripts into smaller parts to find problems

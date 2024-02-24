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



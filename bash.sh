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


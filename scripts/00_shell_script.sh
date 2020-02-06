#!/bin/bash

# PRINTING THINGS
# See the difference between echo and printf, by default echo does
# end with a new line and printf no. You can also format the string just like
# in C.
name=Naomi
echo Hello $name
printf "%s: Hi!\n" $name

# Colors
# To use colors in texts that are printed on the terminal
# use:
# echo -e "[1;<number>m <here your text> \e[0m"
# the number, for text colors are on the interval 30-37
# and to the background on the interval 40-47
echo "Printing a colored text, to so so use the"

echo -e "\e[1;31m This is red text \e[0m"
echo -e "\e[1;32m This is green \e[0m"
echo -e "\e[1;33m This is yellow \e[0m"
echo -e "\e[1;34m This is blue \e[0m"
echo -e "\e[1;35m This is magenta \e[m"
echo -e "\e[1;36m This is cyan \e[m"
echo -e "\e[1;37m This is white \e[m"

echo "Printing a colored background"
echo -e "\e[1;40m This a black background \e[0m"

# VARIABLES
#get the PID of a running program
#pgrep <program_name>
PID=`pgrep firefox`
# The | is used when we want to use the output of a command as the input to
# the following.
# tr is used to make substitutions, in this case the \0 to \n
#cat /proc/$PID/environ | tr '\0' '\n'

# FINDING THE LENGTH OF A STRING
lenght=${#name}
echo "The lenght of the variable Name is: %d", $lenght

# CHECKING FOR SUPERUSER
if [ $UID -ne 0 ]; then
    echo "Non root user"
else
    echo "Root user"
fi

# DOING MATH
## Using let
var=1
let var++
echo $var

## Alternatively
var=1
var=$[var +1]
var=1
echo $var
var=$(( var++ ))
echo $var

# Working with float point numbers
echo "4 * 0.56" | bc

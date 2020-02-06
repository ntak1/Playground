#!bin/bash

# BASE CONVERTER
printf "number: "
read number
echo Converting $number \(dec\)
printf "The number in bynary: "
echo "obase=2;$number" | bc

printf "The number in octal: "
echo "obase=8;$number" | bc

printf "The number in hex: "
echo "obase=16;$number" | bc
 




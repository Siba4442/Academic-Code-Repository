echo "Enter two number to swap them"
echo "First number : "
read num1
echo "Secound number : "
read num2

num1=$(( num1 + num2 ))
num2=$(( num1 - num2 ))
num1=$(( num1 - num2 ))

echo "Now the first number is $num1"
echo "Now the secound number is $num2"


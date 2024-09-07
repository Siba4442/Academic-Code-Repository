echo "Enter two number"
echo "First number"
read num1
echo "Secound number"
read num2


sum=$((num1 + num2))
diff=$((num1 - num2))
prod=$((num1 * num2))


if [ $num2 -ne 0 ]; then
  quot=$((num1 / num2))
  mod=$((num1 % num2))
else
  quot="undefined (division by zero)"
  mod="undefined (modulus by zero)"
fi

echo "Sum: $sum"
echo "Difference: $diff"
echo "Product: $prod"
echo "Quotient: $quot"
echo "Modulus: $mod"

if [ $num1 -eq $num2 ]; then
  echo "The numbers are equal."
else
  echo "The numbers are not equal."
fi

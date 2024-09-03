echo "Enter Celcius to find its corrsponding Fahrenheit"
read num

num2=$(echo "scale=2; (9/5) * $num + 32" | bc)
echo "$num Celsius is equal to $num2 Fahrenheit."

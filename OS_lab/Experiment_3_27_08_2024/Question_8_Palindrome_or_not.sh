echo "Enter a number to check if its palindrome or not"
read num

if ! [[ "$num" =~ ^[0-9]+$ ]]; then
	echo "Please enter a positive number"
	exit 1
fi

temp=$num
rem=0
rev=0

while [ $temp -gt 0 ]; do
	rem=$(( temp%10 ))
	rev=$(( rev*10+rem ))
	temp=$(( temp/10 ))
done

if [ "$num" -eq "$rev" ]; then
	echo "The entered number $num is a palindrome"
else
	echo "The entered number $num is not a palindrome"
fi

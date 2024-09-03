echo "Enter a year to find if its a leap year or not"
read year

if ! [[ "$year" =~ ^[0-9]+$ ]]; then
	echo "Enter a vaild Year"
	exit 1
fi

if (( (year%4 == 0 && year%100 != 0) || (year%400 == 0) )); then
	echo "The entered year $year is a Leap Year"
else
	echo "The entered year $year is not a Leap Year"
fi

 	

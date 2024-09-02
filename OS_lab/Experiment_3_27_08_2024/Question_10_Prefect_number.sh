echo "Enter a number to find if it's Prefect number or not"
read num

if ! [[ "$num" =~ ^[0-9]+$ ]] || [ "$num" -lt 0 ]; then
	echo "Please enter a Positive number"
	exit 1
fi

perfect_number() {
	local n=$1
	local sum=0
	for (( i=1; i<=$((num/2)); i++ )); do
		if [ $(( n%i )) -eq 0 ]; then
			sum=$(( sum+i ))
		fi
	done
	echo $sum
}

sum=$(perfect_number $num)

if [ "$num" -eq "$sum" ]; then
	echo "The entered number $num is a Prefect number"
else
	echo "The Entered number $num is not a Prefect number"
fi
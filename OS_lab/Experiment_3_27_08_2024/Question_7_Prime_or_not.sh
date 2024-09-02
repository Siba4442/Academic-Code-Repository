echo Enter a number to check if its prime or not
read num 
if [ $num -lt 2 ]; then
	echo "$num is not a prime number"
	exit 1
fi

prime_flag=1
for (( i=2; i*i<=num; i++ )); do
	if (( num % i == 0 )); then
		prime_flag=0
		break
	fi
done

if [ $prime_flag -eq 1 ]; then
	echo "$num is a prime number"
else
	echo "$num is not a prime number"

fi	

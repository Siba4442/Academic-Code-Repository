echo "Enter a number to reverse it"
read num
rev=0
lenght=${#num}
while [ $num -gt 0 ]
do
	rem=$((num%10))
	rev=$((rev*10+rem))
	num=$((num/10))
done
echo "The reverse of the entered number is $rev"

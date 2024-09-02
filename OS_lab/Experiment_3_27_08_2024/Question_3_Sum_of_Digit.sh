echo "Enter a number to find the sum of its digits"
read num
temp=$num
sum=0
while [ $num -gt 0 ]
do
	rem=$((num%10))
	sum=$((sum+rem))
	num=$((num/10))
done
echo "The sum of digits of the $temp is $sum"

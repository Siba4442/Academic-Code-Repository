echo "Enter a Number to check if its a Armstrong or not"
read num
length=${#num}
temp=$num
sum=0
while [ $num -gt 0 ]
do
	rem=$(($num%10))
	sum=$((sum+rem**$length))
	num=$((num/10))
done
if [ $sum -eq $temp ]
then
	echo "The entered number is Armstrong Number"
else
	echo "The Entered number is not an Armstrong Number"
fi

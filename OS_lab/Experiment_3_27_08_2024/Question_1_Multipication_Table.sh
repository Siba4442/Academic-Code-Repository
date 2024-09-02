echo "Enter the number to find the its Multipication Table"
read num
for (( i=0;i<10;i++ ))
do
	result=$((num*(i+1)))
	echo "$num X $i = $result"
done

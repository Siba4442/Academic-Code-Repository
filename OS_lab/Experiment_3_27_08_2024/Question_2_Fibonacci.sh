echo "Enter a number"
read num
a=0
b=1
echo "Fibonnaci Series"
for (( i=0;i<num;i++ ))
do
	echo $a
	fn=$((a+b))
	a=$b
	b=$fn
done

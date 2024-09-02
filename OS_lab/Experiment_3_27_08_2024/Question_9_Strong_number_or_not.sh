echo "Enter a number to check if its a strong number or not"
read num

if ! [[ "$num" =~ ^[0-9]+$ ]]; then
    echo "Please enter a positive number"
    exit 1
fi

factorial() {
    local n=$1
    local fact=1
    while [ $n -gt 1 ]; do
        fact=$(( fact*n ))
        n=$(( n-1 ))
    done
    echo $fact
}

temp=$num
sum=0

while [ $temp -gt 0 ]; do
    digits=$(( temp%10 ))
    digits_fact=$(factorial $digits)
    sum=$(( digits_fact+sum ))
    temp=$(( temp/10 ))
done

if [ "$num" -eq "$sum" ]; then
    echo "The Entered number $num is a Strong number"
else
    echo "The Entered number $num is not a Strong number"
fi

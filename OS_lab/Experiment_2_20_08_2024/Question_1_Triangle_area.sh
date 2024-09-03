echo "Enter the sides of the triangle to find its area"

echo "Enter the side a"
read a
echo "Enter the side b"
read b
echo "Enter the side c"
read c

if (( a + b > c && a + c > b && b + c > a )); then
    s=$(echo "scale=5; ($a + $b + $c) / 2" | bc)
    area=$(echo "scale=5; $s * ($s - $a) * ($s - $b) * ($s - $c)" | bc)
    area=$(echo "scale=5; sqrt($area)" | bc -l)
    
    echo "The area of the triangle is: $area"
else
    echo "The entered sides do not form a valid triangle"
fi
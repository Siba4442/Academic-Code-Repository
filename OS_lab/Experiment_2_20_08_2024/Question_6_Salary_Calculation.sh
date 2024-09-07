echo "Enter your Gross Salary : "
read sal

TA=$(echo "(0.5 * $sal) / 100" | bc)
DA=$(echo "(10 * $sal) / 100" | bc)
HRA=$(echo "(10.5 * $sal) / 100" | bc)
epf=$(echo "(12.5 * $sal) / 100" | bc)
esi=$(echo "(2.5 * $sal) / 100 " | bc)
total_all=$(echo "($TA + $DA + $HRA)" | bc)
total_deu=$(echo "$epf + $esi" | bc) 

echo "The Traveling Allowance on the Gross Salary is : $TA "
echo "The Dearness Allowance on the Gross Salary is : $DA"
echo "The House Rent Allowance on the Gross Salary is : $HRA"
echo "The Total Allowance on the Gross Salary : $total_all"

result=$(echo "$TA + $DA + $HRA" | bc)
dedu=$(echo "$epf + $esi" | bc) 
total=$(echo "($sal + $result) - $dedu" | bc)

echo " "
echo "The Employees' Provident Fund on the Gross Salary : $epf"
echo "The Employees' State Insurance on the Gross Salary : $esi"
echo "The total Dedution on the Gross Salary : $total_deu "
echo " "
echo "The Salary after adding the Allowance with the Gross Salary : $result"
echo " "
echo "The total Salary After adding the allowance and deduction :  $total"

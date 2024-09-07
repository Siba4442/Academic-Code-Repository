quick_sort() {
	local arr=("$@")

	if [ ${#arr[@]} -le 1 ]; then
		echo ${arr[@]}
		return
	fi

	local pivot=${arr[0]}
	local left=()
	local right=()

	for (( i=1; i<${#arr[@]}; i++ )); do
		if [ ${arr[i]} -lt $pivot ]; then
			left+=(${arr[i]})
		else
			right+=(${arr[i]})
		fi
	done

	echo "$(quick_sort "${left[@]}") $pivot $(quick_sort "${right[@]}")"

}
arr=(33 12 98 77 44 56 19)
sorted=$(quick_sort "${arr[@]}")

echo "Sorted array: $sorted"

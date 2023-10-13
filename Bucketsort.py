# Python3 program to sort an array
# using bucket sort


def insertionSort(b):
	for i in range(1, len(b)):
		up = b[i]
		j = i - 1
		while j >= 0 and b[j] > up:
			b[j + 1] = b[j]
			j -= 1
		b[j + 1] = up
	return b


def bucketSort(x):
	arr = []
	slot_num = 10 # 10 means 10 slots, each
	# slot's size is 0.1
	for i in range(slot_num):
		arr.append([])

	# Put array elements in different buckets
	for j in x:
		index_b = int(slot_num * j)
		arr[index_b].append(j)

	# Sort individual buckets
	for i in range(slot_num):
		arr[i] = insertionSort(arr[i])

	# concatenate the result
	k = 0
	for i in range(slot_num):
		for j in range(len(arr[i])):
			x[k] = arr[i][j]
			k += 1
	return x

<script>
// Javascript program to sort an array
// using bucket sort

// Function to sort arr[] of size n
// using bucket sort
function bucketSort(arr,n)
{
	if (n <= 0)
			return;

		// 1) Create n empty buckets	 
		let buckets = new Array(n);

		for (let i = 0; i < n; i++)
		{
			buckets[i] = [];
		}

		// 2) Put array elements in different buckets
		for (let i = 0; i < n; i++) {
			let idx = arr[i] * n;
			let flr = Math.floor(idx);
			buckets[flr].push(arr[i]);
		}

		// 3) Sort individual buckets
		for (let i = 0; i < n; i++) {
			buckets[i].sort(function(a,b){return a-b;});
		}

		// 4) Concatenate all buckets into arr[]
		let index = 0;
		for (let i = 0; i < n; i++) {
			for (let j = 0; j < buckets[i].length; j++) {
				arr[index++] = buckets[i][j];
			}
		}
}

// Driver code
let arr = [0.897, 0.565,
		0.656, 0.1234,
		0.665, 0.3434];
let n = arr.length;
bucketSort(arr, n);

document.write("Sorted array is <br>");
for (let el of arr.values()) {
	document.write(el + " ");
}

// This code is contributed by unknown2108
</script>

# Driver Code
x = [0.897, 0.565, 0.656,
	0.1234, 0.665, 0.3434]
print("Sorted Array is")
print(bucketSort(x))

# This code is contributed by
# Oneil Hsiao

size = int(input("enter the size"))
disk_size = int(input("enter the size of the disk"))


def CSCAN(arr, head):
	seek_count = 0
	distance = 0
	cur_track = 0
	left = []
	right = []
	seek_sequence = []
	left.append(0)
	right.append(disk_size - 1)
	for i in range(size):
		if (arr[i] < head):
			left.append(arr[i])
		if (arr[i] > head):
			right.append(arr[i])
	left.sort()
	right.sort()
	print(left)
	print(right)
	for i in range(len(right)):
		cur_track = right[i]
		seek_sequence.append(cur_track)
		distance = abs(cur_track - head)
		seek_count += distance
		head = cur_track
	head = 0
	seek_count += (disk_size - 1)
	for i in range(len(left)):
		cur_track = left[i]
		seek_sequence.append(cur_track)
		distance = abs(cur_track - head)
		seek_count += distance
		head = cur_track
	print("Total number of seek operations =",
		seek_count)
	print("Seek Sequence is")
	print(*seek_sequence, sep="\n")
print("enter the array of disks:")
arr = list(map(int,input().strip().split()))
head = int(input("enter the head position"))

print("Initial position of head:", head)

CSCAN(arr, head)



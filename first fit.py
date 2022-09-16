def FirstFit(block_Size, blocks, process_Size, proccesses):
    allocate = [-1] * proccesses
    occupied = [False] * blocks
    for i in range(proccesses):
        for j in range(blocks):
            if not occupied[j] and (block_Size[j] >= process_Size[i]):
                allocate[i] = j
                occupied[j] = True
                break
    print("Process No. Process Size Block No.")
    for i in range(proccesses):
        print(str(i + 1) + "\t\t\t" + str(process_Size[i]) + "\t\t\t", end=" ")
        if allocate[i] != -1:
            print(allocate[i] + 1)
        else:
            print("Not Allocated")
block_Size = [100, 50, 30, 120, 35]
process_Size = [20, 60, 70, 40]
m = len(block_Size)
n = len(process_Size)

FirstFit(block_Size, m, process_Size, n)

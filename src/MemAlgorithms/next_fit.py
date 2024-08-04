def nextFit(arr, memory_blocks):
    allocation = [-1] * len(arr)
    j = 0
    for i in range(len(arr)):
        if arr[i] == 0:
            continue
        
        while j < len(memory_blocks):
            if memory_blocks[j] >= arr[i]:
                allocation[i] = j
                memory_blocks[j] -= arr[i]
                break
        j = (j + 1) % len(memory_blocks)
    return allocation 

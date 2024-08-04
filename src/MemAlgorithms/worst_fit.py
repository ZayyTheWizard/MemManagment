def worstFit(arr, memory_blocks):
  allocation = [-1] * len(arr)
  for i in range(len(arr)):
      worst_idx = -1
      for j in range(len(memory_blocks)):
          if memory_blocks[j] >= arr[i]:
             if worst_idx == -1 or memory_blocks[worst_idx] < memory_blocks[j]:
                 worst_idx = j
      if worst_idx != -1:
          allocation[i] = worst_idx
          memory_blocks[worst_idx] -= arr[i]
   return allocation

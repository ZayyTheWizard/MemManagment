def firstFit(arr, memBlock):
  dic = {}
  space = 2000

  for a in arr:
    if a == 0:
      continue

    if space <= 0:
      break

    for lo, b in enumerate(memBlock):
      if b <= a and lo not in dic and space > 0:
        dic[lo] = 1 
        space -= 1
        break
  

  if space <= 0:
    return 0
  else:
    return 1
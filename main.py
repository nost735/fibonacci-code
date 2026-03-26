def fibonacci(num): 
  if num ==0: 
  return 0 
  elif num <3: 
  return 1 i=0 
  lis =[1,1] 
  while True: 
    if len(lis)>=3: 
      lis.pop(0) 
    lis.append(lis[0]+lis[1]) 
    i+=1 if i > num-3:break 
  return lis[2]
fibonacci(input())

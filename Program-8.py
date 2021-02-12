numbers=[]
# iterating till the range 
for i in range(1, 21): 
    numbers.append(i)
    
squares = map(lambda x:x*x,numbers)
print(list(squares))

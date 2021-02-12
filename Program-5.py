from bisect import bisect_left 

def BinarySearch(a, x): 
	i = bisect_left(a, x) 
	if i != len(a) and a[i] == x: 
		return i 
	else: 
		return -1

a = [] 
# number of elemetns as input 
n = int(input("Enter number of elements : ")) 
print("Enter the elements in sorted order :") 
# iterating till the range 
for i in range(0, n): 
    elem = int(input()) 
  
    a.append(elem) # adding the element 
 
x = int(input("Enter No to be searched : ")) 
res = BinarySearch(a, x) 
if res == -1: 
	print(x, "is not present") 
else: 
	print("First occurrence of a number", x, "is present at index position", res) 

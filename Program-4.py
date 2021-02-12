import pprint 

def My_3D(a, b, c): 
	lst = [[ ['#' for col in range(a)] for col in range(b)] for row in range(c)] 
	return lst 
	
# Driver Code 
col1 = 3
col2 = 5
row = 8
pprint.pprint(My_3D(col1, col2, row)) 

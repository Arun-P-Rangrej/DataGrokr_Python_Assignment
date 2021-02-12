my_input_list = [12,24,35,24,88,120,155,88,120,155]
print ("The original list is : " +  str(my_input_list)) 


def arun(seq):
    seen = set()
    seen_add = seen.add
    return [x for x in seq if not (x in seen or seen_add(x))]

print("After removing duplicated using set : " + str(arun(my_input_list)))

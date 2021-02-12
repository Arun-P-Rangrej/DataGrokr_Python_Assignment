def MyGenerator(n):
    i=0
    for i in range(n+1):
        if i%5==0 and i%7==0:
            yield i

print("Enter the ending no")
n=int(input())
values = []
for i in MyGenerator(n):
    values.append(str(i))

print(",".join(values))

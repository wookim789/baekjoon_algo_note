a = 5 
b = 6

print("a:", str(a), " b:", str(b))
print("swap")

a, b = b, a 

print("a:", str(a), " b:", str(b))


a = [1,2,3]
b = [4,5,6]

print("a:", a, "b", b)
print("swap")

a[0], b[0] = b[0], a[0]

print("a:", a, "b", b)
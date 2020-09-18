s = input()

arr = [ 'dz=','c=','s=','z=','c-','d-','lj','nj']
for i in arr:
    while i in s:
        s = s.replace(i,' ',1)
print(len(s))

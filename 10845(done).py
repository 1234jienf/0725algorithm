import sys
n = int(sys.stdin.readline())
result=[]

#1.push X
for i in range (n):
    order = sys.stdin.readline().strip('\n')
    if 'push' in order:
        a,b = order.split(' ')
        result.append(b)

#2. pop
    elif 'pop' == order:
        if result != []:
            print(result.pop(0))
        else:
            print(-1)

#3. size
    elif 'size' == order :
        print(len(result))

#4. empty
    elif 'empty' == order : 
        if len(result) == 0:
            print(1)
        else :
            print(0)

#5. front
    elif 'front' == order :
        if len(result) == 0:
            print(-1)
        else : 
            print(result[0])

#6. back
    elif 'back' == order :
        if len(result) == 0:
            print(-1)
        else : 
            print(result[-1])

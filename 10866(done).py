import sys
n = int(sys.stdin.readline())
result=[]

#1.push_front X
for i in range (n):
    order = sys.stdin.readline().strip('\n')
    if 'push_front' in order:
        a,b = order.split(' ')
        result.insert(0,b)

    #2. push_back X 
    elif 'push_back' in order:
        a,b = order.split(' ')
        result.append(b)

    #3. pop_front
    elif 'pop_front' == order:
        if result != []:
            print(result.pop(0))
        else:
            print(-1)

    #4. pop_back
    elif 'pop_back' == order:
        if result != []:
            print(result.pop())
        else:
            print(-1)

    #5. size
    elif 'size' == order :
        print(len(result))

    #6. empty
    elif 'empty' == order : 
        if len(result) == 0:
            print(1)
        else :
            print(0)

    #7. front
    elif 'front' == order :
        if len(result) == 0:
            print(-1)
        else : 
            print(result[0])

    #8. back
    elif 'back' == order :
        if len(result) == 0:
            print(-1)
        else : 
            print(result[-1])

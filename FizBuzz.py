for x in range(1,101):
    if x % 3 == 0:
        print('Fiz',end ="")
    if x % 5 == 0:
        print('Buzz',end ="")
    elif x % 3 != 0:
        print(x,end ="")
    print()

def evenodd(num):
    if num % 2:
        print(str(num) + " is odd")
    else:
        print(str(num) + " is even")
        if num % 4 == 0:
            print(str(num) + " is multiplication of 4")


number = int(input("Give me number: "))
check = int(input("Give me divider: "))

if number % check:
    print(str(number) + " not divided evenly")
    evenodd(number)
else:
    print(str(number) + " divide evenly")
    evenodd(number)

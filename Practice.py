#numbers = [4,12,-3,6,7,80]

#for i in range(len(numbers)):
#    print (i,numbers[i],"hi")
#
#for i in numbers:
#    print(i)


#blah = [1, 7, 19, 22, 24, 8]

#for i in range(len(blah)):
#    print(f"{i} squared is {blah[i]**2}")
numbers = [14,2,3,45,5]

def is_odd(numero):
    odd = True

    if numero % 2 == 0:
        odd = False
    else:
        odd = True

    return odd

for num in numbers:
    if is_odd(num):
        print(f"{num} is odd")
    else:
        print(f"{num} is even")
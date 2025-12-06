def convert2decimal(x):
    size = len(x)
    p2 = 1
    num = 0
    for i in range(size-1, -1, -1):
        if(x[i] == '1'):
            num += p2
        p2 *= 2   # Adding 2s with the 2^pos
    return num

#TC = O(len)  #length of string x
#SC = O(1) 

def convert2binary(x1):
    res = "" #or str()
    while(x1 > 0): #we will divide till 1
        if(x1 % 2 == 1): res += '1'  ## Add '1' as a string
        else: res += '0'  # Add '0' as a string
        x1 //= 2
    # Convert the reversed iterator back to a string
    return ''.join(reversed(res)) 

#TC = O(log2 n)
#SC = O(log2 n)  # = to number of steps taken which is log2 n

#Recursive solution
#def convert2binary1(num):
#    if num >= 1:
#        convert2binary1(num // 2)
    #return num % 2

x = input("Enter binary num: ")
print(convert2decimal(x))

x1 = int(input("Enter decimal num: "))
print(convert2binary(x1))
#print(convert2binary1(x1))

# Quick Ninja One line Code
#print(bin(4)[2:]) #4 as input
#decNum = 4
#print(bin(decNum)[2:])

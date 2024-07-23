def main():
    value=99
    print('The value is:',value)
    change_me(value)
    print('Back in main the value is',value)

def change_me(arg):
    print('I am changing the value')
    arg=0
    print('Now the value is',arg)

main()

print('-----------------')
def foo(c,d,e=10):  #e'ye key word argüman denir.Yani atamalı argüman.

    print(c,d)
    print(e)
foo(1,2)
print('--------------------')

def globaldenemesi():
    global x  #Bunu silersen aşağıdaki print error verir.
    x=5

globaldenemesi()

print('Global x=',x)

x=7
print(x)

print('-------------------------')
def factorial(num):    #Recursive örneği
    if num==0:
        return 1
    else:
        return num*factorial(num-1)

print(factorial(num=int(input('Hangi sayinin faktoriyelini istersin::'))))

def fibonacci(n): #Recursive ile fibonacci
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)

print(fibonacci(n=int(input('Hangi sayinin fibonaccisini istersin::'))))

def gcd(a,b):   #gcd=greatest common divisor #Recursive ile EBOB
    if a%b==0:
        return b
    else:
        return gcd(a,a%b)

print(gcd(a=int(input('EBOB u bulunacak sayilardan ilki::')),b=int(input('Ikincisi::'))))

#Hannoi eksik!!
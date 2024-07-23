x=20
def main():
    global x
    x=5
    x+=5
main()
def second():
    #global x
    #x+=20  #Bunu çalıştıracaksan üsttekine ihtiyacın var.
    y=2*x
    print('y=',y)
second()
print('x=',x)
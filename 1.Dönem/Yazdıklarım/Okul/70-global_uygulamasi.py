

def main():
    value=99
    print('The value is', value)
    change_me(value)
    print('Back in main the value is',value)        #Yani global'ı sanki fonksiyonları tanımlamadan önce yazılmış gibi mi
                                                    #düşünmeliyim?

def change_me(arg):
    print('I am changing the value.')
    arg = 0
    print('Now the value is', arg)
    global value
    value=444





main()

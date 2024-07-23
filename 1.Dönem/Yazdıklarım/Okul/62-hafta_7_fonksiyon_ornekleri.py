def celcius_to_fahrenheit(celcius_float):
    '''Convert Celcius to Fahrenheit'''
    return celcius_float*1.8+32

print(celcius_to_fahrenheit(24))

def length(a_str):
    '''Return the length of a_str-Kelimedeki harfleri sayar'''
    count=0
    for char in a_str:
        count+=1
    return count

print(length('invisible'))

x=55
def void_denemesi(x):
    '''Void fonksiyon içteki değeri değiştirir mi?)'''
    x+=5
    print(x)

print(void_denemesi(x))
print(x,'HAYIR')
def kolay_tuple_ornek1():
    '''Tuple oluşturmak için () gerekmez.'''
    tuple1=1,2,3
    print(tuple1)

def list_comprehension_ornek2():
    '''Tekrarlamalı liste oluşturmanın kolay yolu.'''
    list1=[n for n in range(5)]
    print(list1)
    list2=[n**2 for n in range(6)]  #Yalnızca ilk n ile değişiklik yapılabilir.
    print(list2)
    list3=[x+y for x in range(1,4) for y in range(1,4)]     #İkili for ile yapılan bu işlemi
    print(list3)                                        #baya kolaylaştırıyor.
    list4=[c for c in 'Hi There Mom' if c.isupper()]    #Hatta if bile koyulabiliyor.
    print(list4)                                        #c.isupper büyük harf metodu.

def dictionaryde_for_un_farki_ornek3():
    dict1={'ali':3,'ayse':5}    #'=' değil ':' kullanılır.
    for eleman in dict1:
        print(eleman)   #Value'yi değil key'leri printler.

def dictionary_de_update_metodu_ornek4():
    '''Eşleşen key'lerin value'lerini günceller.'''
    dict1={'ali':5,'hasan':7,'ayse':3}
    dict2={'ali':999,'hasan':3333,'mehmet':'Adam'}
    dict1.update(dict2)     #Key yoksa ilave eder.
    print(dict1)



def dictionary_de_pop_metodu_ornek5():
    '''Eşleştirmeyi siler,value'yi döndürür.'''
    dict1={'ali':3,'hasan':5}
    returned=dict1.pop('ali')
    print(returned)
    print(dict1)



def dictionary_i_for_ile_goruntuleme_ornek6():
    my_dict={'ali':5,'veli':3,'ayse':22}
    for key in my_dict: #Key'ler için
        print(key)
    for key,value in my_dict.items():   #Pair'ler için
        print(key,value)
    for value in my_dict.values():  #Value'ler için.
        print(value)

def iki_boyutlu_liste_ornek7():
    list1=[[0,1,2,3],[99,100,101]]
    print(list1[1][1])

def items_metodu_ornek8():
    dict1={'ali':99,'ayse':22}
    print(dict1.items())

items_metodu_ornek8()


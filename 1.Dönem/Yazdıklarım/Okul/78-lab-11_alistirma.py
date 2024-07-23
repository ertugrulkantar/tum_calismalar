#Belirsiz sayıda kişiden,taraftarı olduğu takımın kısa adını(Büyük harflerle)alan ve girilen takımın kısa adlarını ve
#taraftar sayılarını alıp ekrana yazdıran program.
def yol1():
    '''if-else ile'''
    takim_taraftar_say={}
    devam='e'

    while devam=='e':
        takim=input('Taraftari oldugunuz takimin kisa adini giriniz::')

        if takim in takim_taraftar_say:
            takim_taraftar_say[takim]+=1
        else:
            takim_taraftar_say[takim]=1

        devam=input('Devam icin e tuslayınız')

    for takim in takim_taraftar_say:
        print(takim,takim_taraftar_say[takim])

def yol2():
    '''try-except ile'''
    takim_taraftar_say = {}
    devam = 'e'

    while devam == 'e':
        takim = input('Taraftari oldugunuz takimin kisa adini giriniz::')

        try:
            takim_taraftar_say[takim] += 1
        except KeyError:
            takim_taraftar_say[takim] = 1

        devam = input('Devam icin e tuslayınız')

    for takim in takim_taraftar_say:
        print(takim, takim_taraftar_say[takim])

def yol3():
    '''get ile'''
    takim_taraftar_say = {}
    devam = 'e'

    while devam == 'e':
        takim = input('Taraftari oldugunuz takimin kisa adini giriniz::')

        takim_taraftar_say[takim] = takim_taraftar_say.get(takim, 0) + 1

        devam = input('Devam icin e tuslayınız')

    # for takim in takim_taraftar_say:
    # print(takim, takim_taraftar_say[takim])

    # alternatif
    for takim, taraf_say in takim_taraftar_say.items():
        print(takim, taraf_say)

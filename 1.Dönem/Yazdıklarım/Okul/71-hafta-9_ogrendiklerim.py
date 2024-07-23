temp_file=open('tempfile.txt','w')      #tempfile'ı oluşturuyoruz.
line1=temp_file.write('First line\n')   #ve içeriğini yazıyoruz.
line2=temp_file.write('Second line\n')
lime3=temp_file.write('Third line\n',)
line4=temp_file.write('Forth Line')
temp_file=open('tempfile.txt','r')
#--1--
#file=temp_file.readlines()
#print('1',file)
#print('-------1----------')

#--2--
#file2=temp_file.readline()
#print('2',file2)
#print('--------2---------')

#--3--
#file3=temp_file.read()
#print(file3)
#print('------3---------')

#--4--
#for line_str in temp_file:      #ekstra kendisi de boşluk bırakıyor.
    #print(line_str)
#print('-----4------')

#--5--
#print(temp_file.read(1))        #Harf harf okuma
#print(temp_file.read(2))
#print(temp_file.read(2))
#print(temp_file.read())

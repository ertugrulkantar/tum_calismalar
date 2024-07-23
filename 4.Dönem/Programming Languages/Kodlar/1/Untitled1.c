#include <stdio.h> //Asagida verdigimiz input output komutlarinin calismasini saglar.
#include <stdlib.h>

int main(int argc,char *argv[]){
    printf("hello c\n");

    ///1///
    printf("Merhaba\a\n Ses Geldi Mi?"); //Sesi guzelmis :D

    ///2///
    //Iceriye tirnak mi koymak istiyorsun?
    printf("Merhaba\"\n");  //Diger turlu hata veriyor. \" seklinde koyabiliyorsun.


    ///3///  //(input alma ve ekrana degisken yazdirma)
    int sayi;
    printf("Sayi gir::");
    scanf("%d",&sayi);  //Sayi okuma. & ifadesi o degiskenin adresini temsiller.
    printf("Girilen sayi %d dir\n",sayi);

    ///4///  // 3 e basit bir ornek
    int birinciSayi,ikinciSayi,ucuncuSayi,toplam;
    printf("Birinci sayiyi giriniz::");
    scanf("%d",&birinciSayi);

    printf("\nIkinci sayiyi giriniz::");
    scanf("%d",&ikinciSayi);

    printf("\nUcuncu sayiyi giriniz::");
    scanf("%d",&ucuncuSayi);

    toplam=birinciSayi+ikinciSayi+ucuncuSayi;
    printf("%d + %d + %d = %d dir",birinciSayi,ikinciSayi,ucuncuSayi,toplam);
    return 0;
}

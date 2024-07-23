#include <stdio.h>
#include <stdlib.h>
#include <time.h> //Random sayi uretirken gerekli

int main()
{   /*Dizi olusturma*/
    int dizi[5], dizi1[5]; //Ayni anda birden cok tanimlayabilirsin.
    dizi[0]=5;
    printf("1---------\n");
    printf("%d",dizi[0]);
    ////////////////////

    /*Dizinin tum elemanlarina ayni degeri atama*/
    printf("\n\n2---------\n");
    int dizi2[6]={0};

    for(int i=0;i<5;i++){
        printf("%d",dizi2[i]);
    }
    ////////////////////////////

    /*Dizi elemanlarini toplu atama*/
    printf("\n\n3---------\n");

    int dizi3[5]={0,1,2,3,4};  //Boyutunu vermesen de calisir.

    for(int i=0;i<5;i++){
        printf("%d",dizi3[i]);
    }
    ///////////////////////////////

    /*Hizalama*/

    printf("\n\n4---------\n");
    printf("\n%s%13s\n","Element","Value");  //13s ile t ile e arasini 13 birim acar.

    for(int i=0;i<5;i++){
        printf("%7d%13d\n",i,dizi3[i]);
    }
    ///////////////////////////////////

    /*String detay*/  //Tek tirnak char iki tirnak str belirtir.

    printf("\n\n5---------\n");

    char s33[]="";
    scanf("%s",&s33);
    printf("%s",s33);
    /////////////////////////////////

    /*Dizi icindeki elemanlardan kacar tane oldugunu bulan ve histogramini cizen kod*/

    printf("\n\n6---------\n\n");

    int frequency[11]={0};
    int res[40]={1,2,6,4,8,5,9,7,8,10,1,6,3,8,6,10,3,8,2,7,6,5,7,6,8,6,7,5,6,6,5,6,7,5,6,4,8,6,8,10};

    for(int i=0;i<40;i++){
        frequency[res[i]]+=1;
    }
    for(int i=1;i<11;i++){
        printf("%d frekansi %d\t",i,frequency[i]);
        for(int j=0;j<frequency[i];j++){
            printf("*");
        }
        printf("\n");
    }
    //////////////////////////////////////

    /*Bir zari 6000 defa atip hangi rakamdan kac tane geldigini bulalim*/
    printf("\n\n7---------\n\n");

     int face,roll;
     int freq[7]={0};
     srand(time(NULL)); //Farkli sayilar uretebilmek icin gerekli.

     for(roll=0;roll<6000;roll++){
        face=rand()%6 +1;
        freq[face]++;
     }
     printf("\n%s%17s\n","Face","Frequency");
     for(face=1;face<=6;face++){
        printf("%4d%17d\n",face,freq[face]);
     }
    ///////////////////////////////////

    /*String detay*/ //Stringler gorunmese de '\0' ifadesiyle biter
    printf("\n\n8---------\n\n");

    char string1[20];
    char string2[]="string literal";

    scanf("%s",&string1);
    printf("string1=%s\nstring2=%s\nstring1 harflere ayrilmis sekli=",string1,string2);

    for(int i=0;string1[i]!='\0';i++){
        printf("%c ",string1[i]);
    }
    //////////////////////////////


    return 0;
}

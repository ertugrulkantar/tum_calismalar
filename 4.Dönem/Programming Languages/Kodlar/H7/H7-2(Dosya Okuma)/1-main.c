#include <stdio.h>
#include <stdlib.h>

int main()
{
    int acc;
    char name[30];
    double balance;

    FILE*d;  //File nesnesi olusturma...

    if((d=fopen("a.ert","w"))==NULL){  //Dosyayi yazacagiz 0 dan
        printf("Dosya acilamadi!");
    }
    else{
        scanf("%d%s%lf",&acc,name,&balance);  //Hepsi icin ayri ayri enter vericez.

        while(!feof(stdin)){
            fprintf(d,"%d %s %.2f\n",acc,name,balance);  //toplu yazdirmaya yarar. tek tek icin dosya_yazma detaya bak.
            printf("?");
            scanf("%d%s%lf",&acc,name,&balance);
        }
    }

    return 0;
}

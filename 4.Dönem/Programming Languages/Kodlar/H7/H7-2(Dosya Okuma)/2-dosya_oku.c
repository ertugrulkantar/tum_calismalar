#include <stdio.h>
#include <stdlib.h>

int main(){

FILE *d;
int acc;
char name[30];
double balance;

if((d=fopen("a.ert","r"))==NULL){
    printf("dosya acilamadi");
}
else{
    fscanf(d,"%d%s%lf",&acc,name,&balance); //d yi okuyoruz.11
    while (!feof(d)){
        printf("%d\t%s\t%.2f\n",acc,name,balance);
        fscanf(d,"%d%s%lf",&acc,name,&balance);
    }
}

/*HOCANIN TERCIH ETTIGI YONTEM*/
printf("\n2---------------\n");

if((d=fopen("a.ert","r"))==NULL){
    printf("dosya acilamadi");
}
else{
    while (!feof(d)){
        char a=fgetc(d);
        printf("%c",a);

    }
    fclose(d);
}



return 0;
}

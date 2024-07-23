#include <stdio.h>
#include<ctype.h> //isspace, isalpha, tolower gibi fonksiyonlari iceren kutuphane...
main(){

FILE *d;

if((d=fopen("d.txt","w"))==NULL){
    printf("Dosya acilmadi");
}
else{
    char a[50];
    scanf("%s",a);
    fputc('a',d);
    fputs(a,d);
    fputs("  arif",d);
    fclose(d);  //Simdi dosyaya bak...
}


return 0;

}

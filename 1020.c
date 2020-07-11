#include <stdio.h>

int main(){

    int year,month,days,n;

    scanf("%d",&n);
    printf("%d ano(s)\n",n/365);
    month = n%365;
    printf("%d mes(es)\n",month/30);
    days = month%30;
    printf("%d dia(s)\n",days/1);




    return 0;
}
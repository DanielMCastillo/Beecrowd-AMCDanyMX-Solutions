#include <stdio.h>

#define i 12
int main(){
    float st, sdt,r;

    scanf("%f",&st);
    scanf("%f",&sdt);

    r = st*sdt/i;

    printf("%.3f\n",r);


    return 0;
}
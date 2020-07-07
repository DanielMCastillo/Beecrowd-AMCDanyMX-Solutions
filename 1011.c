//Volume Formula
//(4/3)*pi*R***3
#include <stdio.h>
#include <math.h>

int main(){
    double r,volume,pi=3.14159;
   

    scanf("%lf", &r);

    volume = (((4/3.0)*pi)*(pow(r,3)));

    printf("VOLUME = %.3lf\n",volume);



    return 0;
}
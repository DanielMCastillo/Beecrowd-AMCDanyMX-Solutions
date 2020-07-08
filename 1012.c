#include <stdio.h>
#include <math.h>
#define pi 3.14159
int main(){

    double A,B,C, square, rectangule, circle, triangle_rectangule,trapezium;

    scanf("%lf", &A);
    scanf("%lf", &B);
    scanf("%lf", &C);


    triangle_rectangule = ((A*C)/2.0);
    circle = (pi*(pow(C,2)));
    trapezium = (((A+B)*C)/2);
    square = pow(B,2);
    rectangule = (A*B);


    printf("TRIANGULO: %.3lf\n",triangle_rectangule);
    printf("CIRCULO: %.3lf\n", circle);
    printf("TRAPEZIO: %.3lf\n",trapezium);
    printf("QUADRADO: %.3lf\n", square);
    printf("RETANGULO: %.3lf\n",rectangule);


    return 0;
}
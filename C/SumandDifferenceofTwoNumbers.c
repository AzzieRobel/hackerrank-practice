#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main() {
    // Declare variables to store input values
    int a, b;
    float x, y;
    
    // Read two integers
    scanf("%d %d", &a, &b);
    
    // Read two floating point numbers
    scanf("%f %f", &x, &y);
    
    // Calculate and print sum and difference of integers
    printf("%d %d\n", a + b, a - b);
    
    // Calculate and print sum and difference of floats, rounded to 1 decimal place
    printf("%.1f %.1f\n", x + y, x - y);
    
    return 0;
}

#include <stdio.h>
#include <stdlib.h>  // For abs() function

void update(int *a, int *b) {
    // Store original values of a and b
    int original_a = *a;
    int original_b = *b;
    
    // Update the first value to the sum of a and b
    *a = original_a + original_b;
    
    // Update the second value to the absolute difference of original a and b
    *b = abs(original_a - original_b);
}

int main() {
    int a, b;
    int *pa = &a, *pb = &b;
    
    // Read input values for a and b
    scanf("%d %d", &a, &b);
    
    // Call update function to modify a and b
    update(pa, pb);
    
    // Print the modified values of a and b
    printf("%d\n%d", a, b);

    return 0;
}

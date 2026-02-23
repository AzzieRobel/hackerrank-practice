#include <stdio.h>

// Function to find the maximum of four integers
int max_of_four(int a, int b, int c, int d) {
    // Initialize the maximum with the first value
    int max = a;
    
    // Compare max with b, c, and d to find the greatest value
    if (b > max) max = b;
    if (c > max) max = c;
    if (d > max) max = d;
    
    return max;  // Return the greatest value
}

int main() {
    int a, b, c, d;
    
    // Read four integers from input
    scanf("%d %d %d %d", &a, &b, &c, &d);
    
    // Call max_of_four to get the greatest number
    int ans = max_of_four(a, b, c, d);
    
    // Print the result
    printf("%d", ans);
    
    return 0;
}

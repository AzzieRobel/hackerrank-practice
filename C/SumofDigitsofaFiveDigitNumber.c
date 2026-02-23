#include <stdio.h>

int main() {
    int n, sum = 0;
    scanf("%d", &n);

    // Loop through the digits and add them to the sum
    while (n > 0) {
        sum += n % 10;  // Get the last digit and add it to sum
        n /= 10;         // Remove the last digit
    }

    // Print the sum of the digits
    printf("%d\n", sum);

    return 0;
}

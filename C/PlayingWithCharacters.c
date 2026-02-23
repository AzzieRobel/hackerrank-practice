#include <stdio.h>
#include <string.h>
#include <stdlib.h>

#define MAX_LEN 100

int main() {
    char ch;            // For storing the character input
    char str[MAX_LEN];  // For storing the string input
    char sentence[MAX_LEN];  // For storing the sentence input

    // Read the single character input
    scanf("%c", &ch);
    // Consume the newline character left in the buffer after reading character
    getchar();

    // Read the string input (which does not contain spaces)
    scanf("%s", str);
    // Consume the newline character left in the buffer after reading string
    getchar();

    // Read the sentence input (which can contain spaces)
    scanf("%[^\n]%*c", sentence);

    // Print the character
    printf("%c\n", ch);

    // Print the string
    printf("%s\n", str);

    // Print the sentence
    printf("%s\n", sentence);

    return 0;
}
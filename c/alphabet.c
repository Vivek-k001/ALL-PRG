#include <stdio.h>
#include <ctype.h>

int main() {
    char word[100];
    printf("Enter a word: ");
    scanf("%s", word);

    printf("Alphabet positions: ");
    for(int i = 0; word[i] != '\0'; i++) {
        char ch = tolower(word[i]);
        if(ch >= 'a' && ch <= 'z') {
            printf("%d ", ch - 'a' + 1);
        } else {
            printf("? "); // For non-alphabet characters
        }
    }
    printf("\n");
    return 0;
}
#include <stdio.h>
#include <ctype.h>

int main() {
    char str[100];
    int i, count = 0;

    printf("Enter a string: ");
    fgets(str, sizeof(str), stdin);

    for(i = 0; str[i] != '\0'; i++) {
        char ch = tolower(str[i]);
        if(ch == 'a' || ch == 'e' || ch == 'i' || ch == 'o' || ch == 'u') {
            count++;
        }
    }

    printf("Number of vowels: %d\n", count);
    return 0;
}

.....
.....gyjkyj
hdrthtdhhrrthhtrjnhhtr
eg
erger
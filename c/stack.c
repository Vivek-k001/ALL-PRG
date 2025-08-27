#include <stdio.h>
#define MAX 100

int main() {
    int stack[MAX], top = -1, choice, value, n, i;

    printf("Enter the maximum size of the stack (up to %d): ", MAX);
    scanf("%d", &n);

    while(1) {
        printf("\n1. Push\n2. Pop\n3. Display\n4. Exit\nEnter your choice: ");
        scanf("%d", &choice);

        switch(choice) {
            case 1:
                if(top == n - 1) {
                    printf("Stack Overflow!\n");
                } else {
                    printf("Enter value to push: ");
                    scanf("%d", &value);
                    stack[++top] = value;
                }
                break;
            case 2:
                if(top == -1) {
                    printf("Stack Underflow!\n");
                } else {
                    printf("Popped value: %d\n", stack[top--]);
                }
                break;
            case 3:
                if(top == -1) {
                    printf("Stack is empty.\n");
                } else {
                    printf("Stack elements: ");
                    for(i = top; i >= 0; i--) {
                        printf("%d ", stack[i]);
                    }
                    printf("\n");
                }
                break;
            case 4:
                return 0;
            default:
                printf("Invalid choice!\n");
        }
    }
}
#include <stdio.h>
int guess;
void createandfill(){
    int array [100];
    for (int i = 0; i < 100; i++) {
        array[i] = i;
    }
}
void search(){
    printf("Put in a number from 0-100, and I'll tell you its index number in the array!\n");
    scanf("%d", &guess);
    for (int i = 0; i < 100; i++){
        if (guess==i){
            printf("\nYour input has the index value %d!\n", i);
        }
    }
}
int main(){
    createandfill();
    search();
}
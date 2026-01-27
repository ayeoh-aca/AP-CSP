#include <stdio.h>
void zeroten(){
    printf("0-10: ");
    for (int i=0; i<=10; i++){
        printf("%d ", i);
    }
}
void twotwenty(){
    printf("2-20: ");
    for (int i=2; i<=20; i++){
        printf("%d ",i);
    }
}
void evenfour(){
    printf("Evens 4-40: ");
    for(int i=2; i<=20; i++){
        printf ("%d ", (i*2));
    }
}
void oddsoneohone(){
    printf("Odds 101-303: ");
    for(int i=50;i<=151;i++){
        printf("%d ", (i*2)+1);
    }
}
void sevenmultiples(){
    printf("Multiples of Seven: ");
    for(int i=1;i<=10;i++){
        printf("%d ", i*7);
    }
}
int main(){
    printf("\n");
    zeroten();
    printf("\n\n");
    twotwenty();
    printf("\n\n");
    evenfour();
    printf("\n\n");
    oddsoneohone();
    printf("\n\n");
    sevenmultiples();
    printf("\n\n");
}
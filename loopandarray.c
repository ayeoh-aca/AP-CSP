#include <stdio.h>
void array85(){
    int array [85];
}
void matrix(){
    int matrix[20][20];
}
void populatearray(){
    for (int i=0;i<85;i++){
        int array[i];
    }
}
void populatematrix(){
    for (int i=0; i<20; i++){
        for (int j=0;j<20;j++){
            int matrix[i][j];
            printf("(%d,%d) ", i, j);
        }
    }
}
int main(){
    array85();
    matrix();
    populatearray();
    populatematrix();
}
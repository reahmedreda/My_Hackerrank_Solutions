// Link : https://www.hackerrank.com/challenges/grading/problem
// Name : Grading Students
// Level : Easy
// Max Score : 10

#include <math.h>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <assert.h>
#include <limits.h>
#include <stdbool.h>

int* solve(int grades_size, int* grades, int *result_size){
   int i=0,x[grades_size],temp=0;
    
   for(i=0;i<grades_size;i++){
    
       
       
       if((5-grades[i]%5+grades[i]-grades[i])<3 && grades[i]>=38 )
       {
           temp=5-(grades[i]%5)+grades[i];
           grades[i]=temp;
           
       }
       
       }
     
   return grades;
}

int main() {
    int n; 
    scanf("%d", &n);
    int *grades = malloc(sizeof(int) * n);
    for(int grades_i = 0; grades_i < n; grades_i++){
       scanf("%d",&grades[grades_i]);
    }
    int result_size;
    int* result = solve(n, grades, &result_size);
        
    int result_i = 0;
    for(result_i = 0; result_i < n; result_i++) {
        if(result_i) {
            printf("\n");
        }
        printf("%d", result[result_i]);
    }
    puts("");
    

    return 0;
}

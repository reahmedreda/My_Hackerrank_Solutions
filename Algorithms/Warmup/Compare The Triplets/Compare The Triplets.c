//Problem: https://www.hackerrank.com/challenges/compare-the-triplets

#include <math.h>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <assert.h>
#include <limits.h>
#include <stdbool.h>

int* solve(int a[],int b[],int res[]){
    res[0]=(((a[0]-b[0])>0)? 1:0)+ (((a[1]-b[1])>0)? 1:0) + (((a[2]-b[2])>0)? 1:0);
    res[1]=(((a[0]-b[0])>=0)? 0:1)+ (((a[1]-b[1])>=0)? 0:1) + (((a[2]-b[2])>=0)? 0:1);
    return res;
}

int main() {
    int a[3],b[3],res[2]; 
    scanf("%d %d %d", &a[0], &a[1], &a[2]);
    scanf("%d %d %d", &b[0], &b[1], &b[2]);
    int* result = solve(a,b,res);
    for(int result_i = 0; result_i <2; result_i++) {
        if(result_i) {printf(" ");}
        printf("%d", result[result_i]);
    }
    puts("");
    return 0;
}
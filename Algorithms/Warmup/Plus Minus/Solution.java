import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class Solution {

    static void plusMinus(int[] arr) {
        // Complete this function
        float p=0 , n=0 , z=0 ;
        for (float i :arr){
            if (i > 0)  p++ ;
            else if (i==0)  z++ ;
            else n++ ;
        } 
        System.out.println(p/arr.length);
        System.out.println(n/arr.length);
        System.out.println(z/arr.length);
    }

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int n = in.nextInt();
        int[] arr = new int[n];
        for(int arr_i = 0; arr_i < n; arr_i++){
            arr[arr_i] = in.nextInt();
        }
        plusMinus(arr);
        in.close();
    }
}
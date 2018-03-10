
// Link : https://www.hackerrank.com/challenges/variable-sized-arrays/problem
// Name : Variable Sized Arrays
// Level : Easy
// Max Score : 30

#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
    
    int n, q, size, value, which, index;
    cin >> n >> q;
    vector<vector<int>> Total;
    for (int i = 0; i < n; ++i) {
        cin >> size;
        vector<int> vec;
        for (int j = 0; j < size; ++j) {
            cin >> value;
            vec.push_back(value);
        }
        Total.push_back(vec);
    }
    for (int k = 0; k < q; ++k) {
        cin >> which >> index;
        cout << Total[which][index] << endl;
    }
    return 0;
}
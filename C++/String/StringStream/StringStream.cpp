// Link : https://www.hackerrank.com/challenges/c-tutorial-stringstream/problem
// Name : StringStream
// Level : Easy
// Max Score : 10

#include <sstream>
#include <vector>
#include <iostream>
using namespace std;

vector<int> parseInts(string str) {
    vector<int> integers;
    stringstream s(str);
    int temp;char x;
    while(s>>temp){
       integers.push_back(temp);
       s>>x;
    }
    return integers ;
}

int main() {
    string str;
    cin >> str;
    vector<int> integers = parseInts(str);
    for(int i = 0; i < integers.size(); i++) {
        cout << integers[i] << "\n";
    }
    
    return 0;
}

// Link : https://www.hackerrank.com/challenges/even-tree/problem
// Name : Even Tree
// Level : Medium
// Max Score : 50 

///////////////////////////////////////////////////////////

#include <iostream>
#include <vector>
using namespace std;
struct Node{
	int num,root;
};
int main(){
	int N,M;//nodes edges
	int x,y;
	int count = 0;
	cin >> N >> M;
	vector <Node> nodes = vector<Node>(N);	
	for(int i = 0;i < N;i++){
		nodes[i].num = 1;
		nodes[i].root = -1;
	}
	for(int i = 0;i < M;i++){
		cin >> x >> y;
		nodes[x-1].root = y-1;   
	}
	for(int i = N-1;i > 0;i--)
		if(nodes[i].root >= 0)
			nodes[nodes[i].root].num += nodes[i].num;
	for(int i = 0;i < N;i++)
		if(nodes[i].root >= 0 && nodes[i].num%2== 0)
			count ++;
	cout << count;
	return 0;
}
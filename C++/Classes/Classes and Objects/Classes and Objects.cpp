// Link : https://www.hackerrank.com/challenges/classes-objects/problem
// Name : Classes and Objects
// Level : Easy
// Max Score : 20

class Student{
    
    int x[5],sum=0;
    
   public :
     Student(){sum=0;}
    void input(){
        for(int i=0;i<5;i++){
            cin>>x[i];
            sum+=x[i];
        }
    }
    
    int calculateTotalScore(){return sum;}
    
};
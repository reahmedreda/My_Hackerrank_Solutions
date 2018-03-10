// Link : https://www.hackerrank.com/challenges/virtual-functions/problem
// Name : Virtual Functions
// Level : Medium
// Max Score : 40

class Person {
    
    public :
    
    string name ;
    int age;
    virtual void getdata()=0;
    virtual void putdata()=0;
    
};
class Professor: public Person{
    int p;
    static int cc;
    int y;
    public:
    Professor(){y=++cc;}
    void putdata(){cout<<name<<" "<<age<<" "<<p<<" "<<y<<"\n";}
    void getdata(){cin>>name>>age>>p;}
};
class Student :public Person{
    int marks[6],sum=0;
    static int c;
    int x;
    public:
    Student(){x=++c;}
    void putdata(){cout<<name<<" "<<age<<" "<<sum<<" "<<x<<"\n";}
    void getdata(){cin>>name>>age;
                  for(int i=0;i<6;i++){
                      cin>>marks[i];
                      sum+=marks[i];
                  }}
    
    
};

int Professor::cc=0;
int Student::c=0;
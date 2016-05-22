
#include<iostream>
#include<string>
using namespace std;

int main()
{
        int i,j;
        string s;
        char temp;
        while(cin>>s)
        {
                for(i=0;i<s.length()-1;i++)                              
                {
                        for(j=0;j<s.length()-1-i;j++)               
                        {
                                if(s[j]>s[j+1])
                                {
                                        temp=s[j];
                                        s[j]=s[j+1];
                                        s[j+1]=temp;                
                                }
                        }                
                }
                cout<<s<<endl;                                                       
        }        
        return 0;
}


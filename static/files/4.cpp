#include<iostream>
#include<fstream>
#include<string.h>
#include<algorithm>
#include<functional>

using namespace std;
int main()
{
        char ch[201];
        int len;
        while (cin>>ch)
        {
                len=strlen(ch);
                sort(ch,ch+len,less<char>());
                ch[len+1]='\0';
                cout<<ch<<endl;
        }
        return 0;
}

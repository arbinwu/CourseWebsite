#include<stdio.h>
#include<string.h>
int main()
{
        char string[200],t;
        int a,b,c;
        while(scanf("%s",string)!=EOF)
        {
                c=0;
                while(string[c])
                {
                        c++;
                }
                for(a=1;a<c;a++)
                {
                        for(b=0;b<c-a;b++)
                        {
                                if((string[b]-string[b+1])>0)
                                {
                                        t=string[b];
                                        string[b]=string[b+1];
                                        string[b+1]=t;
                                }
                        }
                }
                printf("%s\n",string);
        }
        return 0;
}

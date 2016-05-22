#include<stdio.h>
#include<string.h>
int main()
{
        char string[200],temp;
        int i,j,n;
        while(scanf("%s",string)!=EOF)
        {
                n=0;
                while(string[n])
                {
                        n++;
                }
                for(i=1;i<n;i++)
                {
                        for(j=0;j<n-i;j++)
                        {
                                if((string[j]-string[j+1])>0)
                                {
                                        temp=string[j];
                                        string[j]=string[j+1];
                                        string[j+1]=temp;
                                }
                        }
                }
                printf("%s\n",string);
        }
        return 0;
}

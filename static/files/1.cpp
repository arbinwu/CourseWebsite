#include <stdio.h>
#include <algorithm>
#include <string.h>
using namespace std;
int main(){
	char s1[300];
	while(scanf("%s",s1)!=EOF){
		int n=strlen(s1);
		sort(s1,s1+n);
		printf("%s\n",s1);
	}
} 

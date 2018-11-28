#include<iostream>
#include<stdlib.h>
using namespace std;

int main()
{
	unsigned char a[] = {153,176,135,158,112,232,65,68,5,4,139,154,116,188,85,88,181,97,142,54,172,9,89,229,97,221,62,63,185,21,237,213};
	for (int j=0;j<4;j++){
		for (int i = 31; i > 0; i--){
			a[i] = a[i] ^ a[i - 1];
		}
	}
	for (int i = 0; i <32; i++){
		a[i] ^= i;
		a[i] = (a[i] >> 2) | (a[i] << 6);	
	}
	cout<<endl << a << endl;
	system("pause");
	return 0;
}
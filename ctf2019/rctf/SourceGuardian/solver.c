#include<pch.h>
#include<iostream>
#include<string.h>
#include<iomanip>
#include<iostream>
#include<string>

using namespace std;
#define MX ((z>>5^y<<2) + (y>>3^z<<4) ^ (sum^y) + (k[p&3^e]^z))

long btea(long* v, long n, long* k) {
	unsigned long z = v[n - 1], y = v[0], sum = 0, e, DELTA = 0x9e3779b9;
	long p, q;
	if (n > 1) {          /* Coding Part */
		q = 6 + 52 / n;
		while (q-- > 0) {
			sum += DELTA;
			e = (sum >> 2) & 3;
			for (p = 0; p < n - 1; p++) y = v[p + 1], z = v[p] += MX;
			y = v[0];
			z = v[n - 1] += MX;
		}
		return 0;
	}
	else if (n < -1) {  /* Decoding Part */
		n = -n;
		q = 6 + 52 / n;
		sum = q * DELTA;
		while (sum != 0) {
			e = (sum >> 2) & 3;
			for (p = n - 1; p > 0; p--) z = v[p - 1], y = v[p] -= MX;
			z = v[n - 1];
			y = v[0] -= MX;
			sum -= DELTA;
		}
		return 0;
	}
	return 1;
}

int main()
{
	long cipher[] = { 1029560848, 2323109303, 4208702724, 3423862500, 3597800709, 2222997091, 4137082249, 2050017171, 4045896598 ,0};
	long key[] = { 1752186684, 1600069744, 1953259880, 1836016479 };
	long k[] = { 1752186684, 1600069744, 1953259880, 1836016479 };
	int i = 0;
	for (i = 0; i < 9; i++)
	{
		cipher[i] ^= key[i % 4];
	}
	btea(cipher, -9, key);
	cout << (char*)cipher << endl;
 }
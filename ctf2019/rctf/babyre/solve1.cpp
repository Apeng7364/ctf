#include<pch.h>
#include<iostream>

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
	long cipher[] = { 0,0 };
	char cipher1[] = "Bingo!\x02\x02";
	long key[] = { 0xE0C7E0C7, 0xC6F1D3D7, 0xC6D3C6D3, 0xC4D0D2CE };
	int i = 0;
	for (i = 0; i < 6; i++)
		cipher1[i] ^= 0x17;
	memcpy(cipher, cipher1, 8);
	btea(cipher, 2, key);
	char *b = (char *)cipher;
	cout << "rctf{";
	for (i = 0; i < 8; i++)
	{
		char c1 = *(b + i) >> 4 & 0xF;
		char c2 = *(b + i) & 0xF;
		if (c1 < 10)
			cout << char(c1 + 0x30);
		else
			cout << char(c1 + 0x61 - 10);
		if (c2 < 10)
			cout << char(c2 + 0x30);
		else
			cout << char(c2 + 0x61 - 10);
	}
	cout << "}";
}
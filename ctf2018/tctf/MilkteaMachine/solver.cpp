#include "pch.h"
#include<iostream>
#include<string.h>
#include<iomanip>
using namespace std;

struct process
{
	unsigned int seed;
	unsigned int debug_whom;
	unsigned int debugged_by_whom;
	unsigned int rand_times;
	unsigned int encode_times;
	unsigned int pipe_use_times;
};

unsigned int main()
{
	unsigned int i, j, t, f, k;
	unsigned int sum = 0;
	unsigned int v2, v3, v6, temp;
	const unsigned  int const_numbers[256] = { 0x29D1C318, 0x0A2127F7C, 0x63535511, 0x0BC20EB9F, 0x62861759, 0x72E2EB39, 0x245A3503, 0x0B6A0B33C, 0x0D8588DF7, 0x32C97731, 0x9C2286A1, 0x0B06F0DF1, 0x3EE8DCD8, 0x0E8AAFD91, 0x2FB7CA47, 0x2E56ED51, 0x0F37AB222, 0x0EDF06A3E, 0x4786ED37, 0x66A60B4D, 0x0CE004DF1, 0x0A706131C, 0x469F7415, 0x92620669, 0x0C28915C3, 0x0F4A0FCB0, 0x909CACEB, 0x25726D7B, 0x7023830A, 0x75364D20, 0x0EBF4D0ED, 0x57E7B138, 0x3FBBDBC4, 0x1AD6A53, 0x2D57B709, 0x0DDAAD68A, 0x847CA156, 0x0A7A8EE84, 0x645D7D31, 0x62B8030F, 0x3C72E503, 0x0B3C1B143, 0x51912BC7, 0x0D155CA1B, 0x79A606FB, 0x6541EB4E, 0x0FC6BD15E, 0x0ED72E7CF, 0x0F8DE314F, 0x8097C65A, 0x3D573A48, 0x55389B74, 0x17504A, 0x0F96ABCF3, 0x4468045C, 0x70FEEECE, 0x7E000AF2, 0x8BF35B81, 0x4B635910, 0x0A9CB945B, 0x47B77790, 0x0EE90D37E, 0x0BB6C15B5, 0x44A5FC82, 0x5397C185, 0x4A79753B, 0x3781C8A0, 0x0CBD7D92B, 0x0ECFF291B, 0x0C8C0208F, 0x0DC7F4825, 0x7F1D5D37, 0x55D85393, 0x90B4F86C, 0x0B97CA571, 0x0F72BDA18, 0x2A929732, 0x0A7F5F2AB, 0x0DC0BB6C6, 0x4841A73F, 0x2DC84A8A, 0x0DEFD50A5, 0x0C5E0FC89, 0x0BFF26C11, 0x4C200AE8, 0x0E0EC8414, 0x6304462C, 0x7735F7C2, 0x0FE9A59CE, 0x146FF117, 0x5C4E8032, 0x0F554D32, 0x0A8CF5DC, 0x6460AD4C, 0x53EB5293, 0x0C95F9E2F, 0x0F3D5A7FB, 0x0EEAF150F, 0x3F4C7C03, 0x0AA0E5C3D, 0x1EF6A22E, 0x9040D341, 0x0D84790F7, 0x3A087715, 0x95BD943E, 0x13E96958, 0x2332540B, 0x65AEC20C, 0x0D6ECB393, 0x1F332E53, 0x155517F2, 0x14831CB7, 0x53BC2D13, 0x0C63A603A, 0x0F80D03FA, 0x6C4AA4A1, 0x2E5C553A, 0x0B4F0A536, 0x81987C04, 0x0A5B6712, 0x38FE2F2C, 0x3DFBCCBC, 0x536F716E, 0x0C37A2560, 0x987B71B, 0x8101E088, 0x64559DD8, 0x0FC0B1F57, 0x7468510A, 0x3A8054BD, 0x0BD153266, 0x77348038, 0x2DF6BFDE, 0x0F54EFCE6, 0x0A65794AA, 0x7CAF657B, 0x632F605E, 0x0E3E21DCE, 0x124F9945, 0x0AA3CA9E9, 0x50913A, 0x57EA2907, 0x0E050101D, 0x0B1E1653E, 0x59582EAF, 0x0DB5FDD8B, 0x0EF8B08BB, 0x19973D7A, 0x7A7A6C1C, 0x7B2F08D7, 0x6236A643, 0x891F2BFE, 0x0FF9456AD, 0x9F278CB0, 0x0D2D9A066, 0x77F7192A, 0x71C95997, 0x0C7E455A3, 0x0C117B13D, 0x331086B7, 0x0CCBA9A0F, 0x0E786485B, 0x800BC70F, 0x73359B2F, 0x0CFD0632, 0x4FDCBCC3, 0x58487C96, 0x799B3F9F, 0x0FE948657, 0x0F083ED1C, 0x105A0B99, 0x0ABA65BF7, 0x1A23ACBB, 0x0D80516BF, 0x9026EF32, 0x95C38248, 0x4132FC4D, 0x1663E8B0, 0x6B3BC663, 0x23AF6996, 0x6A3EA057, 0x52D8FDE4, 0x997344F0, 0x0AA0E6C66, 0x436DBAED, 0x7B91F8BF, 0x0E80E07D, 0x6E56F2E0, 0x0E00EDF1A, 0x0AD54535D, 0x27DA2387, 0x0ADF3F52D, 0x0EDCBF5BB, 0x55CD19C2, 0x0E795156A, 0x3E99A660, 0x30EF3300, 0x0C1FA04BD, 0x0A94F5D3D, 0x0B265DA09, 0x593C3698, 0x14A56619, 0x36BAF68C, 0x3486C520, 0x0CD869ACB, 0x9E85C60A, 0x52AB126E, 0x83A15421, 0x60D2A51D, 0x0A3263723, 0x6F01FB9C, 0x0F0A01A9D, 0x0B8A706E2, 0x2CBFC241, 0x665AFFA7, 0x5CEAFE7D, 0x1B09E16D, 0x0B005DCCE, 0x0EE4070FC, 0x0C5EA7CDC, 0x6500B692, 0x0AADEDD27, 0x0F5A153A6, 0x5D587425, 0x8D570F3A, 0x3B5AB58A, 0x59D5D66B, 0x5B7517CB, 0x0BACE72D1, 0x5F3D4D71, 0x9708837B, 0x47FC85C3, 0x56A55D09, 0x8FC4C937, 0x3265B5B2, 0x0CC0D03BF, 0x0CDB15016, 0x54E49060, 0x0CA7813E8, 0x2B7E7859, 0x0D2154104, 0x6389FDB, 0x291BB90A, 0x0BC5388C7, 0x7E191A1B, 0x2F369C44, 0x0BBE9B02B, 0x13714D6C, 0x0FB73A3E5, 0x0A5EA5A2E, 0x0DFAC48EE, 0x5B61310A, 0x0FBBB34B1, 0x3F50310F, 0x0F78AC7BE, 0x28AF2A56 };

	wchar_t plain[44] = { 0 };
	wchar_t cipher[44] = { 0 };
	wchar_t real_cipher[44] = { 0x4A46, 0x4B10, 0x2AFB, 0x0D924, 0x58B8, 0x0B3B0, 0x0F777, 0x6068, 0x4F2C, 0x7670, 0x10F7, 0x2638, 0x8F55, 0x1CC6, 0x0D9E0, 0x1C80, 0x15B0, 0x0C0C0, 0x2ED8, 0x0A440, 0x70DF, 0x6C58, 0x333C, 0x1BAB, 0x5240, 0x4F92, 0x0EEC8, 0x1084, 0x1C40, 0x0F71E, 0x7A1B, 0x0BD38, 0x9550, 0x9474, 0x3300, 0x0F720, 0x0DAC4, 0x1FF4, 0x6920, 0x0B66C, 0x829E, 0x5524, 0x4788 };
	process p[33];

	for (sum = 3908; sum < 0xff * 43; sum++)
	{
		//init
		for (k = 0; k < 43; k++)
		{
			for (plain[k] = 0x20; plain[k] < 0xff; plain[k]++)
			{
				srand(sum);
				p[0].seed = sum;
				p[0].rand_times = 0;
				p[0].debug_whom = -1;
				p[0].debugged_by_whom = -1;
				p[0].encode_times = 0;
				p[0].pipe_use_times = 0;
				for (i = 1; i < 33; i++)
				{
					p[i].seed = rand();
					p[i].rand_times = 0;
					p[i].debugged_by_whom = -1;
					p[i].debug_whom = -1;
					p[i].encode_times = 0;
					p[i].pipe_use_times = 0;
				}
				//init debug link
				srand(rand());
				p[0].debug_whom = rand() % 32 + 1;
				p[p[0].debug_whom].debugged_by_whom = 0;
				p[0].rand_times = 1;
				temp = p[0].debug_whom;
				for (i = 1; i < 32; i++)
				{
					srand(p[temp].seed);
					rand();
					rand();
					srand(rand());
					f = 1;
					while (f)
					{
						t = (rand() % 32) + 1;
						p[temp].rand_times++;
						if (p[t].debugged_by_whom == -1)
							f = 0;
					}
					p[temp].debug_whom = t;
					p[t].debugged_by_whom = temp;
					temp = t;
				}
				temp = 0;
				//get a pipe
				for (i = 0; i <= k; i++)
				{
					if (i == 0)
					{
						srand(sum);
						for (j = 0; j < 32; j++)
							rand();
						rand();
					}
					else
					{
						srand(p[temp].seed);
						rand();
						rand();
						if (p[temp].debug_whom != -1)
						{
							rand();
							rand();
						}
						for (j = 0; j < p[temp].pipe_use_times; j++)
						{
							rand();
							rand();
						}
						p[temp].pipe_use_times++;
						srand(rand());
					}
					v2 = 9 * const_numbers[(1337 * rand()) % 256];
					v3 = rand();
					temp = (plain[i] * v3 - v2) & 31;
					temp++;//temp:next pipe numbers, the process numbers. too;
					//encode;
					if (p[temp].debugged_by_whom == 0)
					{
						srand(sum);
						for (j = 0; j < 32; j++)
							rand();
					}
					else
					{
						srand(p[p[temp].debugged_by_whom].seed);
						rand();
						rand();
					}
					srand(rand());
					for (j = 0; j < p[p[temp].debugged_by_whom].encode_times; j++)
					{
						rand();
						rand();
					}
					for (j = 0; j < p[p[temp].debugged_by_whom].rand_times; j++)
						rand();
					v6 = 13090 * rand() % 256;
					cipher[i] = const_numbers[v6] * plain[i] * rand();
					p[p[temp].debugged_by_whom].encode_times++;
				}
				if (cipher[k] == real_cipher[k])
				{
					cout << char(plain[k]);
					break;
				}
			}
		}
		break;
	}
}
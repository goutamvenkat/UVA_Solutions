#include <cstdio>
using namespace std;

int Max(int a, int b) {return (a > b ? a : b);}
int Min(int a, int b) {return (a < b ? a : b);}
int main(int argc, char const *argv[])
{
	int n;
	int m;
	while (scanf("%d %d", &n, &m) != EOF) 
	{
		int max = 1;
		int old_n = n;
		int old_m = m;
		n = Min(n, m);
		m = Max(old_n, m);
		for (int i = n; i <= m; i++) 
		{
			int count = 0;
			int j = i;
			while (j != 1) 
			{
				if (j % 2 == 0) j >>= 1;
				else j = (j*3) + 1;
				count++;
			}
			count++;
			max = Max(count, max);
		}
		printf("%d %d %d\n", old_n, old_m, max);
	}

	return 0;
}
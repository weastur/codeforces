#include <iostream>
#include <algorithm>

using namespace std;

const int maxlen = 100500;
int t, n, a[maxlen], b[maxlen];

int main()
{
	ios_base::sync_with_stdio(false);
	cin.tie(0);
	cout.tie(0);

	cin >> t;
	while (t--)
	{
		cin >> n;
		for (int i = 0; i < n; ++i)
		{
			cin >> a[i];
		}
		sort(a, a + n);
		int l = 0;
		int r = n - 1;
		int i = 0;
		while (l <= r)
		{
			if (l == r)
			{
				b[i++] = a[l++];
			}
			else
			{
				b[i++] = a[r--];
				b[i++] = a[l++];
			}
		}
		for (int i = n - 1; i >= 0; i--)
		{
			cout << b[i] << " ";
		}
		cout << endl;
	}

	return 0;
}

#include <iostream>
#include <algorithm>

using namespace std;

const int maxlen = 100500;
long long d, a[maxlen];
int n, t, ans;

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
		long long mmax = 0;
		for (int i = 1; i < n; ++i)
		{
			if (a[i] >= a[i - 1])
			{
				continue;
			}
			mmax = max(mmax, a[i - 1] - a[i]);
			a[i] = a[i - 1];
		}
		ans = 0;
		if (mmax)
		{
			d = 1;
			ans = 1;
			while (d * 2 <= mmax)
			{
				++ans;
				d *= 2;
			}
		}
		cout << ans << endl;
	}

	return 0;
}

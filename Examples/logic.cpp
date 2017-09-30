#include <bits/stdc++.h>

using namespace std;

int main() {
	int t;
	cin >> t;
	while(t--) {
		long long n, x, res;
		cout << n;
		x = (n*(n+1))/2;
		res = x*x;
		cout << res%1000000007 << endl;
	}
	return 0;
}
#include <stdio.h>
#include <math.h>

int main() {
	int t;
	scanf("%d", &t);
	while(t--) {
		long long n, x, res;
		scanf("%lld", &n);
		x = (n*(n+1))/2;
		res = x*x;
		printf("%lld\n", res%1000000007);
	}
	return 0;
}

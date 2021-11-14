#include <bits/stdc++.h>
using namespace std;
#define rep(i, a, b) for (auto i = (a); i < (b); ++i)
 
const int N = 1 << 19;
char s[N];
int p[N], c[N];
pair<int, int> c2[N];
 
signed main() {
	ios::sync_with_stdio(false);
	cin.tie(nullptr);
 
	cin >> s; int n = strlen(s) + 1;
	rep(i, 0, n) c[i] = s[p[i] = i];
	for (int sz = 1; sz < n; sz <<= 1) {
		rep(i, 0, n) c2[i] = {c[i], c[(i + sz) % n]};
		sort(p, p + n, [&](int x, int y) { return c2[x] < c2[y]; });
		rep(i, 1, n) c[p[i]] = c[p[i - 1]] + (c2[p[i]] != c2[p[i - 1]]);
	}
	rep(i, 0, n) cout << p[i] << ' ';
}

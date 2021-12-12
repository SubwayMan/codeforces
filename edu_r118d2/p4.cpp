#include <bits::stdc++.h>

using namespace std;

#define int long long
#define endl "\n";

int INF = 998244353;
int n;
int mod_add(int a, int b) {
    return ((a%INF)+(b%INF))%INF;
}

int phi(int i, int mex, bool lock, vector<int> &a) {
    if (i==n) return 1;

    if (lock)

}

void solve(vector<int> &a) {
    int ans = phi(0, 0, false, a);
    cout << ans << endl;

}

int main() {
    ios_base::sync_with_stdio(0);
    cin.tie(0); cout.tie(0);

    int t;
    cin >> t;

    while (t--) {
        cin >> n;
        vector<int>(n) a;
        for (int i=0; i<n; ++i) cin >> a[i];
        solve(a);

    }
    return 0;
}


#include <iostream>
#include <vector>
using namespace std;

void solve() {
    string s; cin >> s;
    int n = s.length();
    int ans = n;

    for (int i=0; i<n; ++i) {
        if (s[i] == '1')
            ans = n-i;
        else if (s[i] == '0') {
            ans -= (n-i)-1;
            break;
        }
    }
    cout << ans << "\n";
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(0);
    int t = 1; 
    cin >> t;
    while (t--) 
        solve();
}

#include <iostream>
#include <vector>

using namespace std;

void solve() {
    int n, k; cin >> n >> k;
    string s; cin >> s;
    vector<int> vals(n);
    if (k%2 == 1) {
        for (int i=0; i<n; ++i) {
            if (s[i] == '1') {
                s[i] = '0';
            } else {
                s[i] = '1';
            }
        }
    }
        
    for (int i=0; i<n; ++i) {
        if (k != 0 && s[i] == '0') {
            s[i] = '1'; k--;
            vals[i] = 1;
        }
    }
    if (k != 0) {
        vals[n-1] += k;
        if (k%2 == 1) s[n-1] = '0';
    }
    cout << s << "\n";
    for (auto e: vals) {
        cout << e << " ";

    }
    cout << "\n";
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(0);

    int t; cin >> t;
    while (t--) solve();

}


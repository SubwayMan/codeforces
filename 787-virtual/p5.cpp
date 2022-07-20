#include <iostream>
#include <vector>
using namespace std;

void solve() {
    int n, k; cin >> n >> k;
    string s; cin >> s;
    int hold;

    vector<char> seen(150, '0');
    for (int i='a'; i<='z'; ++i)
        seen[i] = i;

    for (int i=0; i<n; ++i) {
        while (s[i] != seen[s[i]]) 
            s[i] = seen[s[i]];

        while (s[i] > 'a' && k) {
            hold = s[i];
            s[i]--;
            while (s[i] != seen[s[i]]) 
                s[i] = seen[s[i]];
            seen[hold] = s[i];
            k--;
        }

    }
    cout << s << "\n";

}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(0);
    int t = 1; 
    cin >> t;
    while (t--) 
        solve();
}

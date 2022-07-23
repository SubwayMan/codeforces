
#define _USE_MATH_DEFINES

#include <ios>
#include <iostream>
#include <algorithm>
#include <string>
#include <cstring>
#include <map>
#include <vector>
#include <climits>
#include <map>
#include <queue>

using namespace std;
typedef long long ll;

int n;

void solve() {
    cin >> n;
    vector<string> mat(n);
    int c = 0;

    for (int i=0; i<n; ++i) {
        cin >> mat[i];
        for (char e: mat[i]) {
            if (e=='1') c++;
        }
    }

    int ans = c+n;
    for (int r=0; r<n; ++r) {
        int row=r;
        int tot1=0;
        for (int col=0; col<n; ++col) {
            if (mat[(row+col)%n][col] == '1')
                tot1++;
        }
        ans = min(ans, c-tot1+(n-tot1));
    }
    cout << ans << "\n";

}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(0);


    int t; cin >> t;
    while (t--) 
        solve();
}

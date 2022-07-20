
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
#include <set>

using namespace std;
typedef long long ll;
int n;

pair<int, string> dp(int i, set<int> bag, string s, int iq, vector<int> &a) {
    if (i==n || iq == 0) return {0, s};
    if (iq >= a[i]) {
        pair<int, string> ret = dp(i+1, bag, s+"1", iq, a); ret.first++;
        return ret;
    }

    pair<int, string> ret = dp(i+1, bag, s+"0", iq, a);
    bag.insert(a[i]);
    pair<int, string> r1 = dp(i+1, bag, s+"1", iq-1, a); r1.first += 1;
    ret = max(ret, r1);

    if (a[i]-iq <= bag.size()-1) {
        bag.erase(a[i]);
        for (int i=0; i<a[i]-iq; ++i)
            bag.erase(bag.begin());
        bag.insert(a[i]);
        pair<int, string> r2 = dp(i+1, bag, s+"1", iq-1, a); r2.first += 1;
        ret = max(ret, r2);
    }
    return ret;

}
void solve() {
    int k; cin >> n >> k;
    vector<int> a(n);
    for (int i=0; i<n; ++i) cin >> a[i];
    set<int> u;
    pair<int, string> result = dp(0, u, "", k, a);
    string sans = result.second;
    while (sans.length() < n) sans.push_back('0');
    cout << sans << "\n";


}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(0);


    int t; cin >> t;
    while (t--) 
        solve();
}

#include <iostream>
#include <cmath>
#include <unordered_set>
#include <algorithm>
#include <vector>
#include <map>
#include <queue>
#include <cstring>
using namespace std;

void solve();

int ks(map<pair<int, int>, int> &, const vector<pair<int, int>> &, pair<int, int>, const int &);

void make_costs(vector<int> &);

vector<int> get_factors(int &);

ostream& operator<<(ostream &o, vector<pair<int, int>> &v) {
    o << "{";
    for (auto pi : v) {
        o << "(" << pi.first << ", " << pi.second << "),";
    }
    o << "}";
    return o;
}

ostream& operator<<(ostream &o, vector<int> &v) {
    o << "{";
    for (auto e: v) o << e << ", ";
    o << "}";
    return o;
}

vector<int> cost(1001, -1);

int main() {
    ios::sync_with_stdio(false);
    cin.tie(0);
    make_costs(cost);

    int t; cin >> t;
    while (t--) {
        solve();
    }
}

void solve() {
    int n, k, x; cin >> n >> k;
    k = min(k, 12*n);
    vector<int> a(n);
    for (int i=0; i<n; ++i) {
        cin >> x;
        a[i] = cost[x];
    }
    vector<pair<int, int>> pis;
    for (int i=0; i<n; ++i) {
        cin >> x;
        pis.push_back(make_pair(a[i], x));
    }
    sort(pis.begin(), pis.end());
    map<pair<int, int>, int> dp;
    x = ks(dp, pis, make_pair(0, 0), k);
    cout << x << "\n";

}

int ks(map<pair<int, int>, int> &dp, const vector<pair<int, int>> &pis, pair<int, int> iw, const int &k) {
    if (dp.find(iw) != dp.end()) return dp[iw];
    if (iw.first == pis.size()) return 0;

    const pair<int, int> *pi = &pis[iw.first];
    if (pi->first + iw.second > k) return dp[iw] = 0;

    return dp[iw] = max(ks(dp, pis, make_pair(iw.first+1, iw.second+pi->first), k) + pi->second, 
            ks(dp, pis, make_pair(iw.first+1, iw.second), k));

}

void make_costs(vector<int> &cost_arr) {
    cost_arr[1] = 0;
    int depth = 1, hold, nv, ub;
    vector<int> v;
    queue<int> q; q.push(1);
    while (!q.empty()) {
        ub = q.size();
        for (int i=0; i<ub; ++i) {
            hold = q.front(); q.pop();
            v = get_factors(hold);
            for (auto e: v) {
                nv = hold + e;
                if (nv > 1000) continue;
                if (cost_arr[nv] != -1) continue;
                cost_arr[nv] = depth;
                q.push(nv);
            }
        }
        depth++;
    }
}

vector<int> get_factors(int &n) {
    vector<int> ret;
    unordered_set<int> seen;
    int hold;
    for (int i=1; i<= n; i++) {
        hold = n/i;
        if (seen.find(hold) == seen.end()) {
            seen.emplace(hold);
            ret.push_back(hold);
        }
    }
    return ret;
}

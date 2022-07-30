
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
void solve() {
    cin >> n;
    set<int> graph[n+1];
    set<int> dmap[n+1];
    int a, b; 
    vector<pair<int, int>> dis;
    for (int i=1; i<=n; ++i) {
        cin >> a >> b;
        dis.push_back({a, b});
        dmap[a].insert(i);
        dmap[b].insert(i);
    }

    for (int i=1; i<=n; ++i) {
        if (dis[i-1].first==dis[i-1].second) {
            cout << "nO" << "\n";
            return;
        }

        for (auto e: dmap[dis[i-1].first]) {
            if (e==i) continue;
            graph[i].insert(e);
        }

        for (auto e: dmap[dis[i-1].second]) {
            if (e==i) continue;
            graph[i].insert(e);
        }
        if (graph[i].size() > 2) {
            cout << "NO" << "\n";
            return;
        }
    }
    /*
    for (int i=1; i<=n; ++i) {
        cout << i << ": ";
        for (auto e: graph[i]) cout << e << " ";
        cout << "\n";
    }
    */


    vector<int> marks(n+1, -1);
    for (int i=1; i<=n; ++i) {
        if (marks[i] != -1) continue;
        queue<int> q;
        q.push(i);
        int col = 1;
        marks[i] = col;
        while (!q.empty()) {
            int node = q.front();
            q.pop();
            for (auto e: graph[node]) {
                if (marks[e] == marks[node]) {
                    cout << "No" << "\n";
                    return;
                }
                if (marks[e] == -1) {
                    marks[e] = marks[node]^1;
                    q.push(e);
                }
            }
        }
    }
    cout << "YES" << "\n";
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(0);


    int t; cin >> t;
    while (t--) 
        solve();
}

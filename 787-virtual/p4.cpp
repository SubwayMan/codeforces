#include <iostream>
#include <vector>
#include <queue>
#include <unordered_set>
using namespace std;

void printv(vector<int> &v) {
    for (auto e: v)
        cout << e << " ";
}
void printvb(vector<int> &v) {
    for (auto e = v.rbegin(); e!=v.rend(); ++e)
        cout << *e << " ";
}

void solve() {
    int n; cin >> n;
    vector<int> a(n+1);
    vector<int> adj[n+1];
    int temp, root;
    for (int i=1; i<n+1; ++i) {
        cin >> temp;
        a[i] = temp;
        if (temp == i) root = temp;
        else {
            adj[temp].push_back(i);
        }
    }

    queue<int> q;
    vector<int> ends;
    q.push(root);

    while (!q.empty()) {
        temp = q.front(); q.pop();
        if (adj[temp].size() == 0) {
            ends.push_back(temp);
            continue;
        }

        for (auto e: adj[temp]) {
            q.push(e);
        }
    }
    vector<vector<int>> paths;
    vector<int> path, rootpaths;
    unordered_set<int> seen;
    int cur, i=0;
    for (auto e: ends) {
        cur = e;
        path.clear();
        while (seen.find(cur) == seen.end()) {
            path.push_back(cur);
            seen.emplace(cur);
            cur = a[cur];
        }
        paths.push_back(path);
        i++;
    }

    int lp = paths.size();
    cout <<  lp << "\n";
    for (int i=0; i<lp; ++i) {
        cout << paths[i].size() << "\n";
        printvb(paths[i]);
        cout << "\n";
    }
    cout << "\n";
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(0);
    int t = 1; 
    cin >> t;
    while (t--) 
        solve();
}

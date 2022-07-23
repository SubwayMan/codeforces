
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
    vector<int> graph[n+1];
    int a, b; 
    for (int i=0; i<n; ++i) {
        cin >> a >> b;
        graph[a].push_back(b);
        graph[b].push_back(a);
    }

    vector<int> seen(n+1);
    for (int i=1; i<=n; ++i) {
        if (graph[i].size() > 2) {
            cout << "No" << "\n";
            return;
        }
        //if (seen[i] != 0 || graph[

    }

}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(0);


    int t; cin >> t;
    while (t--) 
        solve();
}

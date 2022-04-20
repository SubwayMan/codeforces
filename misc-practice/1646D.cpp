#include <iostream>
#include <vector>
#include <algorithm>
#include <bitset>
using namespace std;

bitset<200001> dp(vector<int> (&graph)[], int (&p1)[], int (&p2)[], int n, int P) {
    bitset<200001> base, val1, val2, hold;
    int sum1=0, sum2=0;

    for (auto e: graph[n]) {
        if (e==P) continue;
        hold = dp(graph, p1, p2, e, n);
    }

}

int main() {
    int n; cin >> n;
    vector<int> graph[n+1];
    int a, b;
    while (cin >> a >> b) {
        graph[a].push_back(b);
        graph[b].push_back(a);
    }

    if (n==2) {
        cout << "2 2\n1 1\n";
        return 0;
    }
}

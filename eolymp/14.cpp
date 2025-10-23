#include <cmath>
#include <bits/stdc++.h>
using namespace std;

int main() {
    int n, m, mi;
    cin >> n;
    cin >> m;
    vector<int> v(110000, 1);
    v[0] = 0;
    v[1] = 0; 
    for (int i = 2; i<v.size();i++) {
        if (v[i] ==1) {
            for (int j = i*i; j < v.size(); j+=i) {
                v[j] = 0;
            }
        }
    }
    vector<int> primes;
    for (int i = 2; i < v.size();i++) {
        // cout<<i << ":" << v[i] << " ";
        if (v[i]==1) {primes.push_back(i);}
        if (i == m) {mi = primes.size();}
    }
    if (m+n-1 > primes[mi+1]) {
        cout << -1;
    } else { 
        cout << 1;
    }
}



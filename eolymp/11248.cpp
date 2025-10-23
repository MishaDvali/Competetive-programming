#include <bits/stdc++.h>
#include <cmath>
using namespace std;

int main() {
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);

    int a, b, c;
    cin >> b;
    cin >> c;

    vector<int> sieve(pow(10, 6), 1);
    sieve[0]=0;
    sieve[1]=0;
    for (int i = 0; i < (int)sqrt(sieve.size());++i){
        if (sieve[i]) {
            for (long long j = i * i; j < sieve.size();j+=i) {
                sieve[j] = 0;
            }
        }
    }
    int left = c;
    for (a = b; a > 0 && left > 0; a--) {
        if (sieve[a]) {left--;}
    }
    cout << a+1;
}


#include <bits/stdc++.h>
using namespace std;
#include <cmath>;

long long int sq (long long int n) {
    long long int ans;
    s = sqrt(n);
    ans = 2*((s+1)*(s));
    long long int sq_left = n - s*s;
    ans += sq_left * 2;
    ans += ceil(sq_left / (double)s);
    return ans;
}
int main() {
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);

    // example below, replace it with your solution
    long int n;
    cin>>n;
    cout << sq(n);
}
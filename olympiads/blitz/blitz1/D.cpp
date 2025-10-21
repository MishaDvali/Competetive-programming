#include <bits/stdc++.h>
#include <unordered_map>
using namespace std;

int main() {
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);
    int t;
    cin>>t;
    int count_key;
    int nm;
    int new_p;
    for (int tt = 0;tt < t;++t) {
        cin >> nm;
        std::unordered_map<int, int> p_n_d;
        for (int a =1;a < nm+1;a++) {
            new_p=1;
            for (int b = 1;b < nm; b++) {
                new_p=new_p*a;
                count_key=p_n_d.count(new_p);
                if (count_key == 0) {
                    p_n_d[count_key]=1;
                } else {p_n_d[count_key] = p_n_d[count_key]+1;}
            }
        }
    }


}

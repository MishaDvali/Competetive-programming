#include <iostream>
#include <vector>
#include <tuple>
#include <string>
#include <algorithm>

using namespace std;

// Function to compute the pair (y, z-y) for numbers a and b.
pair<int, int> check(int a, int b) {
    // Count digit frequencies for a and b.
    string s = to_string(a), t = to_string(b);
    int countA[10] = {0}, countB[10] = {0};
    for (char c : s)
        countA[c - '0']++;
    for (char c : t)
        countB[c - '0']++;
    
    int z = 0;
    for (int d = 0; d < 10; d++)
        z += min(countA[d], countB[d]);
    
    // Count the number of i in [0, 5] for which a/(10^i) equals b/(10^i).
    // Note: Using pow10 computed as 10^i (i.e. 10 raised to i).
    int y = 0;
    for (int i = 0; i < 6; i++) {
        int pow10 = 1;
        for (int j = 0; j < i; j++) {
            pow10 *= 10;
        }
        if (a / pow10 == b / pow10)
            y++;
    }
    return {y, z - y};
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    
    int n;
    cin >> n;
    
    // Data contains triples (x, y, z) for each input line.
    vector<tuple<int, int, int>> data;
    for (int i = 0; i < n; i++) {
        int x, y, z;
        cin >> x >> y >> z;
        data.emplace_back(x, y, z);
    }
    
    int countCandidates = 0;
    
    // Iterate over all 6-digit numbers.
    for (int i = 100000; i < 1000000; i++) {
        bool valid = true;
        for (auto [x, y, z] : data) {
            auto [y2, z2] = check(i, x);
            if (y2 != y || z2 != z) {
                valid = false;
                break;
            }
        }
        if (valid) {
            countCandidates++;
            // More than one valid candidate found: answer "NO".
            if (countCandidates > 1) {
                cout << "NO" << "\n";
                return 0;
            }
        }
    }
    
    cout << (countCandidates == 1 ? "YES" : "NO") << "\n";
    return 0;
}

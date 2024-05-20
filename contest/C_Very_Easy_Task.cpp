#include <iostream>
#include <algorithm>

using namespace std;

bool good(int time, int n, int x, int y) {
    if (time < min(x, y))
        return false;

    time -= min(x, y);
    
    int count = (time / x) + (time / y) + 1;
    return count >= n;
}

int main() {
    int n, x, y;
    cin >> n >> x >> y;

    int l = 0, r = max(x, y) * n ;

    while (l + 1 < r) {
        int mid = l + (r - l) / 2;

        if (good(mid, n, x, y))
            r = mid;
        else
            l = mid;
    }

    cout << r << endl;

    return 0;
}

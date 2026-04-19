#include<iostream>
using namespace std;
int main()
{
    int m, t, s;
    cin >> m >> t >> s;

    if (t == 0) {
        cout << 0 << endl;
        return 0;
    }

    int eaten = (s + t - 1) / t;
    int left = m - eaten;
    if (left < 0) {
        left = 0;
    }

    cout << left << endl;
    return 0;
}
#include<iostream>
#include<iomanip>
using namespace std;
int main()
{
    int n, k;
    cin >> n >> k;
    int Asum = 0;
    int Bsum = 0;
    int Acnt = 0;
    int Bcnt = 0;

    for(int i = 1; i <= n; i++){
        if(i % k == 0){
            Asum += i;
            Acnt++;
        }else{
            Bsum += i;
            Bcnt++;
        }
    }

    cout << fixed << setprecision(1)
         << (double)Asum / Acnt << ' '
         << (double)Bsum / Bcnt << endl;
    return 0;
}

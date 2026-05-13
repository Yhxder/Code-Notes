#include<iostream>
using namespace std;
int main(){
    int k, days=0, sum=0;
    cin>>k;
    for(int i=0; i<k;i++){
        for(int j=0; j<i;j++){
            sum+=i;
            days++;
            if(days==k){
                break;
            }
        }
        if(days==k){
            break;
        }
    }
    cout<<sum;
    return 0;
}
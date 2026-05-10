#include<iostream>
using namespace std;
int main(){
    int n;
    cin>>n;
    int minValue;
    cin>>minValue;
    for(int i=1;i<n;i++){
        int x;
        cin>>x;
        if(x<minValue){
            minValue=x;
        }
    }
    cout<<minValue<<endl;
    return 0;
}
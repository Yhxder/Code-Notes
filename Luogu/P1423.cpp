/*题目描述
小玉开心的在游泳，可是她很快难过的发现，自己的力气不够，游泳好累哦。已知小玉第一步能游 2 米，可是随着越来越累，力气越来越小，她接下来的每一步都只能游出上一步距离的 98%。现在小玉想知道，如果要游到距离 s 米的地方，她需要游多少步呢。请你编程解决这个问题。

输入格式
输入一个实数 s（单位：米），表示要游的目标距离。

输出格式
输出一个整数，表示小玉一共需要游多少步。 */
#include<iostream>
using namespace std;
int main(){
    double s;
    cin>>s;
    double step=2;
    int cnt=0;
    while(s>0){
        s=s-step;
        step=step*0.98;
        cnt++;
    }
    cout<<cnt<<endl;
    return 0;
}


// count digits in a number

#include<bits/stdc++.h>
using namespace std;
int main(){
    int n;
    while(1){
    cin>>n;
    // int count=0;
    // while(n!=0){
    //     count++;
    //     n=n/10;
    // }
    // cout<<count;

    int count=(int)(log10(n)+1);
    cout<<count<<endl;;
    }
    return 0;    
}

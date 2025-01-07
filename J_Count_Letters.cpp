
#include<bits/stdc++.h>
using namespace std;
int main(){
    string s;
    cin >> s;
    int frq[26] ={0};

    for (char c:s){
        frq[c - 'a']++;
    }

    for (int i=0; i<26; i++){
        if(frq[i]>0)
        cout << char(i + 'a')<< " : " << frq[i] << endl;
    }
   
    return 0;
}
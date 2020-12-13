#include <bits/stdc++.h>
using namespace std;

const int maxn=1e6+10;
string ch,tem;
int cnt[maxn];
vector <pair<int,string>> e[maxn];
string ans;
string res[30000];

void dfs(int k,int tar,string now) {
    if (k==tar) {
        ans=now;
        return;
    }

    for (auto i:e[k]) dfs(i.first,tar,now+i.second);
}

int main() {
    int n=256;
    ifstream lanly("word.txt");
    freopen("ans.txt","wb",stdout);
    int enter=0;
    while (true) {
        getline(lanly,tem);
        if (lanly.eof()) break;
        ch+=tem;
        enter++;
    }

    int L=ch.length();
    for (int i=0;i<L;i++) cnt[ch[i] + 0]++;
    cnt[13]+=enter;
    for (int i=0;i<=2*L;i++) if (cnt[i]==0) cnt[i]=-1;
    int m=n;
    for (int i=1;i<m;i++) {
        int M1=L+1,p=-1;
        for (int j=0;j<n;j++) {
            if (cnt[j]==-1) continue;
            if (cnt[j]<M1) {M1=cnt[j];p=j;}
        }

        int M2=L+1,q=-1;
        for (int j=0;j<n;j++) {
            if (cnt[j]==-1 || j==p) continue;
            if (cnt[j]<M2) {M2=cnt[j];q=j;}
        }

        if (p==-1 || q==-1) break;
        cnt[n]=M1+M2;
        printf("%d %d %d\n",n,p,q);
        e[n].push_back({p,"0"});
        e[n].push_back({q,"1"});
        cnt[p]=-1;cnt[q]=-1;
        n++;
    }

    n--;
    for (int i=0;i<m;i++) {
        ans="";
        dfs(n,i,"");
        res[i]=ans;
        //cout << ans << endl;
    }
    for (int i=0;i<L;i++) cout<<res[ch[i]];
    for (int i=0;i<enter;i++) cout<<res[13];

    return 0;
}

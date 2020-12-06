#include <bits/stdc++.h>
using namespace std;

const int maxn=1e5+10;
char ch[maxn];
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
    scanf("%s",ch);
    int L=strlen(ch);

    for (int i=0;i<L;i++) cnt[ch[i]]++;
    for (int i=0;i<=2*L;i++) if (cnt[i]==0) cnt[i]=-1;
    int m=n;
    for (int i=1;i<m;i++) {
        int M1=L+1,p=0;
        for (int j=0;j<n;j++) {
            if (cnt[j]==-1) continue;
            if (cnt[j]<M1) {M1=cnt[j];p=j;}
        }

        int M2=L+1,q=0;
        for (int j=0;j<n;j++) {
            if (cnt[j]==-1 || j==p) continue;
            if (cnt[j]<M2) {M2=cnt[j];q=j;}
        }

        cnt[n]=M1+M2;
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
    }
    for (int i=0;i<L;i++) cout<<res[ch[i]];

    return 0;
}

#include <iostream>
using namespace std;

int main() {
  int t;
  cin>>t;
  while(t--){
    long long x1,y1,x2,y2;
    cin>>x1>>y1>>x2>>y2;
    long long d1=abs(x1)+abs(y1);
    long long d2=abs(x2)+abs(y2);
    bool b=(((x1 > 0 && x2 > 0) || (x1 < 0 || x2 < 0))&&((y1 > 0 && y2>0)||(y1<0&&y2<0)));
    if (b){
      if(d1<d2){
        cout<<"YES"<<'\n';
      }
      else{
        cout<<"NO"<<'\n';
      }
    } 
    else{
      if(d1<=d2){
        cout<<"YES"<<'\n';
      }
      else{
        cout<<"NO"<<'\n';
      }
    }
  }
  return 0;
}


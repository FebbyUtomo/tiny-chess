import json,os,urllib.request as Q
S="AAAAUVWSCHFL=EAE;BCC;CB>9C?8AAAA14..@?Z8CRASGGLJABIF=CDG;=AA/;;;2--.>FJ7?K9KGEFIDCEGEGGEFFDC?A=>JHIBOHORFJHIABED:8=<7:7;479;9;=BCA?'EIP?ALIPA=GE==A@9?>>8=A<799>BOM(9COO1D3L3MD@364:576-@B=5EI@="
V=(50,140,160,239,464,30000);T={}
for n,k in enumerate('PNBRQK'):
 t=[0]*120
 for r in range(8):
  for f in range(8):t[21+f+10*r]=V[n]+ord(S[n*32+r*4+min(f,7-f)])-65
 T[k]=tuple(t)
D={'P':(-10,-20,-11,-9),'N':(-21,-19,-12,-8,8,12,19,21),'B':(-11,-9,9,11),'R':(-10,-1,1,10),'Q':(-11,-10,-9,-1,1,9,10,11)}
D['K']=D['Q']
ML=23955;MU=34650;CAP=150000;ND=0;Y={}
class X(Exception):pass
def g(p):
 b,s,w,c,e,k=p
 for i,x in enumerate(b):
  if x not in 'PNBRQK':continue
  for d in D[x]:
   j=i+d
   while 1:
    q=b[j]
    if q in ' \nPNBRQK':break
    if x=='P':
     if d in(-10,-20)and q!='.':break
     if d==-20 and(i<81 or b[i-10]!='.'):break
     if d in(-11,-9)and q=='.'and j not in(e,k,k-1,k+1):break
     if 21<=j<=28:
      for r in 'NBRQ':yield(i,j,r)
      break
     yield(i,j,'');break
    yield(i,j,'')
    if x in 'PNK'or q in 'pnbrqk':break
    if i==91 and b[j+1]=='K'and w[0]:yield(j+1,j-1,'')
    if i==98 and b[j-1]=='K'and w[1]:yield(j-1,j+1,'')
    j+=d
def v(p,m):
 b,s,w,c,e,k=p;i,j,r=m;x,y=b[i],b[j];t=T[x][j]-T[x][i]
 if y in 'pnbrqk':t+=T[y.upper()][119-j]
 if abs(j-k)<2:t+=T['K'][119-j]
 if x=='P':
  if 21<=j<=28:t+=T[r][j]-T['P'][j]
  if j==e:t+=T['P'][119-(j+10)]
 return t
def mv(p,m):
 b,s,w,c,e,k=p;i,j,r=m;x=b[i];l=list(b);nw=(w[0] and i!=91,w[1] and i!=98);nc=(c[0] and j!=28,c[1] and j!=21);ne=0;nk=0;sc=s+v(p,m);l[j]=x;l[i]='.'
 if x=='K':
  nw=(0,0)
  if abs(j-i)==2:nk=(i+j)//2;rr=91 if j<i else 98;l[rr]='.';l[nk]='R'
 if x=='P':
  if 21<=j<=28:l[j]=r
  if j-i==-20:ne=i-10
  if j==e:l[j+10]='.'
 nb=''.join(l);return(nb[::-1].swapcase(),-sc,nc,nw,119-ne if ne else 0,119-nk if nk else 0)
def se(p,d,a,be):
 global ND
 ND+=1
 if ND>CAP:raise X
 if p[1]<=-ML:return -MU
 kk=p[0:1]+p[2:];e=Y.get(kk);tm=e and e[3]
 if e and e[0]>=d and(e[2]==0 or e[2]==1 and e[1]>=be or e[2]==2 and e[1]<=a):return e[1]
 if d<=0:
  st=p[1]
  if st>=be:return be
  if st>a:a=st
  for m in g(p):
   if p[0][m[1]] in 'pnbrqk'or m[1]==p[4] or abs(m[1]-p[5])<2:
    s=-se(mv(p,m),0,-be,-a)
    if s>=be:return be
    if s>a:a=s
  return a
 if d>=3:
  q=(p[0][::-1].swapcase(),-p[1],p[3],p[2],0,0)
  s=-se(q,d-3,-be,-be+1)
  if s>=be:return be
 best=-MU;bm=None;ao=a
 for _,m in sorted(((v(p,m)+(99999 if m==tm else 0),m) for m in g(p)),reverse=True):
  s=-se(mv(p,m),d-1,-be,-a)
  if s>best:best=s;bm=m
  if s>a:a=s
  if a>=be:break
 if best==-MU:
  q=p[0][::-1].swapcase(),-p[1],p[3],p[2],0,0;best=-ML if any(q[0][m[1]]=='k' or abs(m[1]-q[5])<2 for m in g(q)) else 0
 Y[kk]=(d,best,(best>=be)+2*(best<=ao),bm)
 return best
def rt(p,rms):
 global ND
 ND=0;best=rms[0]
 for d in range(1,99):
  try:
   bs=-MU;bm=None
   for m in rms:
    s=-se(mv(p,m),d-1,-MU,MU)
    if s>bs:bs=s;bm=m
   best=bm
  except X:break
 return best
def pf(f):
 p=f.split();c=p[2];r=''
 for a in p[0].split('/'):r+=' '+''.join('.'*int(h) if h.isdigit() else h for h in a)+'\n'
 b='         \n'*2+r+'         \n'*2;t=0
 for i,h in enumerate(b):
  if h.isalpha():t+=T[h][i] if h.isupper() else -T[h.upper()][119-i]
 e=ord(p[3][0])+4-10*int(p[3][1]) if p[3]!='-' else 0
 if p[1]=='w':return(b,t,('Q' in c,'K' in c),('k' in c,'q' in c),e,0)
 return(b[::-1].swapcase(),-t,('k' in c,'q' in c),('Q' in c,'K' in c),119-e if e else 0,0)
def uc(m,bl):
 i,j,r=m
 if bl:i,j=119-i,119-j
 return chr((i-91)%10+97)+str(1-(i-91)//10)+chr((j-91)%10+97)+str(1-(j-91)//10)+r.lower()
def po(u,pa,o):
 try:return json.load(Q.urlopen(u+pa,json.dumps(o).encode()))
 except Exception:return{}
def main():
 u=os.getenv('MAKEFUN_ENV_URL','')
 while 1:
  e=po(u,'/game',{})
  if 'fen' not in e or e.get('status')=='finished':break
  lg=e.get('legal_moves') or []
  if not lg:break
  bl=e.get('colour')=='black';p=pf(e['fen']);ls=set(lg)
  rms=[m for m in g(p) if uc(m,bl) in ls]
  m=rms[0] if len(rms)==1 else rt(p,rms);w=uc(m,bl)
  po(u,'/move',{'game':e.get('game'),'move':w})
 return 0
main()


n=8

king,st,sq = input().split()



move = {
    'RT': (1,1),
    'T':  (1,0),
    'LT': (1,-1),
    'L': (0,-1),
    'R':(0,1),
    'LB':(-1,-1),
    'B':(-1,0),
    'RB':(-1,1)
}

kx= (ord(king[0])-65)
ky= (int(king[1])-1)
sx= (ord(st[0])-65)
sy= (int(st[1])-1)





for p in range(int(sq)):

    mo=move.get(input())
    kmy = ky + mo[0]
    kmx = kx + mo[1]
    
    if 0>kmy or kmy >= 8 or 0>kmx or kmx >=8:
        continue
    elif 0<=kmy or kmy < 8 or 0<=kmx or kmx <8:
            if kmy == sy and kmx == sx:
                smy = sy + mo[0] 
                smx = sx + mo[1]
                if 0>smy or smy >= n or 0>smx or smx >=n:
                    continue
                elif 0<=smy or smy < 8 or 0<=smx or smx <8:
                    sy = smy
                    sx = smx 
                    ky =kmy
                    kx =kmx
            else:
                ky =kmy
                kx =kmx

print (chr(kx+65),ky+1,sep='')
print (chr(sx+65),sy+1,sep='')

#
n=8

king,st,sq = input().split()



move = {
    'RT': (1,1),
    'T':  (1,0),
    'LT': (1,-1),
    'L': (0,-1),
    'R':(0,1),
    'LB':(-1,-1),
    'B':(-1,0),
    'RB':(-1,1)
}

kx= (ord(king[0])-65)
ky= (int(king[1])-1)
sx= (ord(st[0])-65)
sy= (int(st[1])-1)





for p in range(int(sq)):

    mo=move.get(input())
    kmy = ky + mo[0]
    kmx = kx + mo[1]
    
    if 0>kmy or kmy >= 8 or 0>kmx or kmx >=8:
        continue
    elif 0<=kmy or kmy < 8 or 0<=kmx or kmx <8:
            if kmy == sy and kmx == sx:
                smy = sy + mo[0] 
                smx = sx + mo[1]
                if 0>smy or smy >= n or 0>smx or smx >=n:
                    continue
                elif 0<=smy or smy < 8 or 0<=smx or smx <8:
                    sy = smy
                    sx = smx 
                    ky =kmy
                    kx =kmx
            else:
                ky =kmy
                kx =kmx

print (chr(kx+65),ky+1,sep='')
print (chr(sx+65),sy+1,sep='')






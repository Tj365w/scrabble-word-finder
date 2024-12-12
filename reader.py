ref={'e' :24, 'a' :16, 'o' :15, 't' :15, 'i' :13, 'n' :13, 'r' :13, 's' :10, 'l' :7, 'u' :7
    ,'d' :8, 'g' :5
    , 'c' :6, 'm' :6, 'b' :4, 'p' :4
    , 'h' :5, 'f' :4, 'w' :4, 'y' :4, 'v' :3
    , 'k' :2
    , 'j' :2, 'x' :2
    ,'q' :2, 'z' :2}

def main():
    def sortSecond(val):
        return val[1] 

    def assort(i):
            probab=0 
            for j in i:
                probab+=ref[j]
            l.append((i,probab))

    def mtc(patt):
                for m in d: 
                    if re.search(patt,m) and len(m)<=7:
                        assort(m)

    def reassign(d):
        for i in d:
            if reg[i]>0:
                ref[i]-=1

    t=open('words_dictionary.json','rb')
    import time
    import re
    import json
    t.seek(0)
    d=json.load(t)
    m=int(input('enter mode , 0 for auto search, ').strip() or 0)
    p=input('enter search,  ') or '^a'
    start_time = time.time()
    l=[]



    if not m:
        for i in range(len(p)):
            for j in range(len(p)-i):
                patt=re.escape(p[i])
                if not p[i]==p[j]:
                    p+=re.escape(p[j])
                mtc(patt)
    else:
        mtc(p)

    l=list(set(l))

    l.sort(key=sortSecond,reverse=True)
    r=int(input(f'enter range, default 100, max 10k, full length {len (l)}  ').strip() or 100)
    print(' ')
    for i in range(r):
        try:
            print(f'{l[i][0]}',end='\t'*2)
        except:
            continue
    print('')
    print("--- %s seconds ---" % (time.time() - start_time))
    reassign(input('letters used now by all players, '))
    t.close()
    print(ref)
    main()
main()
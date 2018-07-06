key=[73, 90, 75, 10, 67, 92, 65, 80, 65, 75, 85, 93, 67, 13, 70, 64, 65, 1, 92, 6, 1, 89, 91, 14, 90, 82, 65, 93, 8, 94, 6]
f=[]
flag={}
def isgood(k):
    if k>47 and k<58:
        return True
    elif k>96 and k<123:
        return True
    else:
        return False
def func():
    for iii in range(10):
        if iii==0:
            tmp1=[]
            tmp2=[]
            tmp3=[]
            tmp4=[]
            for i in range(48,128):
                for j in range(48,128):
                    for k in range(48,128):
                        for z in range(48,128):
                            if i^key[iii]==j^key[iii+10]==k^key[iii+20]== z^key[iii+30] and isgood(i) and isgood(j) and isgood(k) and isgood(z):
                                tmp1.append(chr(i))
                                tmp2.append(chr(j))
                                tmp3.append(chr(k))
                                tmp4.append(chr(z))
                                
                                #flag=True
                                #break
            flag[iii]=tmp1
            flag[iii+10]=tmp2
            flag[iii+20]=tmp3
            flag[iii+30]=tmp4
        else:
            tmp1=[]
            tmp2=[]
            tmp3=[]
            for i in range(48,128):
                for j in range(48,128):
                    for k in range(48,128):
                        if i^key[iii]==j^key[iii+10]==k^key[iii+20] and isgood(i) and isgood(j) and isgood(k):
                            tmp1.append(chr(i))
                            tmp2.append(chr(j))
                            tmp3.append(chr(k))
            flag[iii]=tmp1
            flag[iii+10]=tmp2
            flag[iii+20]=tmp3
    answer='1499419583'
    tmp=''
    ffff={}
    for j in range(10):
        for i in range(len(flag[j])):
            if chr(ord(flag[j][i])^key[j])==answer[j]:
                ffff[j]=flag[j][i]
                ffff[j+10]=flag[j+10][i]
                ffff[j+20]=flag[j+20][i]
                break
    ffff[30]=flag[30][0]
    aa=''
    for i in range(31):
        aa+=ffff[i]
    print(aa)
if __name__=='__main__':
    print('begin...')
    func()
    
                        

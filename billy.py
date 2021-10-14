qq = str(input('输入一个十进制浮点数'))
l = qq.split('.')
front = int(l[0])#这是小数点前的数
latter = l[1]#这是小数点后的数（均为十进制）a

#首先定义sign        #注意：-0,+0转化为整数时会去掉符号
if qq.find('-') == -1:
    sign = str(0)
else:
    sign = str(1)# sign是S
    if str(front).find('-')==0:
        front=int(str(front).replace('-',''))
    else:
        pass
#第二步定义front
if front!=0:
    x = int(bin(front)[2:])  # 取小数点前的数并转化为二进制并消除0b
    abc = str(float(x)).find('.')
    abc = abc - 1 + 127
    abc = bin(abc)[2:].zfill(8)  # abc是E
    # latter
    a = int(latter) / 10 ** len(latter)#int是把第一个不是0的数转化
    s = ''
    while a != 1.0 and len(s) < 23:
        a = a * 2
        s += str(a)[0]
        if a > 1:
            a -= 1
        elif 0 < a < 1:
            a = a
        elif a == 1:
            a = 1.0
    l = float('0.' + s) + int(x)  # x是front的二进制结果，s是latter的二进制结果
    l = list(str(l / (10 ** (str(l).find('.') - 1))))
    lc=''.join(l)
    if lc.find('9')!=-1:
        x2 = l.count('9')
        i = 1
        while i in range(1, x2 + 1):
            l.remove('9')
            i += 1
        l1 = ''.join(l)#join函数括号内是列表
        l1 = str(float(l1)) + '1'
        l1 = l1[2:]  # l1为M未填0的结果
        all = sign + abc + l1
        all = all + (32 - len(all)) * '0'
    else:
        l2=''.join(l)[2:]
        all = sign + abc + l2
        all = all + (32 - len(all)) * '0'
elif front==0:
    a = int(latter) / 10 ** len(latter)
    s = ''
    while a != 1.0 and len(s) < 23:
        a = a * 2
        s += str(a)[0]
        if a > 1:
            a -= 1
        elif 0 < a < 1:
            a = a
        elif a == 1:
            a = 1.0
    s1='0.'+s
    s2=1-s1.find('1')+127
    abc=bin(s2)[2:].zfill(8)#abc是E
    #M
    s3=10**(s1.find('1')-1)
    s4=str(float(s1)*s3)
    M1=s4[2:]
    all=sign+str(abc)+M1
    all=all+'0'*(32-len(all))
print(all)


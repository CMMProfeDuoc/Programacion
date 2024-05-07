fibo = []
for i in range(int(input(">> "))):
    if ((i==0) or (i==1)):
        fibo.append(1)
    else:
        sig_num = fibo[i-1] + fibo[i-2]
        fibo.append(sig_num)
    print(fibo[i])

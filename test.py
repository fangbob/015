def hanoi(circle,towerA,towerB,towerC):
    if(circle > 1):    #環大於1個時
        hanoi(circle-1,towerA,towerC,towerB)    #把A塔頂部的n-1塊環移到B塔，再把A塔剩下的環移到C塔
        print(str(circle) + "號環 " + towerA + " -> " + towerC)
        hanoi(circle-1,towerB,towerA,towerC)    #把B塔的n-1塊環移到C塔
    else:
        print(str(circle) + "號環 " + towerA + " -> " + towerC)    #把A塔的環移到C塔
num = int(input("請輸入環數："))    
hanoi(num,"A","B","C")

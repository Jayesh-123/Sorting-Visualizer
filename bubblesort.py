import time
def bubble_sort(data,drawData,timeTick):
    for i in range(len(data)-1):
        for j in range(len(data)-1):
            if(data[j]>data[j+1]):
                data[j],data[j+1]=data[j+1],data[j]
                drawData(data,['red' if x==j or x==j+1 else 'cyan' for x in range(len(data))])
                time.sleep(timeTick)
    drawData(data,["green2" for i in range(len(data))])
                

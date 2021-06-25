import time

def selection_sort(data,drawData,timeTick):
    for i in range(len(data)): 
        min_idx = i 
        for j in range(i+1, len(data)): 
            if data[min_idx] > data[j]: 
                min_idx = j

        data[i], data[min_idx] = data[min_idx], data[i] 
        drawData(data,['blue' if x==min_idx else 'pink' for x in range(len(data))])
        time.sleep(timeTick)
    drawData(data,["green2" for i in range(len(data))])
  


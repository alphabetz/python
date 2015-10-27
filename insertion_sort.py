import time
def insertion_sort(list):
    startTime = time.time()
    for index in range(len(list)):
        value = list[index]
        i = index - 1
        while i >= 0 and value < list[i]:
                list[i+1],list[i] = list[i], value
                i = i - 1
    elapsedTime = time.time() - startTime
    print elapsedTime

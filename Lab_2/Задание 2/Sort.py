import random
import time
#Shell Sort Algorithm
def shellSort(data, length):
    gap = length//2
    while gap > 0:            
        for i in range(gap, length):
            temp = data[i]
            j = i
            while(j >= gap and data[j - gap] > temp):
                data[j] = data[j - gap]
                j -= gap   
            data[j] = temp
        gap //= 2
    

def quickSort(nums):
    if len(nums) <= 1:
        return nums
    else:
        q = random.choice(nums)
        s_nums = []
        m_nums = []
        e_nums = []
        for n in nums:
            if n < q:
                s_nums.append(n)
            elif n > q:
                m_nums.append(n)
            else:
                e_nums.append(n)
        return quickSort(s_nums) + e_nums + quickSort(m_nums)

data1 = []
for i in range(100000):
    data1.append(random.randint(0,10000))
for i in range(100000):
    data1.append(i)
for i in range(100000):
    data1.append(100000 - i)
data2 = data1.copy()
data3 = data1.copy()

#print(data1[5],'',data2[5],'',data3[5])
start_time = time.time() 
shellSort(data1,len(data1))
print("--- %s seconds ---" % (time.time() - start_time))


start_time = time.time() 
quickSort(data2)
print("--- %s seconds ---" % (time.time() - start_time))


start_time = time.time()
data3.sort()
print("--- %s seconds ---" % (time.time() - start_time))


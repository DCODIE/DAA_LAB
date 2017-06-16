def bubble_sort(seq):
    j=0
    while j<len(seq)-1:
        for i in range(len(seq) - 1):
            if seq[i] > seq[i+1]:
                seq[i], seq[i+1] = seq[i+1], seq[i]
        j+=1
    print (seq)
import random,time
alist=[random.randint(0,100) for i in range(10)]
start=time.time()
bubble_sort(alist)
end=time.time()
print(end-start,"Seconds")
print(alist)
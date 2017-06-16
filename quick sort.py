def qsort(list):
    if not list:
        return []
    else:
        pivot = list[0]
        less = [x for x in list if x <pivot]
        more=[x for x in list if x>pivot]
        return qsort(less) + [pivot] + qsort(more)
import random,time
alist=[random.randint(0,100) for i in range(10)]
print(alist)
start=time.time()
print(qsort(alist))
end=time.time()
print((end-start),"Seconds")
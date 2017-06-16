def total_value(items, max_weight):
    return  sum([x[2] for x in items]) if sum([x[1] for x in items]) <= max_weight else 0
cache = {}
def knapsack(items, max_weight):
    if not items:
        return ()
    if (items,max_weight) not in cache:
        head = items[0]
        tail = items[1:]
        include = (head,) + knapsack(tail, max_weight - head[1])
        dont_include = knapsack(tail, max_weight)
        if total_value(include, max_weight) > total_value(dont_include, max_weight):
            answer = include
        else:
            answer = dont_include
        cache[(items,max_weight)] = answer
    return cache[(items,max_weight)]
items=((1,3,10),(2,5,4),(3,6,9),(4,2,11))
max_weight = 7
x= (knapsack(items,max_weight))
print("The items are",x)
print("The number of items are",len(x))
total_weight=sum([a[1] for a in x])
total_value=sum([a[2] for a in x])
print("The total weight is {0} and the total value is {1}.".format(total_weight,total_value))


from bisect import *
class Interval(object):
    def __init__(self, title, start, finish, weight):
        self.title = title
        self.start = int(start)
        self.finish = int(finish)
        self.weight = weight
    def __repr__(self):
        return str((self.title, self.start, self.finish, self.weight))
def compute_previous_intervals(I):
    start = [i.start for i in I]
    finish = [i.finish for i in I]
    p = []
    for j in range(len(I)):
        i = bisect(finish, start[j]) - 1  # rightmost interval f_i <= s_j
        p.append(i)
    return p
def schedule_weighted_intervals(I) :
    I.sort(key=lambda x: x.finish - x.finish)  # f_1 <= f_2 <= .. <= f_n
    p = compute_previous_intervals(I)
    OPT = {}
    OPT[-1] = 0
    OPT[0] = 0
    for j in range(1, len(I)):
        OPT[j] = max(I[j].weight + OPT[p[j]], OPT[j - 1])
    O = []
    def compute_solution(j):
        if j >= 0:  # will halt on OPT[-1]
            if I[j].weight + OPT[p[j]] > OPT[j - 1]:
                O.append(I[j])
                compute_solution(p[j])
            else:
                compute_solution(j - 1)
    compute_solution(len(I) - 1)
    return O
I = []
I.append(Interval("1", "1", "2", 100))
I.append(Interval("2", "2", "5", 200))
I.append(Interval("3", "3", "6", 300))
I.append(Interval("4", "4", "8", 400))
I.append(Interval("5", "5", "9", 500))
I.append(Interval("6", "6", "10", 100))
O = schedule_weighted_intervals(I)
print (O)

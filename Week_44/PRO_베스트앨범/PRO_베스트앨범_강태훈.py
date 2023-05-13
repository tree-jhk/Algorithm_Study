from heapq import heappush, heappop

def solution(genres, plays):
    hqdict = {}
    sumval = {}
    for idx, (g,p) in enumerate(zip(genres, plays)):
        sumval[g] = sumval.get(g, 0) + p
    for idx, (g,p) in enumerate(zip(genres, plays)):
        if g not in hqdict:
            hqdict[g] = []
        heappush(hqdict[g], [-p, -sumval[g], idx])
    answer = []
    for info in sorted(hqdict.values(), key=lambda x:x[0][1]):
        answer.append(heappop(info)[2])
        if info:
            answer.append(heappop(info)[2])
    return answer

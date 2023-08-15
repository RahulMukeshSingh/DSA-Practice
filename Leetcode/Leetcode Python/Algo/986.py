def intervalIntersection(firstList, secondList):
    ans = []
    for first in firstList:
        for second in secondList:
            if first[1] < second[0]: break;
            if second[1] >= first[0]:
                ans.append([max(first[0],second[0]),min(first[1],second[1])])
    return ans     


print(8+6+2+5+4+8+3+7)
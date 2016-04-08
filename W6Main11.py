def FindingYoonNyeon(year):

    if(year%4 == 0) and (year%100 !=0 or year%400==0):
        res="YoonNyeon"
    else:
        res="PyeongNyeon"
    return res

result=FindingYoonNyeon(2016)
print result

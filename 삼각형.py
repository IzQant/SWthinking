def solution(A):
    answer = 0
    a = max(A)
    b = min(A)

    for i in range(1,2005) :
        if ( a + b > i and i >= a ) or ( b+i>a and a>=i ):
            answer+=1

    return answer
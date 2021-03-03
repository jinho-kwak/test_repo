def solution(a, b):
    day = ['THU', 'FRI', 'SAT', 'SUN', 'MON', 'TUE', 'WED']
    mon = [31,29,31,30,31,30,31,31,30,31,30,31]
    answer = ''
    tmp = 0
    if a == 1:
        return day[b % 7]    
    for i in range(a-1):
        tmp += mon[i]
    answer = day[(tmp + b) % 7]
    return answer
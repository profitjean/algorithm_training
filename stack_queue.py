# 프로그래머스 스택큐
# 기능 개발

def solution(progresses, speeds):
    
    date = []
    time = 0 
    count = 0
    
    while len(progresses) > 0:
        if progresses[0] + time*speeds[0] >= 100:
            progresses.pop(0)
            speeds.pop(0)
            count = count + 1
        else:
            if count > 0:
                date.append(count)
                count = 0
            time = time + 1
            
    date.append(count) #마지막에 while문 탈출 이후에 작동
    return date
        
        
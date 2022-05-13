# 카카오 17년도 기출

# n회, t분 간격, 한 셔틀에 최대 m명 탑승가넝
def solution(n, t, m, timetable):
    busTime = []
    for idx, time in enumerate(timetable): # enumerate - idx, 요소값 분리
        hour, minute = time.split(':')
        timetable[idx] = int(hour) *60 + int(minute) # 시/분 단위에서 분단위로 변환
    timetable.sort()
    for i in range(n):
        busTime.append(9*60+t*i) # 버스 시간, 첫차는 오전 9시니까 540분 기준으로.

    i = 0 # 버스에 탈 크루의 인덱스
    for bt in busTime:
        cnt = 0 # 버스에 탑승 가능한 크루
        while cnt < m and i<len(timetable) and timetable[i] <= bt:
            i += 1
            cnt += 1
        if cnt < m: # 버스에 자리가 남았으면 내가 타면 된당
            answer = bt
        else:
            answer = timetable[i-1]-1 # 자리가 없으면 마지막에 도착한 사람보다 1분 빨리 도착하기

    return str(answer//60).zfill(2) + ":" + str(answer%60).zfill(2)
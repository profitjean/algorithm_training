# 카카오 19년도 기출
def solution(record):
    answer = []
    name_list = {}
    for word in record:
        k = word.split()
        if k[0] == 'Enter':
            name_list[k[1]] = k[2]
        if k[0] == 'Change':
            name_list[k[1]] = k[2]
    # 딕셔너리로 {id:닉네임} 형태로 저장하게끔
    # 아이디 변경된것까지 반영시켜주
    # 이후 record for문으로 Enter/Leave 여부기 저장
    # for문 2번..이게 맞냐? 근데 히든케이스까지 다 통과
    # 효율성이 아쉬움
    for word in record:
        k = word.split()
        if k[0] == 'Enter':
            answer.append(name_list[k[1]]+'님이 들어왔습니다.')
        if k[0] == 'Leave':
            answer.append(name_list[k[1]]+'님이 나갔습니다.')
    return answer
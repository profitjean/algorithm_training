# 진열된 모든 종류의 보석을 적어도 1개 이상 포함하는 가장 짧은 구간을 찾아서 구매한다
# 가장 짧은 구간의 시작 번호와 끝 번호를 차례대로 배열에 담아서 return
# 짧은 구간이 여러개라면, 시작 진열대 번호가 가장 작은 구간을 return

def solution(gems):
    answer = []
    shortest = len(gems) + 1

    start_p = 0
    end_p = 0

    check_len = len(set(gems))  # 보석의 총 종류
    contained = {}  # 구간별 포함된 보석의 개수 보여주기

    while end_p < len(gems):  # 구간의 끝 점이 gem길이보다 작은동안
        if gems[end_p] not in contained:
            contained[gems[end_p]] = 1
        else:
            contained[gems[end_p]] += 1
        end_p += 1

        if len(contained) == check_len:  # 필요한 보석을 다 포함하고 있다면?
            while start_p < end_p:  # start_p가 end_p보다 같을때까지 증가
                # end_p 기준으로 start_p 한칸씩 땡겨오기
                if contained[gems[start_p]] > 1:
                    contained[gems[start_p]] -= 1
                    start_p += 1
                elif shortest > end_p - start_p:
                    shortest = end_p - start_p  # 최단 거리 갱신하기
                    answer = [start_p + 1, end_p]
                    break
                else:
                    break
    return answer
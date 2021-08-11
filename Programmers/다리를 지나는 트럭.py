def solution(bridge_length, weight, truck_weights):
    
    count = 0 # 건너가는데 걸리는 소요시간
    arr = bridge_length * [0] # 다리 길이만큼 배열을 생성
    current = 0 # 현재 다리 위의 무게의 합

    while True:
        current = current - arr.pop() # 맨 뒤의 트럭부터 내보내기
        
        if (truck_weights[0] + current) <= weight: # 다리 하중이 있으므로 건너는 차의 무게를 제한
            arr.insert(0, truck_weights.popleft()) 
				# arr 배열의 0번에 넣고자하는 값을 삽입 -> insert()의 기능;원하는 위치에 원하는 값 삽입
				# 트럭 무게를 저장한 리스트 중 맨 앞을 pop
				# 참고) pop(0)으로 대체해도 동일하다고 함
            current = current + arr[0]
        else:
            arr.insert(0, 0)
            
        count += 1 

        if len(truck_weights) == 0:
            break

    return count + bridge_length # 지금까지 걸린 시간 + 마지막 트럭이 다리를 건너는 시간 합하기
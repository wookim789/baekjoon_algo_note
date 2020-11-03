# N : 배열 길이
# M : 더하는 횟수
# K : 같은 인덱스의 수를 연속해서 더 할 수 있는 횟수


# 지금 고를수 있는 가장 큰수를 고른다.
# K번 더한다. (k <= M)

# M번 이상 초과하지 않았을 경우
# 다음으로 큰 수를 골라 더한다.

# 만약 현재 고른 수보다 더 큰수가 있다면 
# 더 큰수를 K번 더한다.



# 베열 내림차순 정렬
# 첫 인덱스 K번 더하기
# 다음 인덱스 1번 더하기
# 처음 인덱스와 다음 인덱스 크기 비교
# 처음 인덱스가 더 크다면 
# 처음 인덱스 K번 더하기
# 총 더한 횟수가 m번이면 더한값 리턴

if __name__ == "__main__":
    condition = [5,8,3]

    l = condition[0]
    m = condition[1]
    k = condition[2]

    arr = [2, 4, 5, 4, 6]


    arr.sort(reverse=True)

    # 6, 5, 4, 4, 2 

    # 총 합
    result = 0

    # 더하는 횟수 제한 <= M
    countIdx = 0

    # 연속 더하는 횟수 제한 <= K
    sumIdx = 0

    idx = 0
    while idx < l:
        if countIdx < m:
            if sumIdx < k :
                result += arr[idx]
                countIdx += 1
                sumIdx += 1
                if idx > 0:
                    idx -= 1
                    sumIdx = 0
            elif sumIdx == k:
                sumIdx = 0
                idx += 1
        else :
            break

    print(result)


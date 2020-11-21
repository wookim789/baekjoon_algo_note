# 뮤직 dvd

# n개의 음악, m개의 cd
n, m = map(int, input().split())
# 각 음악의 길이
m_arr = list(map(int, input().split()))

# m개의 cd의 최소 용량으로 
# 모든 음원을 순서에 맞게 나누어 저장한다.

# 모든 음원을 m개의 cd에 저장 가능한 최소 용량을 구한다.

# 가장 쉽게 구할수 있는 답은
# 1. 음악길의 총합으로 용량을 잡는다. -> 1개의 cd에 전부 저장
answer = sum(m_arr)
# 2. 점차 용량을 줄여가며 적절한 용량을 찾아간다
# 이분 탐색의 while문 조건
st, ed = 0, answer
while st <= ed:
    # print(st, ed)
    mid = (st + ed) // 2
    # m을 넘어서면 실패
    m_cnt = 1
    tmp_sum = 0

    for i in m_arr:
        tmp_sum += i
        if m_cnt <= m and tmp_sum < mid:
            continue
        elif m_cnt < m and tmp_sum >= mid and i <= mid:
            m_cnt += 1
            tmp_sum = i
        elif i > mid:
            tmp_sum = 1e9
            break
        elif m_cnt > m:
            break
        else:
            tmp_sum = 1e9
    if m_cnt <= m and tmp_sum <= mid:
        answer = mid
        ed = mid - 1
    else:
        st = mid + 1

print(answer - 1)
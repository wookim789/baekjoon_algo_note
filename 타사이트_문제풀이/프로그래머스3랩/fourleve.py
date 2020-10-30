# 과자를 바구니 단위로 파는 가게가 있습니다. 이 가게는 1번부터 N번까지 차례로 번호가 붙은 바구니 N개가 일렬로 나열해 놨습니다.

# 철수는 두 아들에게 줄 과자를 사려합니다. 첫째 아들에게는 l번 바구니부터 m번 바구니까지, 둘째 아들에게는 m+1번 바구니부터 r번 바구니까지를 주려합니다. 단, 두 아들이 받을 과자 수는 같아야 합니다(1 <= l <= m, m+1 <= r <= N). 즉, A[i] 를 i번 바구니에 들어있는 과자 수라고 했을 때, A[l]+..+A[m] = A[m+1]+..+A[r] 를 만족해야 합니다.

# 각 바구니 안에 들은 과자 수가 차례로 들은 배열 cookie가 주어질 때, 조건에 맞게 과자를 살 경우 한 명의 아들에게 줄 수 있는 가장 많은 과자 수를 return 하는 solution 함수를 완성해주세요. (단, 조건에 맞게 과자를 구매할 수 없다면 0을 return 합니다)

# 제한사항
# cookie의 길이는 1 이상 2,000 이하입니다.
# cookie의 각각의 원소는 1 이상 500 이하인 자연수입니다.  ㅂ

def solution(cookie):
    n = len(cookie)
    
    if n == 1:
        return 0

    dp_table = [0] * n
    result = []
    # dp_table[e] - dp_table[f] == dp_table[f] result.append()
    dp_table[0] = cookie[0]
    for i in range(1, n):
        dp_table[i] = dp_table[i - 1] + cookie[i]
    # print(dp_table)
    
    
    is_change_dir = None
    for i in range(1, n + 1):
        for j in range(i):
            l = j
            r = n - i + j
            m = (r - l) // 2
            while True:
                l_tum = 0
                if l != 0:
                    l_tum = dp_table[l-1]
                    
                # print(dp_table[m] - l_tum, dp_table[r] - dp_table[m], end = " : ")
                if l > m or m > r:
                    break
                if dp_table[m] - l_tum == dp_table[r] - dp_table[m]:
                    result.append(dp_table[m] - l_tum)
                    break

                elif dp_table[m] - l_tum > dp_table[r] - dp_table[m]:
                    m -= 1
                    if is_change_dir == None or is_change_dir:
                        is_change_dir = True
                    else:
                        break

                elif dp_table[m] - l_tum < dp_table[r] - dp_table[m]:
                    m += 1
                    if is_change_dir == None or not is_change_dir:
                        is_change_dir = False
                    else:
                        break
        if result:
            return max(result)
    max_v = 0
    if result:
        max_v = max(result)
    return max_v

# 정확성: 24.4
# 효율성: 10.5
# 합계: 34.9 / 50
# 모험가 길드
# 1
# 30분 
# 1초 128mb


# 모험가 n 
# 공포도 x

# 조건 
# x 공포도가 x인 모험가 -> x명 이상으로 구성한 모험가 그룹에 참여

# 최대 최대 몇개의 그룹을 만들 수 있는가

# 공포도 순 -> 내림차순 정렬
# 공포도 가장 높은 사람 뽑기
# x -1 명 만큼 뽑기 -> 조합


from collections import Counter

n = int(input())

x_arr = list(map(int, input().split()))
x_arr.sort()
count = 0

# 공포도가 1인 녀석부터 그룹으로 만들기
# 공포도가 2인 녀석 2명으로 그룹 만들기
# 공포도가 3인 녀석 ,,,

# 남은 인원중 가장 작은 공포도와 남은 인원수 확인하여 모자르면 end

pear = 0

count_map = dict(Counter(x_arr))
key_list = list(count_map.keys())
key_list.sort()

heap = 0
count = 0
for i in key_list:
    cur_tot = count_map[i] + heap

    count += cur_tot // i
    heap = cur_tot % i
    

# 몫 나누고 나눈 나머지는 더큰 애들에 숫자를 더해 준다

# 46분 32초 - 16분 32초 초과
# 문제 : 문제를 제대로 읽지 않음
# -> 시간초과
# 헛짓말고 문제를 제대로 읽고
# 최종족으로 구해야하 하는 답을 제대로 파악해야 한다
# 감으로 읽지말것
# 제댜로 파악하고 글로 써둘것
print(count)
# 우선선위 큐
import heapq

heap = []

heapq.heappush(heap, (3, 2))
heapq.heappush(heap, (1, 3))
heapq.heappush(heap, (4, 5))
heapq.heappush(heap, (6, 2))
heapq.heappush(heap, (7, 1))
heapq.heappush(heap, (9, 8))
heapq.heappush(heap, (2, 9))

# 원소로 튜플을 넣었다면 리스트를 출려해도 정렬되진 않고
print(heap)

# pop을 했을떄 정렬되어 나온다
for i in range(len(heap)):
    print(heapq.heappop(heap))

# pop 후엔 삭제되니 유의
print('heap',heap)
print()
arr = []
arr1 = [1]
if arr :
    print(0)
if arr1:

    print(1)
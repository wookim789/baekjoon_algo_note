	# 5, [[1, 0, 0, 1], [1, 1, 1, 1], [2, 1, 0, 1], [2, 2, 1, 1], [5, 0, 0, 1], [5, 1, 0, 1], [4, 2, 1, 1], [3, 2, 1, 1]]

def solution(n, build_frame):
    list_map = [[0]* n for _ in range(n)]
    result = []
    for fr in build_frame:
        # x, y 좌표, 
        # cd 기둥:0  보:1 
        # build_type 삭제:0 설치:1
        x, y, cd, build_type  = fr
        
        # 설치
        if build_type == 1:
            # 기둥
            if cd == 0:
                # 기둥 위
                if [x, y - 1, 0] in result:
                    result.append([x, y, cd])
                # 보 위
                elif [x - 1, y, 1] in result:
                    result.append([x, y, cd])
                # 땅 위
                elif y == 0:
                    result.append([x, y, cd])
            # 보
            else:
                # 기둥 위 왼쪽에서 
                if [x, y-1, 0] in result :
                    result.append([x, y, cd])
                elif [x-1, y-1,0] in result:
                    result.append([x, y, cd])
                # 기둥 위 오른쪽에서 
                elif [x+1, y-1, 0] in result :
                    result.append([x, y, cd])
                # 보 와 보 사이를 동시에 연결
                elif [x -1, y, 0] in result and [x + 1, y, 0] in result:
                    result.append([x, y, cd])
        # 삭제
        else:
            # 기둥 삭제
            if cd == 0:
                if [x, y, cd] in result:
                    idx = 0
                    for i in result:
                        if i == [x,y,cd]:
                            break
                        idx += 1
                    # 못지우는 사례 
                    # 1자 기중의 중간 빼기
                    if not( ([x, y-1, 0] in result and [x, y-1, 1] not in result) and ([x, y+1,0] in result and [x,y+1,1] not in result)):
                        del result[idx]
                    # 보 보 로 연결된 보 긑에 기둥 뺴기
                    elif not ([x, y+1, 1] in result and [x+1, y+1, 1] in result and [x+1, y, 0] not in result):
                        del result[idx]
                    elif not ([x, y+1,1] in result and [x-1, y+1, 1] in result and [x-1, y, 0] not in result):
                        del result[idx]
                    # [x-1, y-1, cd] in result or [x+1, y-1, cd] in result:
            # 보 삭제
            else :
                if [x, y, cd] in result:
                    idx = 0
                    for i in result:
                        if i == [x,y,cd]:
                            break
                        idx += 1
                    if not ([x-1, y, cd] in result and [x+1,y,cd] in result):
                        del result[idx]
    result.sort(key=lambda x: x[1])
    result.sort()
    print(result)
    return result
# solution(5, [[1, 0, 0, 1], [1, 1, 1, 1], [2, 1, 0, 1], [2, 2, 1, 1], [5, 0, 0, 1], [5, 1, 0, 1], [4, 2, 1, 1], [3, 2, 1, 1]] ) 
# print([[1,0,0],[1,1,1],[2,1,0],[2,2,1],[3,2,1],[4,2,1],[5,0,0],[5,1,0]])
solution(	5, [[0, 0, 0, 1], [2, 0, 0, 1], [4, 0, 0, 1], [0, 1, 1, 1], [1, 1, 1, 1], [2, 1, 1, 1], [3, 1, 1, 1], [2, 0, 0, 0], [1, 1, 1, 0], [2, 2, 0, 1]]) 
print([[0, 0, 0], [0, 1, 1], [1, 1, 1], [2, 1, 1], [3, 1, 1], [4, 0, 0]])









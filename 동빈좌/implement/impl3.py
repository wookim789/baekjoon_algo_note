

if __name__ == "__main__":

    input_data = input()

    # 좌우 2칸 -> 상하 1칸
    # 상하 2칸 -> 좌우 1칸


    y = int(input_data[1])
    x = ord(input_data[0]) - ord('a') + 1

    # 경로 관련 문제에서 이동 경로의 경우의 수가 많지 않다면
    # 아래 처럼 이동 방법의 경우의 수를 배열로 만드는 방법을 고려해볼것
    step_list = [(-2, -1), (-2, 1), (2, -1), (2, 1), (-1, -2), (1, -2), (-1, 2), (1, 2)]

    result = 0 

    for step in step_list:
        dx = x + step[0]
        dy = y + step[1]

        if 1 <= dx and dx <= 8 and 1 <= dy and dy <= 9:
            result += 1
    print(result)
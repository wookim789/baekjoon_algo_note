from collections import deque
answer = []
    
ball, orders = 	[11, 2, 9, 13, 24], [9, 2, 13, 24, 11]
# deque 사용

# 조건
# 중간공이 빠져나오지 못했다
# 이후 명령부터 수행 하다가
# 중간공이 빠져나올수 있다면 먼저 뺀다

# 명령은 큐에 쌓는다

# 공이 빠져나오는 순서를 리턴한다

ball_deque = deque(ball)

ball = None
order_ques = deque()

# 2중 포문으로 최상위 order 그 안은 ord_que 로 이룬다

    for order in orders:
        order_ques.append(order)
        print("append oq:", order_ques)
        # 대기중인 명령이 있다면
        idx = 0
        while idx < len(order_ques):
            # print(idx)
            if len(ball_deque) == 0 or len(order_ques) == 0:
                break
            # ball에 앞 뒤 확인
            if ball_deque[0] == order_ques[idx]:
                answer.append(order_ques[idx])
                ball_deque.popleft()
                if idx == 0:
                    order_ques.popleft()
                else:
                    order_ques.remove(order_ques[idx])
                idx = -1
                # print("앞 제거 bq:", ball_deque)
                # print("앞 제거 oq:", order_ques)
            elif ball_deque[-1] == order_ques[idx]:
                answer.append(order_ques[idx])
                ball_deque.pop()
                if idx == 0:
                    order_ques.popleft()
                else:
                    order_ques.remove(order_ques[idx])
                idx = -1
                # print("뒤 제거 bq:", ball_deque)
                # print("앞 제거 oq:", order_ques)
            idx += 1
        if len(ball_deque) > 0 and ball_deque[0] == order:
            answer.append(order)
            ball_deque.popleft()
            order_ques.pop()
            # print("_앞 제거 bq:", ball_deque)
            # print("_뒤 제거 oq:", order_ques)
        elif len(ball_deque) > 0 and ball_deque[-1] == order:
            answer.append(order)
            ball_deque.pop()
            order_ques.pop()
            # print("_뒤 제거 bq:", ball_deque)
            # print("_뒤 제거 oq:", order_ques)

print('result:', answer)
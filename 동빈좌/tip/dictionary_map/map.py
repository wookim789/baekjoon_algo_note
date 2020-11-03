
# python에서 map은 dictionary로 칭함

# 선언
dictionary = dict()
dictionary = {"key1": 1}

# 추가
dictionary["key2"] = 2

print(dictionary)

# 읽기
print("key1:", dictionary["key1"]) # key 없을 시 예외
print("key1:", dictionary.get("key1")) # key 없을 시 None 리턴

# 삭제
del dictionary["key1"]

# print(dictionary["key1"]) # key 없을 시 예외
print("del key1:", dictionary.get("key1")) # key 없을 시 None 리턴



# dictionay에서 key 있는지 조사 탐색 시 O(1)
if "key2" in dictionary:
    print("if hash key2 : ", dictionary["key2"])


# key의 리스트 반환받고 싶을떄
key_list = list(dictionary.keys())
print("key list: ",key_list)

# 키 리스트를 반환하는건 오버에드이기에 추천하지 않는다
# 키를 순회해야 한다면
# 아래처럼 사용할 것
print("key list:", end =' ')
for key in dictionary.keys():
    print(key, end = ' ')

print()
print("items")

# key와 value를 쌍으로 가져오고 싶을 때
for key, value in dictionary.items():
    print('key:', key, ' value:', value)
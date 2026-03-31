# 파일이름 : main.py
# 작 성 자 : 강현민, 3.31

#미션 3
bucket_list = []

food = input('맛집 리스트 입력: ')
bucket_list.append(food)

food = input('맛집 리스트 입력: ')
bucket_list.append(food)

food = input('맛집 리스트 입력: ')
bucket_list.append(food)

print(f'리스트: {bucket_list}\n')

vip_food = input('맛집 리스트 입력: ')
bucket_list.insert(0, vip_food)
print(f'리스트: {bucket_list}\n')

today_food = input('도장 깨기: ')
bucket_list.remove(today_food)

print(f'리스트: {bucket_list}')
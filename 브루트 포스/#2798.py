#블랙잭 문제
#N장의 카드에 써져 있는 숫자가 주어졌을 때, M을 넘지 않으면서 M에 최대한 가까운 카드 3장의 합을 구해 출력하시오.


from itertools import combinations

card_num, target_num = map(int,input().split())
card_list = list(map(int,input().split()))

big_num = 0

for cards in combinations(card_list,3):
    if big_num < sum(cards) <=target_num:
        big_num = sum(cards)
print(big_num)
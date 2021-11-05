a = int(input())
b = int(input())

#a, b => 각각 세 자리수 자리수별로 쪼갠 리스트
b_split = list(str(b))
li = []
for i in range(3):
    int_i = int(b_split.pop())
    li.append(int_i)
print(li)

print(a*li[-3]) #ans_3
print(a*li[-2]) #ans_4
print(a*li[-1]) #ans_5
print(a*li[-1]*100 + a*li[-2]*10 + a*li[-3]) #ans_6
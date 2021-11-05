a, b = map(str, input().split())

re_a = list(a)
re_b = list(b)

re_a.reverse()
re_b.reverse()

reverse_a =int("".join(re_a))
reverse_b =int("".join(re_b))
if reverse_a < reverse_b:
    print(reverse_b)
else:
    print(reverse_a)
year = int(input())

def yoon_year(year):
    if year % 4 == 0 and (year % 100 !=0 or year % 400 == 0):
        print(1)
    else:
        print(0)

yoon_year(year)
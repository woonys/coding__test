-- 코드를 입력하세요
SELECT HOUR(DATETIME) AS hour, count(HOUR(DATETIME))
from ANIMAL_OUTS
where HOUR(DATETIME) <= 19 and 9<= HOUR(DATETIME)
group by hour
order by hour
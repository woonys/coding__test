-- 코드를 입력하세요
SELECT NAME, count(name)
from ANIMAL_INS
group by NAME
having count(name) >=2
order by name
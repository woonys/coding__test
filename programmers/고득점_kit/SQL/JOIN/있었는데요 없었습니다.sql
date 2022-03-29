-- 코드를 입력하세요
SELECT outs.ANIMAL_ID, outs.NAME
from ANIMAL_OUTS outs
left outer join ANIMAL_INS ins
on outs.ANIMAL_ID = ins.animal_id
where outs.datetime<=ins.datetime
order by ins.datetime
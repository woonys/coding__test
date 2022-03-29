-- 코드를 입력하세요
SELECT outs.ANIMAL_ID, outs.NAME
from ANIMAL_OUTS outs -- 입양 간 기록(out)은 존재한다 했으니 out이 왼쪽에 와야 한다.
left outer join ANIMAL_INS ins -- 붙이려는 애는 오른쪽에 오니까 join 뒤에 온다.
on outs.ANIMAL_ID=ins.ANIMAL_ID
where ins.ANIMAL_ID is null -- ins의 animal id에 없는 애들만 불러온다.
order by outs.ANIMAL_ID
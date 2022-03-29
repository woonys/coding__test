-- 코드를 입력하세요
SELECT outs.animal_id, outs.animal_type, outs.name
from animal_outs outs
left outer join animal_ins ins
on outs.animal_id=ins.animal_id
where (outs.sex_upon_outcome like'Spayed%'
OR outs.sex_upon_outcome like 'Neutered%')
AND ins.SEX_UPON_INTAKE like 'Intact%'
order by outs.animal_id

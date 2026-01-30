
select d.nombre_departamento,
count(e.id_empleado) as cantidad_emplados,
avg(e.salario) as promedio_salario,
sum(e.salario) as total_salario
from departamentos as d
left  join empleados as e on (d.id_departamento=e.id_departamento)
where e.salario > 1000000  -- filtrando por registro
group by d.nombre_departamento
having sum(e.salario) < 2000000 -- filtrar por agrupacion
;
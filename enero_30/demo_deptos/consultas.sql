
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
-- Obtener los nombres de los empleados y sus salarios que 
-- trabajan en el mismo departamento que
-- el empleado con id_empleado = 3.

select nombre,apellido,salario
from empleados
where id_departamento = (select id_departamento
						   from empleados
						  where id_empleado=3) ;
-- Obtener el nombre del departamento y el nombre del 
-- empleado con el salario más alto en cada departamento.

select e1.nombre,e1.apellido,  d.nombre_departamento
from 
	(
	select id_departamento,  max(e2.salario) as salario_max
	from empleados e2
	group by id_departamento
	) as resultado
inner join empleados as e1 on (e1.id_departamento = resultado.id_departamento 
								and e1.salario=resultado.salario_max)
inner join departamentos as d on (d.id_departamento=e1.id_departamento);
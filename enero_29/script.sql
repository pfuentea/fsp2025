-- 1.Obtener el nombre y apellido de los empleados que trabajan en el departamento con nombre
"Ventas".

select nombre,apellido
from empleados
where id_dapartamento = ( select id_departamento
							from departamentos
							where nombre_departamento='Ventas' )

-- 2. Obtener los nombres de los empleados y sus salarios que trabajan en el mismo departamento
-- que el empleado con “id_empleado” igual a 2.
select nombre, salario
from empleados
where id_departamento = (select id_departamento
						from empleados
						where id_empleado=2
						)

-- 3. Recupera el nombre del empleado cuya ubicación sea igual a Chile
select nombre
from empleados
where id_departamento in ( select id_departamento
							from departamentos
							where ubicacion='Chile')

-- 4. Recupera los nombres de los empleados cuyo “id_departamento” sea igual a 1.
-- By Karina
SELECT nombre
FROM empleados
WHERE id_departamento = 1;



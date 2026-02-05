INSERT INTO empleados (nombre, apellido, salario, fecha_ingreso, departamento)
VALUES
('Yerco', 'Arancibia', 83000, '2021-05-12', 'IT'),
('Yuri', 'Leal', 76000, '2022-08-01', 'Finanzas'),
('Constanza', 'Fica', 70000, '2023-03-18', 'Marketing'),
('Jocelyne', 'Arancibia', 68000, '2024-01-10', 'RRHH'),
('Sandra', 'Fuentes', 74000, '2022-11-05', 'Ventas');


-- Aumenta un 7 % a quienes ganen < 80 000.
update empleados
set salario= salario * 1.07
where salario < 80000 ;
-- Suma 5 000 fijos a los que tengan > 3 años de antigüedad.

update empleados2
set salario = salario + 5000
where fecha_ingreso < CURRENT_DATE - INTERVAL '3 years';

-- Cambia a Sofía Ruiz al departamento Ventas.

update empleados2
set departamento = (
		Select id_departamento
		from departamentos2
		where nombre_departamento = 'Ventas'
		)
where nombre = 'Sofía' and apellido = 'Ruíz';


UPDATE empleados
SET departamento = 'Ventas'
WHERE nombre = 'Sofia' AND apellido = 'Ruiz';

UPDATE empleados 
SET departamento = 'Gerencia'
WHERE nombre ='Karina' and apellido = 'De Armas'  ;

DELETE FROM empleados
WHERE departamento = 'Recursos Humanos';

DELETE FROM empleados
WHERE departamento = 'RRHH';

-- ATENCION !!!!
DROP → destruye todo
TRUNCATE → borra todo rápido (instántaneo)
DELETE sin WHERE → vacía tablas
UPDATE sin WHERE → arruina datos 
ALTER TABLE → cambios estructurales peligrosos

-- IMPORTANTE
NO USAR DELETE O UPDATE SIN WHERE


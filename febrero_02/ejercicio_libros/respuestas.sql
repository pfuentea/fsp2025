-- Muestra titulo, nombre_genero, autor (nombre + apellido) 
-- y nombre_editorial de cada libro,
-- uniendo las cuatro tablas con INNER JOIN.

select l.titulo, g.nombre_genero,
a.nombre || ' ' || a.apellido as nombre_autor,
e.nombre_editorial
from libros as l
inner join autores as a On (a.id_autor=l.id_autor)
inner join editoriales as e on (e.id_editorial=l.id_editorial)
inner join generos as g on (g.id_genero=l.id_genero);


-- Lista los géneros que no tienen ningún libro asociado. 
-- Usa un LEFT JOIN de Generos contra Libros y
-- filtra donde Libros.id_genero sea NULL.
insert into generos(nombre_genero) VALUES
('Religión');
SELECT   g.nombre_genero , g.id_genero
	FROM generos as g      -- desde donde sacar la informacion
		left join libros as l on ( g.id_genero =l.id_genero)
	WHERE l.id_genero is  null

SELECT g.* , l.id_genero,l.titulo  -- que columnas mnostrar
FROM generos as g      -- desde donde sacar la informacion
	left join libros as l on ( g.id_genero =l.id_genero)
WHERE g.id_genero=3   -- las condiciones para filtrar
  and (titulo like 'A%' OR titulo like 'E%')


select resultado.*, l2.titulo
from (
	SELECT   g.nombre_genero , 'No existe libro asociado' as descripcion, 0.19 as iva, g.id_genero
	FROM generos as g      -- desde donde sacar la informacion
		left join libros as l on ( g.id_genero =l.id_genero)
	WHERE l.id_genero is not null
	group by g.nombre_genero, g.id_genero
	)  resultado
inner join libros as l2 on (resultado.id_genero= l2.id_genero)

-- solucion 1 para sacar repetidos
SELECT   g.nombre_genero , 'No existe libro asociado' as descripcion, 0.19 as iva, g.id_genero
	FROM generos as g      -- desde donde sacar la informacion
		left join libros as l on ( g.id_genero =l.id_genero)
	WHERE l.id_genero is not null
	group by g.nombre_genero, g.id_genero

--solucion 2 para sacar repetidos

SELECT  distinct g.nombre_genero , 'No existe libro asociado' as descripcion, 0.19 as iva, g.id_genero
	FROM generos as g      -- desde donde sacar la informacion
		left join libros as l on ( g.id_genero =l.id_genero)
	WHERE l.id_genero is not null
	


-- Conteo de libros por autor (incluyendo 0)
INSERT INTO autores (nombre, apellido) VALUES
('Patricio', 'Fuentealba')


-- AL USAR GROUP BY TODAS LAS COLUMNAS QUE NO TENGAN UNA FUNCION DE AGRUPACION
-- DEBEN IR EN EL GROUP BY
select a.nombre,a.apellido, count(l.id_libro) as cant_libros  , count(a.id_autor)  as otro_count_INCORRECTO
from autores as a
left join libros as l on (l.id_autor=a.id_autor)
where 1=1 
-- condicion dinamica  AND CAMPO = OTRA_COSA
group by a.nombre,a.apellido


-- UNION 
select nombre, 100 as sueldo, 'dic' as mes from autores
union 
select nombre, 100 as sueldo, 'nov' as mes from autores



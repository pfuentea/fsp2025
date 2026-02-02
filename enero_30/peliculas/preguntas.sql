-- Obtener el título de todas las películas junto 
-- con el nombre del actor principal en cada una.
select p.titulo, 
pa.es_principal,pa.id_actor,
a.id_actor,
a.nombre, a.apellido
from peliculas as p
inner join peliculas_actores  as pa on (p.id_pelicula=pa.id_pelicula)
inner join actores as a on (pa.id_actor=a.id_actor)
where pa.es_principal = TRUE
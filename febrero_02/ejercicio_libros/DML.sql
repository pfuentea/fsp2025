- sintaxis de INSERT forma 1 , insertar 1 valor
-- INSERT INTO [TABLA] (COLUMNAS) VALUES (Los valores) ;
INSERT INTO autores (nombre,apellido) VALUES ('Patricio','Fuentealba');

-- sintaxis de INSERT forma 2 , insertar varios valores
-- INSERT INTO [TABLA] (COLUMNAS) VALUES (Los valores) , (otros_valores),
-- (otros_valores) , (otros_valores)  ;
INSERT INTO autores (nombre,apellido) VALUES ('Jocelyne','Arancibia'),('Gloria','Contreras');

select * from autores
-- sintaxis de UPDATE forma 1 , actualizar 1 columna
-- UPDATE  [TABLA] SET [CAMPO] = [VALOR] WHERE [CONDICION] 
UPDATE  autores SET nombre = 'Floripondio' WHERE id_autor=11;

-- sintaxis de UPDATE forma 2 , actualizar más de una columna
-- UPDATE  [TABLA] SET [CAMPO1] = [VALOR1], [CAMPO2] = [VALOR2],..., [CAMPO_N] = [VALOR_N]  
-- WHERE [CONDICION] 
UPDATE  autores SET nombre = 'Floripondio',apellido='Motuda' WHERE id_autor=11;

select * from autores

-- sintaxis de UPDATE forma 3 , actualizar con el valor de mismo u otro campo
-- UPDATE  [TABLA] SET [CAMPO1] = [CAMPO4], [CAMPO2] = [CAMPO1]*1.19  ,..., [CAMPO_N] = [VALOR_N]  
-- WHERE [CONDICION] ;
UPDATE  autores SET nombre = 'Muy '||apellido WHERE id_autor=11;
UPDATE  autores SET nombre = CONCAT('Muy','-',apellido ) WHERE id_autor=11;


select * from autores

-- sintaxis DELETE
-- DELETE FROM [TABLA] WHERE [CONDICION] ;
DELETE 
--select *
from autores
WHERE id_autor=11;

select * from autores
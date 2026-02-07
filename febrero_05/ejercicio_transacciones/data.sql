INSERT INTO usuarios(nombre) 
VALUES ('Constanza'),('Gloria'),('Wladimir'),('Yuri'),('Francisco');

INSERT INTO transacciones (sender_user_id,receiver_user_id,monto)
-- (2,4,10000)
SELECT u1.user_id, u2.user_id , 10000
FROM usuarios as u1 , usuarios as u2 
WHERE u1.nombre='Gloria'
AND u2.nombre='Yuri';

-- posible soluciones para generar el registro 
-- de forma que no se rompa la integridad referencial

SELECT u1.user_id, u2.user_id , 10000
FROM usuarios as u1
JOIN usuarios as u2 on (u2.nombre='Yuri')
WHERE u1.nombre='Gloria';

SELECT u1.user_id, u2.user_id , 10000
FROM usuarios as u1 , usuarios as u2 
WHERE u1.nombre='Gloria'
AND u2.nombre='Yuri';

-- la consulta correcta para ver las transacciones


select t.id_transaccion,
u1.nombre as usuario_envia,
u2.nombre as usuario_recibe,
t.monto
from transacciones as t
INNER JOIN usuarios as u1 on (t.sender_user_id=u1.user_id)
INNER JOIN usuarios as u2 on (t.receiver_user_id=u2.user_id)
;

-- esto causa un error de integridad
INSERT INTO transacciones (sender_user_id,receiver_user_id,monto)
VALUES(5,19,29983);
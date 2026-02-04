
select -- t.*,
u1.nombre as emisor ,
u2.nombre as  receptor,
t.valor,
t.transaction_date
from transacciones as t
inner join usuarios as u1 on (t.sender_user_id=u1.user_id)
inner join usuarios as u2  on (t.receiver_user_id=u2.user_id)

;
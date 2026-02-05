CREATE TABLE usuarios (
    user_id INT PRIMARY KEY,
    nombre VARCHAR(100)
);

CREATE TABLE transacciones (
    id_transaccion INT PRIMARY KEY,
    sender_user_id INT,
    receiver_user_id INT,
    monto DECIMAL(10,2),
    FOREIGN KEY (sender_user_id) REFERENCES usuarios(user_id),
    FOREIGN KEY (receiver_user_id) REFERENCES usuarios(user_id)
);
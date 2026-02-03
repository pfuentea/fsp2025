CREATE TABLE usuarios (
    user_id SERIAL PRIMARY KEY,
    nombre VARCHAR(100),
    email VARCHAR(150),
    password VARCHAR(255),
    saldo DECIMAL(12,2),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE monedas (
    currency_id SERIAL PRIMARY KEY,
    currency_name VARCHAR(50),
    currency_symbol VARCHAR(10)
);

CREATE TABLE transacciones (
    transaction_id SERIAL PRIMARY KEY,
    sender_user_id INT REFERENCES usuarios(user_id),
    receiver_user_id INT REFERENCES usuarios(user_id),
    valor DECIMAL(12,2),
    transaction_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
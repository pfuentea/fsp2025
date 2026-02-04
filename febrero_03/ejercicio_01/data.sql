
INSERT INTO usuarios (nombre, email, password, saldo)
VALUES
('Ana', 'ana@correo.com', '1234', 50000),
('Juan', 'juan@correo.com', 'abcd', 30000),
('Maria', 'maria@correo.com', 'pass', 70000);

INSERT INTO monedas (currency_name, currency_symbol)
VALUES
('Peso Chileno', 'CLP'),
('Dólar Americano', 'USD'),
('Euro', 'EUR');

INSERT INTO transacciones (sender_user_id, receiver_user_id, valor)
VALUES
(1, 2, 10000),
(2, 3, 5000),
(3, 1, 15000);
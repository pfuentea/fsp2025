INSERT INTO clientes (nombre) VALUES
('Ana'),
('Luis');

INSERT INTO pedidos (id_cliente)
SELECT id_cliente FROM clientes WHERE nombre = 'Ana';

INSERT INTO pedidos (id_cliente)
SELECT id_cliente FROM clientes WHERE nombre = 'Luis';

INSERT INTO pedidos (id_cliente)
SELECT id_cliente FROM clientes WHERE nombre = 'Ana';
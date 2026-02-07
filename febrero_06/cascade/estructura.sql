CREATE TABLE clientes (
    id_cliente SERIAL PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL
);

CREATE TABLE pedidos (
    id_pedido SERIAL PRIMARY KEY,
    id_cliente INT NOT NULL,
    fecha_pedido DATE NOT NULL DEFAULT CURRENT_DATE,

    CONSTRAINT fk_pedidos_clientes1
        FOREIGN KEY (id_cliente)
        REFERENCES clientes(id_cliente)
        ON DELETE CASCADE
);
opcion 2: borra los pedidos si es que borro al cliente

CREATE TABLE pedidos2 (
    id_pedido SERIAL PRIMARY KEY,
    id_cliente INT NOT NULL,
    fecha_pedido DATE NOT NULL DEFAULT CURRENT_DATE,

    CONSTRAINT fk_pedidos_clientes
        FOREIGN KEY (id_cliente)
        REFERENCES clientes(id_cliente)
);
opcion 1: no permite si quiera borrar al cliente

CREATE TABLE pedidos3 (
    id_pedido SERIAL PRIMARY KEY,
    id_cliente INT  NULL,
    fecha_pedido DATE NOT NULL DEFAULT CURRENT_DATE,

    CONSTRAINT fk_pedidos_clientes
        FOREIGN KEY (id_cliente)
        REFERENCES clientes(id_cliente)
		ON DELETE SET NULL
);

opcion 3: los pedidos quedan y el cliente se borra
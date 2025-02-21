CREATE TABLE IF NOT EXISTS users (
  id SERIAL PRIMARY KEY,
  username VARCHAR UNIQUE NOT NULL,
  password VARCHAR NOT NULL,
  role VARCHAR NOT NULL 
);

CREATE TABLE IF NOT EXISTS toppings (
  id SERIAL PRIMARY KEY,
  name VARCHAR UNIQUE NOT NULL
);

CREATE TABLE IF NOT EXISTS pizzas (
  id SERIAL PRIMARY KEY,
  name VARCHAR UNIQUE NOT NULL
);

CREATE TABLE IF NOT EXISTS pizzas_toppings (
  id SERIAL PRIMARY KEY,
  pizza_id INTEGER NOT NULL,
  topping_id INTEGER NOT NULL,
  FOREIGN KEY (pizza_id) REFERENCES pizzas (id),
  FOREIGN KEY (topping_id) REFERENCES toppings (id)
);

INSERT INTO users(username, password, role) VALUES('pizzamindowner', 'password1', 'owner');
INSERT INTO users(username, password, role) VALUES('pizzamindchef', 'password2', 'chef');
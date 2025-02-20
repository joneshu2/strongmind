CREATE TABLE IF NOT EXISTS pizzas_toppings (
  id SERIAL PRIMARY KEY,
  pizza_id INTEGER NOT NULL,
  topping_id INTEGER NOT NULL,
  FOREIGN KEY (pizza_id) REFERENCES pizzas (id),
  FOREIGN KEY (topping_id) REFERENCES toppings (id)
);
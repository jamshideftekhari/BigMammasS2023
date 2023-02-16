-- delete Pizza;

-- update price 
select * from Pizza;
select PizzaName, Price from Pizza;
update Pizza set Price = 65 where PizzaName = 'Margherita';
-- update price
update Pizza set Pris = 82 where PizzaNavn = 'SOLE';
-- update price for 2 other pizzas 
-- add a kea pizza

-- Find alle pizzas less than 75 kr and betwwen 75 and 80.
select * from Pizza where price < 75;
select * from Pizza where price > 75 and price <80; 
-- find pizzas with price over 80


-- select 
select PizzaNavn from Pizza;
select PizzaNavn, Pris from Pizza;
-- get alle pizzas less than 70, and between 70 and 80
select PizzaNavn, Pris from Pizza where Pris<70;
select PizzaNavn, Pris from Pizza where Pris>70 and pris<80;
-- get all pizzas with bacon,
select * from Pizza where Ingredients Like '%bacon%';
select * from Pizza where Ingredients Not Like '%bacon%';
-- get all pizzas with  onion, egg
-- find vegeterian pizzas
-- find vegan Pizzas. 
select * from ingredients;
-- Delete ingredients;
select * from ingredients where IngredientClass = 'meet';
-- find fruits and herbs
-- find fruits less than 20
-- find meets less than 20
-- find fruits less than 20 and meet less than 20
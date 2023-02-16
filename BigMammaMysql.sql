create database BigMamma2023;
Use BigMamma2023; 

create table pizza(
pizzaId        int primary key,
pizzaName      text,
ingredients    text,
price          real );

create table customer(
customerId       int primary key,
customerName     text,
customerAddress  text,
PhoneNo          text,
Email            text  );

create table orders(
orderId          int primary key, 
customerId       int,
orderDate        text, 
orderStatus      text,
foreign key (customerId) references customer(customerId)
);

-- create table orderDetail()

create table ingredients(
ingId           int auto_increment primary key,
ingName         text,
ingType         text,
IngNumber       real)
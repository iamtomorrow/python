use bankmanagementsystem;

select * from customers;

create table customers (
	customer_id INT PRIMARY KEY auto_increment,
    customer_first_name VARCHAR(20),
    customer_second_name VARCHAR(20),
	customer_last_name VARCHAR(20),
    customer_birthdate date,
    customer_age INT,
    customer_country VARCHAR(20),
    customer_city VARCHAR(20),
    customer_phone VARCHAR(15),
    customer_email VARCHAR(30),
	date_became_customer date,
    customer_login_code VARCHAR(10),
	customer_username VARCHAR(20),
    customer_password VARCHAR(30)
);
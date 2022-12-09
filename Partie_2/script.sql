DROP DATABASE IF EXISTS brazil;

CREATE DATABASE IF NOT EXISTS brazil;

CREATE TABLE IF NOT EXISTS product(
   product_id VARCHAR(50),
   product_category_name VARCHAR(50),
   product_name_lenght INT,
   product_description_lenght INT,
   product_photos_qty INT,
   product_weight_g INT,
   product_length_cm INT,
   product_height_cm INT,
   product_width_cm INT,
   PRIMARY KEY(product_id)
);

CREATE TABLE IF NOT EXISTS order_customer(
   customer_id VARCHAR(50),
   customer_unique_id VARCHAR(50),
   customer_zip_code_prefix INT,
   customer_city VARCHAR(50),
   customer_state VARCHAR(50),
   PRIMARY KEY(customer_id)
);

CREATE TABLE IF NOT EXISTS geolocalisation(
   geolocation_zip_code_prefix INT,
   geolocation_lat DECIMAL(15,15),
   geolocation_lng DECIMAL(15,15),
   geolocation_city VARCHAR(50),
   geolocation_state VARCHAR(50),
   PRIMARY KEY(geolocation_zip_code_prefix)
);

CREATE TABLE IF NOT EXISTS orders(
   order_id VARCHAR(50),
   customer_id VARCHAR(50) NOT NULL,
   order_status VARCHAR(50),
   order_purchase_timestamp DATETIME,
   order_approved_at DATETIME,
   order_delivered_customer_date DATETIME,
   order_estimated_delivery_date DATETIME,
   PRIMARY KEY(order_id),
   FOREIGN KEY(customer_id) REFERENCES order_customer(customer_id)
);

CREATE TABLE IF NOT EXISTS sellers(
   seller_id VARCHAR(50),
   seller_zip_code_prefix INT,
   seller_city VARCHAR(50),
   seller_state VARCHAR(50),
   PRIMARY KEY(seller_id),
   FOREIGN KEY(seller_zip_code_prefix) REFERENCES geolocalisation(geolocation_zip_code_prefix)
);

CREATE TABLE IF NOT EXISTS order_payments(
   order_id VARCHAR(50),
   payment_sequential INT,
   payment_type VARCHAR(50),
   payment_installments INT,
   payment_value DECIMAL(15,2),
   order_id_1 VARCHAR(50) NOT NULL,
   PRIMARY KEY(order_id),
   FOREIGN KEY(order_id) REFERENCES orders(order_id)
);

CREATE TABLE IF NOT EXISTS order_reviews(
   review_id VARCHAR(50),
   order_id VARCHAR(50) NOT NULL,
   review_score INT,
   review_comment_title VARCHAR(50),
   review_comment_message VARCHAR(50),
   review_creation_date DATETIME,
   review_answer_timestamp DATETIME,
   PRIMARY KEY(review_id),
   FOREIGN KEY(order_id) REFERENCES orders(order_id)
);

CREATE TABLE IF NOT EXISTS order_items(
   order_item_id INT,
   order_id VARCHAR(50) NOT NULL,
   product_id VARCHAR(50),
   seller_id VARCHAR(50),
   shipping_limit_date DATETIME,
   price DECIMAL(15,2),
   freight_value DECIMAL(15,2),
   PRIMARY KEY(order_item_id),
   FOREIGN KEY(seller_id) REFERENCES sellers(seller_id),
   FOREIGN KEY(order_id) REFERENCES orders(order_id),
   FOREIGN KEY(product_id) REFERENCES product(product_id)
);


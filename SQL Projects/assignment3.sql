#Julio Claros
#INST 327

#Question 1

SELECT category_name, COUNT(*) AS num_products, 
	ROUND(AVG(list_price), 2) AS avg_list_price, FORMAT(MAX(list_price), 2) AS max_list_price
FROM my_guitar_shop.categories JOIN my_guitar_shop.products 
	ON categories.category_id = products.category_id
GROUP BY category_name ASC WITH ROLLUP;

#QUESTION 2

SELECT product_name, description AS product_discription, 
	FORMAT(list_price, 2) AS product_list_price
FROM my_guitar_shop.products
WHERE list_price >
	(SELECT AVG(list_price)
	 FROM my_guitar_shop.categories JOIN my_guitar_shop.products 
		ON categories.category_id = products.category_id
	 WHERE category_name = "Basses")
ORDER BY list_price, product_name;

#QUESTION 3

SELECT email_address, COUNT(DISTINCT orders.order_id) AS order_count,
	FORMAT(SUM(item_price - discount_amount), 2) AS order_total,
    FORMAT(ROUND(SUM(item_price - discount_amount) / COUNT(DISTINCT orders.order_id), 2), 2) AS avg_order_total
FROM (my_guitar_shop.orders
	INNER JOIN my_guitar_shop.customers ON orders.customer_id = customers.customer_id
    INNER JOIN my_guitar_shop.order_items ON orders.order_id = order_items.order_id)
GROUP BY email_address
HAVING COUNT(DISTINCT orders.order_id) >
	(SELECT COUNT(customer_id)
	 FROM my_guitar_shop.orders
     GROUP BY customer_id
     HAVING COUNT(customer_id) < 2
     LIMIT 1);
     
# QUESTION 4

SELECT DISTINCT category_name
FROM my_guitar_shop.categories c
WHERE c.category_id IN
	(SELECT category_id
	 FROM my_guitar_shop.products p)
ORDER BY category_name;

#QUESTION 5

# No, you are selecting 2 columns from 2 separate tables, you need the join the be able to select them. 

#Trial and Error Code: 

#SELECT DISTINCT CONCAT(first_name, ' ', last_name) AS customer_name,
	#state AS customer_state
#FROM my_guitar_shop.customers c
#WHERE c.customer_id IN 
	#(SELECT customer_id
	 #FROM my_guitar_shop.addresses a)
#ORDER BY last_name, first_name;
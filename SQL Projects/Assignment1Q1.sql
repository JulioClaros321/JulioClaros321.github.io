SELECT CONCAT(customer_first_name, ' ' ,customer_last_name) AS customer_name,
	   CONCAT("Phone #:", ' ', customer_phone) AS customer_phone,
       CONCAT(customer_address, ", ", customer_city, ", ", customer_state, " ", customer_zip) AS customer_address
FROM om.customers AS peasants
WHERE customer_last_name > "L" AND customer_last_name < "T"
ORDER BY customer_last_name;

#Question 2
SELECT DISTINCT invoice_id, vendor_name, invoice_number, invoice_due_date, invoice_total-payment_total-credit_total AS balance_left, 
				if(invoice_total - payment_total - credit_total < 100, "low balance", "HIGH BALANCE") AS balance_level
FROM ap.invoices INNER JOIN ap.vendors 
ON invoices.vendor_id = vendors.vendor_id
WHERE payment_total = 0
ORDER BY invoice_due_date;


#Question 3
SELECT CONCAT(customer_first_name, " ", customer_last_name) AS customer_name, 
	    DATE_FORMAT(order_date, "%m/%Y") AS order_month, item_id
FROM ((om.orders 
LEFT OUTER JOIN om.customers ON orders.customer_id = customers.customer_id)
LEFT OUTER JOIN om.order_details ON orders.order_id = order_details.order_id)
WHERE customer_last_name > "P" AND customer_last_name < "T"
ORDER BY customer_last_name;

#Question 4
SELECT invoice_id, line_item_description, account_description, line_item_amount
FROM ap.invoice_line_items INNER JOIN ap.general_ledger_accounts
ON ap.invoice_line_items.account_number = ap.general_ledger_accounts.account_number
WHERE line_item_amount > 700 AND line_item_amount < 1200
ORDER BY line_item_description;
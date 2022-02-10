SELECT *
FROM ap.invoices
WHERE payment_total = 0
ORDER BY invoice_due_date ;
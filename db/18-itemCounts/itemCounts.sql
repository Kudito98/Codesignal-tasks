CREATE PROCEDURE solution()
BEGIN
	SELECT item_name, item_type, COUNT(item_name) AS item_count
	FROM availableitems
	GROUP BY item_name, item_type
	ORDER BY item_type, item_name
	;
END
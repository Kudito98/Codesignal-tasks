CREATE PROCEDURE solution()
BEGIN
	SELECT IFNULL(country, 'Total:') AS country , count(country) as competitors  
	FROM foreignCompetitors GROUP BY country WITH ROLLUP;
END
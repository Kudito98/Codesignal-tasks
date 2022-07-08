CREATE PROCEDURE solution()
BEGIN
	SELECT COUNT(name) AS number,
	SUM(population) / COUNT(name) AS average,
	sum(population) AS total
	FROM countries;
END
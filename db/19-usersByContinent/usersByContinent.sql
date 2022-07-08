CREATE PROCEDURE solution()
BEGIN
	SELECT continent, SUM(users) AS users
	FROM countries
	GROUP BY continent
	ORDER BY users DESC;
END
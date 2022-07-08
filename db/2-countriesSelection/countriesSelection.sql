CREATE PROCEDURE solution()
BEGIN
	SELECT name, continent, population FROM countries WHERE continent = "Africa";
END
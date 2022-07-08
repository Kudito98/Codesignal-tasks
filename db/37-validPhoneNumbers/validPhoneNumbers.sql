CREATE PROCEDURE solution()
BEGIN
	SELECT *
	FROM phone_numbers
	WHERE phone_number REGEXP '^(\\(1\\)|1-)([0-9]{3}-){2}[0-9]{4}$'
	ORDER BY surname;
END
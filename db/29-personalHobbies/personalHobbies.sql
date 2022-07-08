CREATE PROCEDURE solution()
BEGIN
	SELECT name 
	FROM people_hobbies
	WHERE hobbies & 3 = 3;
END
CREATE PROCEDURE solution()
BEGIN
	SELECT CONCAT(IF(gender = "F", "Queen ", "King "), name) AS name 
	FROM Successors
	ORDER BY birthday;
END
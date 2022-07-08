CREATE PROCEDURE solution()
BEGIN
	SELECT id, a, b, operation, c 
	FROM expressions 
	WHERE CASE operation 
	WHEN "+" THEN a + b 
	WHEN "-" THEN a - b 
	WHEN "*" THEN a * b 
	WHEN "/" THEN a / b 
	END = c;
END
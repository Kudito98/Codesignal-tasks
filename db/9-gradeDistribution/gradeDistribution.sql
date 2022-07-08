CREATE PROCEDURE solution()
BEGIN
	SELECT Name, ID 
	FROM Grades
	WHERE final > 0.25*Midterm1 + 0.25*Midterm2 + 0.50*Final AND final > 0.50*Midterm1 + 0.50*Midterm2 
	ORDER BY LEFT (Name, 3);
END
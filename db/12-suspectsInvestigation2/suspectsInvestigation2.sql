CREATE PROCEDURE solution()
BEGIN
	SELECT id, name, surname FROM Suspect WHERE height <= 170 OR LOWER(surname) NOT LIKE 'gre_n' OR name NOT LIKE 'B%';
END
CREATE PROCEDURE solution()
BEGIN
	SELECT IFNULL(SUM(salary=mas) * mas - SUM(salary=mis) * mis, 0) AS difference
    FROM employees, (SELECT MAX(salary) mas, MIN(salary) mis FROM employees) t;
END
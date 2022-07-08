CREATE PROCEDURE solution()
BEGIN
	SELECT dep_name
	FROM departments
	WHERE NOT EXISTS (
		SELECT department
		FROM employees
		WHERE department = departments.id
	)
	;
END
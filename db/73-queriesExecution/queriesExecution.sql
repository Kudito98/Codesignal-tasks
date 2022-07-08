CREATE PROCEDURE solution()
BEGIN
	SET @code = CONCAT(
    (SELECT 
         group_concat(
            concat('SELECT "',query_name,'" AS query_name, (', code,') AS val')
         SEPARATOR ' UNION ')
     FROM queries));

	PREPARE query from @code;
	EXECUTE query;
END
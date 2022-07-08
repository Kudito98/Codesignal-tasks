CREATE PROCEDURE solution()
BEGIN
   	SET @first := true;
    WHILE row_count() OR @first DO
        SET @first := false;
        UPDATE inheritance a
        JOIN inheritance b ON a.base = b.derived AND a.base != "Number"
        SET a.base = b.base;
    END WHILE;
    
    SELECT var_name, type AS var_type
    FROM variables JOIN inheritance ON type = derived
    WHERE base = "Number"
    ORDER BY var_name;
END
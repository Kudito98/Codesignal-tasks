CREATE PROCEDURE solution()
BEGIN
    DELETE FROM currencies
    WHERE LENGTH(code) <> 3;

    SELECT * FROM currencies ORDER BY code;
END

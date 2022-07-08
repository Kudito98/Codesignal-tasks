CREATE PROCEDURE solution()
BEGIN
	CREATE TABLE x (l char, n int); 

    SET @a = '`';
    WHILE '{' > @a:=char(ord(@a) + 1) DO
        INSERT INTO x 
            SELECT @a, 
                   length(str) - length(REPLACE(str, @a, "")) n 
                FROM strs 
                HAVING n;
    END WHILE;

    SELECT l letter,
           SUM(n) total,
           SUM(1) occurrence,
           MAX(n) max_occurrence,
           SUM(n = (SELECT MAX(n) FROM x WHERE l = y.l)) max_occurrence_reached
        FROM x y
        GROUP by 1;

    DROP TABLE x;
END
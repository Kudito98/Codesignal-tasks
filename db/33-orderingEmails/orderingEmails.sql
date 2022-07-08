CREATE PROCEDURE solution()
BEGIN
	SELECT id, email_title, 
	CASE
        WHEN size >= 1048576 THEN CONCAT(FLOOR(size / 1048576), ' Mb')
        ELSE CONCAT(FLOOR(size / 1024), ' Kb')
    END  AS short_size
	FROM emails
	ORDER BY size DESC;
END
CREATE PROCEDURE solution()
BEGIN
	SELECT DATE(date_str)
	AS date_iso
	FROM documents;
END
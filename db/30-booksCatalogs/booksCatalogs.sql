CREATE PROCEDURE solution()
BEGIN
	SELECT DISTINCT ExtractValue(xml_doc, '/catalog/book[1]/author') as author
    FROM catalogs
    ORDER BY author;
END
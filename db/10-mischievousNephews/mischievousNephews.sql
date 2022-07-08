CREATE PROCEDURE solution()
BEGIN
SELECT (DAYOFWEEK(mischief_date) + 5) % 7 as weekday, mischief_date, author, title 
FROM mischief
ORDER BY weekday, CASE author WHEN 'Huey' THEN 1 WHEN 'Dewey' THEN 2 WHEN 'Louie' THEN 3 END, mischief_date, title asc;
END
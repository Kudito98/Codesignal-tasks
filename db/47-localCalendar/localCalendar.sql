CREATE PROCEDURE solution()
BEGIN
	SELECT event_id, DATE_FORMAT(DATE_ADD(date, INTERVAL timeshift minute), 
	IF(hours=24 ,'%Y-%m-%d %H:%i', '%Y-%m-%d %h:%i %p')) AS formatted_date
    FROM events NATURAL JOIN settings
    ORDER BY event_id;
END
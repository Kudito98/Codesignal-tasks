CREATE PROCEDURE solution()
BEGIN
	SELECT DISTINCT anonymous_id AS 'anonym_id',
    (SELECT event_name FROM tracks b 
	WHERE b.anonymous_id = a.anonymous_id AND b.user_id IS NULL 
	ORDER BY received_at DESC LIMIT 1) AS 'last_null',
    (SELECT event_name FROM tracks b 
	WHERE b.anonymous_id = a.anonymous_id AND b.user_id IS NOT NULL 
	ORDER BY received_at ASC LIMIT 1) AS 'first_notnull'
    FROM tracks a ORDER BY a.anonymous_id;
END
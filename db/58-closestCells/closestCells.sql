CREATE PROCEDURE solution()
BEGIN
	SELECT p1.id id1, (
		SELECT id FROM positions p2
		WHERE p1.id != p2.id
		ORDER BY power(p1.x-p2.x,2) + power(p1.y-p2.y,2) LIMIT 1) AS id2
	FROM positions p1;
END
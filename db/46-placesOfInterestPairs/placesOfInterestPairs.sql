CREATE PROCEDURE solution()
BEGIN
       SELECT s1.name AS place1, s2.name AS place2
       FROM sights s1 CROSS JOIN sights s2
       WHERE s1.name < s2.name AND POWER(s1.x - s2.x, 2) + POWER(s1.y - s2.y, 2) < 25
       ORDER BY place1, place2;
END
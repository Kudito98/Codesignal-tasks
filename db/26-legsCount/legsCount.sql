DROP PROCEDURE IF EXISTS solution;
CREATE PROCEDURE solution()
    SELECT SUM(CASE WHEN type = "human" then 2 ELSE 4 END) as summary_legs
    FROM creatures
    ORDER BY id;

CREATE PROCEDURE solution()
BEGIN
	SELECT
        ELT(d, name_naughts, name_crosses) name,
        SUM((r=d)*2 + (r=3)) points,
        SUM(1) played,
        SUM(r=d) won,
        SUM(r=3) draw,
        SUM(r=3-d) lost
    FROM
        (SELECT
            *,
            IF(board RLIKE '^(...)*XXX|X..(X|.X.)..X|^..X.X.X', 2, 
                LENGTH(REPLACE(board, '.', ''))%2*2+1
            ) r
        FROM results) x,
        (SELECT 1 d UNION SELECT 2) b
    GROUP BY 1
    ORDER BY 2 DESC, 3, 5,1;
END
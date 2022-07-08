CREATE PROCEDURE solution()
BEGIN
	SELECT director
	FROM moviesinfo
	WHERE year > 2000
	GROUP BY director HAVING SUM(oscars) > 2
	ORDER BY director;
END
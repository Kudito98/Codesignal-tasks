CREATE PROCEDURE solution()
BEGIN
	SELECT actor_ages.*
    FROM 
        actor_ages
        JOIN starring_actors USING(actor)
        JOIN movies ON movie_name = movie
        JOIN (
            SELECT genre
            FROM movies
            GROUP BY genre
            ORDER BY COUNT(*) DESC
            LIMIT 1
        )best_genre USING(genre)
    ORDER BY age DESC, actor;
END
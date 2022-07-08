CREATE PROCEDURE solution()
    SELECT * FROM students
    WHERE EXISTS (
        SELECT id
        FROM clubs
        WHERE students.club_id = id
    )
    ORDER BY students.id;

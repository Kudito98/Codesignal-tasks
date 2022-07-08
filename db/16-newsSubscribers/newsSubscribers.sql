CREATE PROCEDURE solution()
BEGIN
    SELECT subscriber
	FROM (

        SELECT subscriber FROM full_year WHERE newspaper LIKE '%Daily%'

        UNION

        SELECT subscriber FROM half_year WHERE newspaper LIKE '%Daily%'    

        ) as t

    ORDER BY subscriber;
END
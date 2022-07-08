CREATE PROCEDURE solution()
BEGIN
        SELECT @a alarm_date
        FROM userInput, 
             (SELECT 1 UNION SELECT 2 UNION SELECT 3 UNION SELECT 4) x,
             (SELECT 1 UNION SELECT 2 UNION SELECT 3 UNION SELECT 4) y,
             (SELECT 1 UNION SELECT 2 UNION SELECT 3 UNION SELECT 4) z
        WHERE year(ifnull(@a:=date_add(@a, INTERVAL 1 week), @a:=input_date)) 
            = year(input_date);
END

CREATE PROCEDURE solution()
BEGIN
	SELECT  id, 
    IF(SUM(expenditure_sum)-value <0, 0, SUM(expenditure_sum)-value) AS loss
    FROM allowable_expenditure ae 
    CROSS JOIN
        (SELECT monday_date, 
                week(monday_date, 3) AS weeknum,
                expenditure_sum
         FROM expenditure_plan 
         ) ep 
    ON 1 = 1
    WHERE ep.weeknum BETWEEN ae.left_bound AND ae.right_bound
    GROUP BY ae.id 
    ORDER BY ae.id;
END
CREATE PROCEDURE solution()
BEGIN
	SELECT b.title bug_title,
           c.title component_title,
           (SELECT sum(1) FROM BugComponent WHERE component_id=id) bugs_in_component
        FROM Bug b, Component c, BugComponent
        WHERE bug_num=num 
              && component_id=id
              && (SELECT sum(1) FROM BugComponent WHERE bug_num=num)>1
        ORDER BY 3 DESC, id, num;
END
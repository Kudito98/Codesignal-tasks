CREATE PROCEDURE solution()
BEGIN
	SELECT group_concat(concat(first_name," ", surname, " #", player_number) ORDER BY player_number 	SEPARATOR '; ') AS players FROM soccer_team;
END
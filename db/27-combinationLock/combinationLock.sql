CREATE PROCEDURE solution()
BEGIN
	SELECT ROUND(EXP(SUM(LOG(CHAR_LENGTH(characters))))) AS combinations FROM discs;
END
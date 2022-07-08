CREATE PROCEDURE solution()
BEGIN
	UPDATE reservedNicknames
    SET id = CONCAT_WS(" - ", "rename", id), nickname = CONCAT_WS(" - ", "rename", nickname)
    WHERE LENGTH(nickname) <> 8;

    SELECT * FROM reservedNicknames ORDER BY id;
END

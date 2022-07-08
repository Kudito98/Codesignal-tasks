CREATE PROCEDURE solution()
BEGIN
    ALTER TABLE restaurants 
    ADD (description VARCHAR(100) DEFAULT 'TBD', active INT DEFAULT 1);
    
    SELECT * FROM restaurants ORDER BY id;
END

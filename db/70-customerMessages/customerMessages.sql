DROP FUNCTION IF EXISTS response;
CREATE FUNCTION response(name VARCHAR(40)) RETURNS VARCHAR(200) DETERMINISTIC
BEGIN
    SET @Firstname = LOWER(SUBSTRING_INDEX(name, ' ', 1));
    SET @Lastname = LOWER(SUBSTRING_INDEX(name, ' ', -1));

    SET @Firstname = CONCAT(UPPER(LEFT(@Firstname, 1)), SUBSTRING(@Firstname, 2));
    SET @Lastname = CONCAT(UPPER(LEFT(@Lastname, 1)), SUBSTRING(@Lastname, 2));

    RETURN CONCAT('Dear ', @Firstname, ' ', @Lastname, '! We received your message and will process it as soon as possible. Thanks for using our service. FooBar On! - FooBarIO team.');
END;

CREATE PROCEDURE solution()
BEGIN
    SELECT id, name, response(name) AS response
    FROM customers;
END;

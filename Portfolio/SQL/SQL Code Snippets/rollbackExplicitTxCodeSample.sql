USE banking
GO

BEGIN TRAN 
	UPDATE saVaccount
	SET balance=balance-500
	WHERE customerID=18568
	IF (  (SELECT balance FROM savaccount WHERE customerID=18568)<0)
ROLLBACK TRAN
	UPDATE ckaccount 
	SET balance=balance+500
	WHERE customerID=18568
COMMIT TRAN 
GO

SELECT *
FROM savaccount
WHERE customerID=18568

GO

SELECT *
FROM ckaccount
WHERE customerID=18568

USE jproco
GO
--Create Banking Database, Checking account table, Savings account table, insert fictitious data for customer Skizzee Leaker
CREATE DATABASE banking
USE banking
GO
CREATE TABLE Savaccount (customerID INT PRIMARY KEY  NOT NULL, balance INT, custlastName VARCHAR(30) NOT NULL, custfirstname VARCHAR(20) NOT NULL)
GO
CREATE TABLE ckaccount (customerID INT NOT NULL, balance INT, custlastName VARCHAR(30) NOT NULL, custfirstname VARCHAR(20) NOT NULL)
GO
INSERT INTO savaccount
VALUES (18568, 501, 'Leaker', 'Skizzee')
GO
INSERT INTO ckaccount
VALUES (18568, 501, 'Leaker', 'Skizzee')
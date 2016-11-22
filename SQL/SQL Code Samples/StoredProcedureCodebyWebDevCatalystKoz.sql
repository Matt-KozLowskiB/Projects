USE [JProCo]
GO

/****** Object:  StoredProcedure [dbo].[DelGrantbyIDthenAddNewGrantDAta]    Script Date: 8/26/2016 5:02:32 PM ******/
--NOTE: Need to supply 1) GrantID# to delete;
--2) GrantID # of new Grant;
--3) GrantName of New Grant;
--4) GrantAmt of New Grant;
--Totally new, incredible query invented by Matt.B.Kozlowski, WebDev Catalyst
SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO

CREATE PROC [dbo].[DelGrantbyIDthenAddNewGrantDAta] @delgrantidnmbr INT, @newgrntID INT, @newgrntname VARCHAR(30), @newgrntamt INT
AS
BEGIN TRAN
	DELETE [grant]
	WHERE grantID = @delgrantidnmbr

	INSERT INTO [grant]
	VALUES (@newgrntID, @newgrntname, NULL, @newgrntamt)
COMMIT TRAN
GO



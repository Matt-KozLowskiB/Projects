USE [AdventureWorks2012]
GO

/****** Object:  StoredProcedure [dbo].[SDLASTFIRSTDEPTSHFTqueryII]    Script Date: 8/30/2016 6:18:36 PM ******/
SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO

CREATE PROC [dbo].[SDLASTFIRSTDEPTSHFTqueryII]  @StartDate NVARCHAR(10)=NULL, @LastName VARCHAR(30) = NULL, @FirstName VARCHAR(20)=NULL, @Dept VARCHAR(20)=NULL, @Shift VARCHAR(15) = NULL
AS
SELECT HRemp.BusinessEntityID,HRemp.StartDate, pp.LastName, pp.Firstname, HRdep.Name, HRsh.Name
FROM HumanResources.EmployeeDepartmentHistory AS HREmp
INNER JOIN Person.person as pp
ON HRemp.BusinessEntityID=pp.BusinessEntityID
INNER JOIN HumanResources.department AS HRdep
ON HRemp.departmentID=HRdep.departmentID
INNER JOIN HumanResources.[shift] AS HRsh
ON HRemp.ShiftID=HRsh.shiftID
WHERE HRemp.StartDate Like '%' + ISNULL(@StartDate, HRemp.StartDate)+'%'
AND pp.LastName LIKE '%'+ ISNULL(@LastName, pp.LastName)+'%'
AND pp.FirstName LIKE '%' + ISNULL(@FirstName,pp.FirstName)+'%'
AND HRdep.Name LIKE '%' + ISNULL(@Dept,HRdep.Name)+'%'
AND HRsh.Name LIKE '%' + ISNULL(@Shift, HRsh.Name)+ '%'
GO



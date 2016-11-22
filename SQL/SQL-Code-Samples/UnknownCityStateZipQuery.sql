USE [AdventureWorks2012]
GO

/****** Object:  StoredProcedure [dbo].[unkwnAddCityZip]    Script Date: 8/30/2016 2:46:53 PM ******/
SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO

CREATE PROC [dbo].[unkwnAddCityZip] @AddressLine1 NVARCHAR(40)=NULL, @City VARCHAR(20)=NULL, @PostalCode NVARCHAR(8)=NULL
AS
SELECT AddressLine1, City, PostalCode
FROM person.address
WHERE AddressLine1 LIKE '%'+ISNULL(@AddressLine1,AddressLine1) +'%'
AND City Like '%' + ISNULL(@City, City) +'%'
AND PostalCode LIKE '%'+ISNULL(@PostalCode,PostalCode)+'%'
ORDER BY City
GO



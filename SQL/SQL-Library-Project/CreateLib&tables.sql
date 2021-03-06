USE master
GO
DROP DATABASE Library
GO

CREATE DATABASE Library
GO
USE Library
GO
CREATE TABLE BookLoans (BookID INT PRIMARY KEY NOT NULL, BranchID INT NOT NULL, CardID INT NOT NULL, DateOut DATE NOT NULL, DateIn DATE NOT NULL)
GO
CREATE TABLE Branch (BranchID INT PRIMARY KEY NOT NULL, BranchName VARCHAR(30) NOT NULL, BranchAddress VARCHAR(50) NOT NULL)
GO
CREATE TABLE Borrower (CardID INT PRIMARY KEY NOT NULL, BorrowerName VARCHAR(50) NOT NULL, BorrowerAddress VARCHAR(50) NOT NULL, BorrowerPhone VARCHAR(20) NULL)
GO
CREATE TABLE BookCopies (BookID INT  NOT NULL, BranchID INT NOT NULL, NumberCopies INT NOT NULL)
GO
CREATE TABLE Author (BookID INT  NOT NULL, AuthorName VARCHAR(40) NOT NULL)
GO
CREATE TABLE Publisher (PublisherName VARCHAR(50) NOT NULL, PubAddress VARCHAR(50) NOT NULL, PubPhone VARCHAR(20) NOT NULL)
GO
CREATE TABLE Book (BookID INT PRIMARY KEY NOT NULL, BookTitle VARCHAR(100) NOT NULL, PublisherName VARCHAR(50) NOT NULL)
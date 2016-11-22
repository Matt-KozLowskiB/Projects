CREATE PROC NumberOfbyTitleBranch @GetBookTitle VARCHAR(30),@GetBranchName VARCHAR(40)
AS
SELECT NumberCopies,BookTitle,BranchName
FROM bookcopies AS bc
INNER JOIN book
ON bc.bookID=book.bookID
INNER JOIN branch
ON bc.branchID=branch.branchID
WHERE BookTitle=@GetBookTitle
AND branchname=@GetBranchName
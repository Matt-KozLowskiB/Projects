CREATE PROC FindbyAuthorBranch @GetAuthor VARCHAR(30), @GetBranch VARCHAR(30)
AS
SELECT BookTitle,numbercopies
FROM bookcopies as bc
INNER JOIN Branch as br
ON bc.branchID=br.branchID
INNER JOIN Author
ON Author.bookID=bc.bookID
INNER JOIN book
ON book.bookID=bc.bookID
WHERE authorname=@GetAuthor
AND branchname=@GetBranch
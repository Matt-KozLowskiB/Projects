SELECT NumberCopies,BookTitle,BranchName
FROM bookcopies AS bc
INNER JOIN book
ON bc.bookID=book.bookID
INNER JOIN branch
ON bc.branchID=branch.branchID
WHERE BookTitle='The Lost Tribe'
AND branchname LIKE '%'
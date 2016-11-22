SELECT BookTitle,numbercopies
FROM bookcopies as bc
INNER JOIN Branch as br
ON bc.branchID=br.branchID
INNER JOIN Author
ON Author.bookID=bc.bookID
INNER JOIN book
ON book.bookID=bc.bookID
WHERE authorname='Stephen King'
AND branchname='Central'
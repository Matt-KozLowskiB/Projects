
SELECT COUNT (*) AS booksloaned, BorrowerName
FROM BOOKLOANS as bl
INNER JOIN Borrower as br
on bl.cardID = br.cardID
INNER JOIN Book
ON book.bookid=bl.bookID
INNER JOIN Branch
ON branch.branchID=bl.branchID
GROUP BY BorrowerName
ORDER BY booksloaned DESC

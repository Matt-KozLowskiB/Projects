SELECT BorrowerName,BorrowerAddress,BorrowerPhone
FROM bookloans as bl
RIGHT JOIN borrower as br
ON br.cardID=bl.cardID
WHERE Bl.cardID IS NULL

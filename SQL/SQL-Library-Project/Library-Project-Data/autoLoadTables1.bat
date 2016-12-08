echo
cd\joes2pros
REM load data from text files publisher, branch and bookloans into Library database 
REM tables Publisher, Branch and BookCopies-

BCP library.dbo.Publisher IN publisher.txt -c -t, -T -r\n

BCP library.dbo.branch IN branch.txt -c -t, -T -r\n

BCP LIbrary.dbo.bookcopies IN bookloans1.txt -c -T -r\n

BCP library.dbo.author IN bookidauth.txt -c -T -r\n

BCP library.dbo.book IN books.txt -c -T -r\n

echo off
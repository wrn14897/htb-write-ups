1. Found secret path in HTML ('..../portfolio.php?id=1')
2. SQL injection using sqlmap (found hash password in freelancer table)
3. Crack passowrd using John the Ripper (too slow...)
4. Find hidden path using fuzzer (DIRB) -> http://165.232.32.84:31669/administrat
5. Then find potential php file -> 'dirb http://165.232.32.84:31669/administrat -X .php' -> index, panel
6. We can't see the content (302) from panel, so we can use --file-read option to retrive the file

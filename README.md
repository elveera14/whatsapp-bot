# whatsap-bot
It is a simple WhatsApp bot created using Python, Selenium and BeautifulSoup which takes a command and gives some output.

Now in detail, Exacly what we're gonna do is
1. we'll open whatsap webapp using our code.
2. we'll send a message to a specific contact Which will basically ask for some input.
3. we'll wait for 10 seconds.
4. we'll check if we got some responce.
    (i) we'll send a closing message in case of no response.
    (ii) we'll check if the given response is valid in case we have some response.
         (a) In case of valid response, we'll scrap some data from a website and send it.
         (b) In case of invalid response We'll simply send a message stating the same.
         
Note: It is a very basic version. Hence we have only one valid response and only one very basic scrapping operation.


**Exercise_Game**
<br>
We first changed the N variable to be 10, indicating that the program should flash 10 times for the user to test their response time. Next, we added the database_api_url, to the script, provided from the Firebase RealTime Database. We also defined the authorization url using the API key provided to us in Firebase. The authorization url was used to POST a game user's email and password to, checking if the user was authorized. If the user is authorized, the game script continues and they play the game as normal. If they are not authoized, the game script ends.
<br>
<br>
After the user plays the game, the data is POST to our Firebase using our database_api_url and the requestspost() function.

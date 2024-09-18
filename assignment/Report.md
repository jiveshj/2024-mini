
**Exercise_Game**
<br>
We first changed the N variable to be 10, indicating that the program should flash 10 times for the user to test their response time. Next, we added the database_api_url, to the script, provided from the Firebase RealTime Database. We also defined the authorization url using the API key provided to us in Firebase. The authorization url was used to POST a game user's email and password to, checking if the user was authorized. If the user is authorized, the game script continues and they play the game as normal. If they are not authoized, the game script ends.
<br>
<br>
After the user plays the game, the data is POST to our Firebase using our database_api_url and the requestspost() function.
<br>
<br>
Video to explanation of game script changes: https://drive.google.com/file/d/11ckuMMk4Gg_ktbyP83gU_T7NIFiLv3r7/view?usp=drive_link
Video to exercise_game execution: https://drive.google.com/file/d/1n6CW81tCQc919181dyqBDZaYS5t4At7A/view?usp=drive_link

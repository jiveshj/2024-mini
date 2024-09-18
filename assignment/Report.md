**Exercise_light**
<br>
For the exercise 01, we found the max and min bright values as follows: 
max brightness value:  4000
min brightness value: 51100
<br>
The resistance of the photocell decreases as more light shines on it. Therefore, in the voltage divider circuit we see that the value of the ADC2 decreases with increasing brightness (the resistance of the photocell decreases relative to the fixed 10K ohm resistor). Similarly, when the photocell is put in a dark room we see that its resistance increases, therefore the voltage across it increases and consequently the value of the ADC2 also increases. 
For finding the min brightness we put the photocell setup in a dark room and ran the code. For the max brightness, we shone two flashlights at the photocell to get the best possible max brightness value. 
<br>

**Exercise_sound**
<br>
We have modified our code to play the super Mario cart theme tune.  
<br>
**Exercise_Game**
<br>
We added code to make the Raspberry Pi Pico to connect to the internet (via wifi) so that it can communicate with firebase. 
We changed the N (no of times the LED blinks) variable to be 10, indicating that the program should flash 10 times for the user to test their response time. Next, we added the database_api_url (the database endpoint) to the script, provided from the Firebase RealTime Database. We also defined the authorization url using the API key provided to us in Firebase. The authorization url was used to POST a game user's email and password to, checking if the user was authorized. If the user is authorized, the game script continues and they play the game as normal. If they are not authoized, the game script ends.
<br>
<br>
After the user plays the game, the data is POST (via a restAPI which sends a HTTP request) to our Firebase using our database_api_url and the requestspost() function.
<br>
<br>
Video to explanation of game script changes: https://drive.google.com/file/d/11ckuMMk4Gg_ktbyP83gU_T7NIFiLv3r7/view?usp=drive_link
Video to exercise_game execution: https://drive.google.com/file/d/1n6CW81tCQc919181dyqBDZaYS5t4At7A/view?usp=drive_link

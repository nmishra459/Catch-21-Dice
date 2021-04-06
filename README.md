# Catch 21: Dice
### By Omar Wahby and Nishant Mishra

![Catch_21_Dice](https://user-images.githubusercontent.com/54038104/102028625-2cfc4700-3d79-11eb-937e-9087a06c4936.PNG)

<b>Description</b>: A web application (Flask, Jinja, Python) that features a two-player dice game (JavaScript), along with a personalized stats page and global leaderboard ranking all registered users (SQL). Front-end designed with HTML5/CSS and Bootstrap 4. Final project for CS50!

### Link to Deployed Website (Heroku): https://catch-21-dice.herokuapp.com/login

### Link to Video Demo: https://youtu.be/euf5um5zlSY

## Instructions on how to configure the project files to ensure proper functionality

	In your IDE, within a folder which can have any name please create two separate folders: 
	one folder called “static” and another folder called “templates.” 
	
	Place the following files in the “static” folder:
		catch_21.js
		dice.png
		dice1.jpg 
		dice2.jpg 
		dice3.jpg 
		dice4.jpg 
		dice5.jpg 
		dice6.jpg 
		favicon.ico 
		styles.css 
	 
	Place the following files in the “templates” folder:
		apology.html 
		change.html
		index.html
		layout.html 
		leaderboard.html
		login.html 
		play.html 
		register.html 
		second_player_login.html 
		stats.html

	Place the following files OUTSIDE of these two folders:
		application.py
		dice.db 
		helpers.py 
		requirements.txt 

	Once you have all these folders set up, cd into the parent folder, the first one 
	that was created, and type “flask run” into the command line. Following the link that flask 
	run creates will take you to the website.


## Registration and Starting a Game

		First, the user will be directed to a login page where they can sign into the 
	application if they already have an account, or click the “Register” button in the top right
	corner to create their account. The website will flash messages (as opposed to returning 
	apology.html) if the user fails to enter a username, password, or confirmation, if the username 
	has already been taken, or if the password and confirmation do not match once the user has created 
	their account. Then, the user will be redirected to the login page, where they can sign in by 
	entering their username and password to access the application. Once again, the code will flash 
	error messages if the username inputted is not in the dice.db database, or if the password entered 
	is incorrect. 
	
		Once the user logs in, they will be directed to a page containing the rules of the Catch 
	21: Dice Game. To get an early look at what the gameplay is like, the user can click the “roll” 
	button to cycle through the different dice values that can appear. Once the user has familiarized 
	themself with the rules of the game, they can click the “Play!” button below the game’s rules to 
	move on. They will then be directed to a page that allows them to play with another registered user 
	by having the other user log in with their username and password. The code will flash errors if the 
	inputted second player credentials match those of the user already logged in, or if the 
	username/password are not in the database or are incorrect. Alternatively, if the user would like 
	to play with a user who is currently unregistered, the second player can select the green-colored 
	“Play as Guest” button to allow them and the other person to play the game. 

## The Rules

		Catch 21: Dice is a two player game. Each player will get to take turns rolling the dice to 
	score 21 points. When it’s their turn, a player can choose to roll the dice to increase their total 
	score by clicking the "roll" button. Alternatively, a player can choose to stay at their current score 
	by clicking the button "stay." If a player is comfortable enough with their current score and wants to 
	withdraw from the game, they can click "fold."

	There are three different ways a player can win.
	1) If the opposing player's score exceeds 21.
	2) If they score 21 points before the other player.
	3) If, when they choose to fold by clicking the "fold" button, the opposing player reaches a lower 
	   score than them and folds.

## Playing the Game
	
		After another player chooses to play as a guest or as a registered user, the two players, 
	using the same device, will be able to play the game together! The first user who logged in to the 
	application will be “Player 1”, and will have their username displayed on the left, while the “Guest” 
	or the second user who logged in to the application will be “Player 2,” and will have their username 
	displayed on the right. When both players tie or one player wins, a notification will appear indicating 
	a tie or which player has won or lost the game. The game will then reset once this notification is 
	triggered. At any time during the game, if the user would like to change the person they are playing 
	against (Player 2), they can select the “Play” button in the top left corner of the screen and they 
	will be redirected to the page where another registered user can sign in or another person can play as
	a guest (Player 2).

## The “Your Stats” Page
	
		The “your stats” page contains a record of every match the user has played. In each row, 
	ranked from most to least recent, the stats page contains the time, opponent, games won, and games lost
	in a single match.

## The “Leaderboard” Page
	
		The leaderboard page will rank all the registered users by the number of games they’ve won 
	across their entire tenure as players. Users can see how many matches their fellow players have won, 
	lost, and played. 

## The “Change Password” Page
	
		The change password page lets the user that is logged in to change their password. They must 
	input their old password and what they want their new password to be, along with a confirmation to 
	prevent any mistakes in the resetting. If the confirmation or current password is entered incorrectly, 
	the user will be flashed an error message.

## Logging Out
	
		The player can log out of the application by selecting the “Log Out” button in the top right 
	corner. Player 2 is always logged out whenever one exits a match.

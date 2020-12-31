# Design Document: Catch 21: Dice
### By Omar Wahby and Nishant Mishra

## Static Files (in the “static” folder)
	
### catch_21.js 
	This file contains all of the custom javaScript code needed to program the Catch 21: Dice Game itself. To keep the code as
	concise and as readable as possible, we organized the code into 6 different functions. Three of these functions relate to 
	keeping track of and updating the scores of both players in a gaming session, while theother three functions provide proper 
	functionality for the three options that either player can choose when it is their turn: (1) to roll, (2) to stay, or (3) to fold.  
	
	roll()
		The first function (lines 6-50) in the script is called “roll”. This function is called when a player selects the 
	“Roll” button to roll the dice when it is their turn. First, a random integer is generated in line 10 to determine the amount
	by which to increment the score of the player who rolled the dice. Lines 13 and 14 serve to select the dice image that 
	displays this most recent randomly selected integer on the front end to both players. The second half of the “roll” function 
	deals with all possible scenarios that may happen when a player chooses to roll the dice. The first pair of if-else statements 
	(lines 18-35) increments the score of the player who chose to roll and (in lines 23-26, 31-34) checks if the amount by which a 
	player's score was incremented results in that player's current score equaling twenty-one, thereby causing that player to win 
	the game. The second set of if-else statements (lines 39-48) check if a player’s current score after rolling the dice has exceeded
	twenty-one, resulting in that player losing the game.

	game_won()
		The second function (lines 54-72) in the script is called “game_won”. This function is called whenever a player wins a 
	game. It takes in one integer parameter, called x, which is the number of the player who won a game. Depending on which player 
	won the game, the total number of wins and losses for both players of the current gaming session are updated accordingly and 
	displayed to both players at the bottom of the page. Finally, line 71 posts an announcement of the winner of the game to both 
	players.

	stay()
		The third function (lines 75-133) in the script is called “stay”. This function is called when a player selects the 
	“Stay” button to stay at their current score, effectively ending their turn. Lines 85-102 handle the scenario when no player 
	has folded. In this case, the current player who chose to stay has their background changed from green to gray (lines 88-89, 
	95-96) and the other player’s background changes from gray to green (lines 90-91, 97-98). Lines 125-131 provide a visual indication 
	to both players that the current player’s turn has ended and the other player’s turn has begun. Lines 106-122 handle the 
	scenario when at least one player has folded and the other player chooses to stay. Since a player who has already folded can 
	no longer be granted any more turns, the game must end with the winner or a tie being announced after the other person chooses 
	to stay (lines 109-120).


	fold()
		The fourth function (lines 136-196)  in the script is called “fold”. This function is called when a player selects the 
	“Fold” button to stay at their current score for the rest of the game. When a player folds, line 140 notifies both players about 
	which player has folded and lines 150-173 switch the background colors of both players to indicate that the player who first folded 
	can no longer do anything during the current game. To maintain good readability of the code, the names of the variables and the 
	process used to perform this background change are the same as what was  used to make the background change in the “stay” function. 
	Then, lines 178-194 handle the scenario in which both players decide to fold. In this case, a winner or a tie must be declared, so 
	the conditional statements in lines 181-192 compare the	scores of both players to determine the appropriate outcome of the current 
	game and prepare for the next game. 
	
	reset_score()
		The fifth function (lines 199-230) in the script is called “reset_score”. This function is called when a winner or tie is 
	announced, and serves to reset the scores of both players to zero, as well as the variables monitoring the number of players who 
	have folded during the last game, the current player of the game, as well as the background display associated with the current 
	and non-current player of the game. When it came to resetting the scores of both players to zero, javaScript’s setTimeout function 
	enabled us to synchronize the timings of when these resets took place, providing for a clear transition between one game and another 
	(lines 226-228).
	
	game_tie()
		The sixth function (lines 233-242) in the script is called “game_tie”. This function is called when the final scores of both 
	players are the same, and serves to increment both players’ number of wins by 1 (lines 234-235), display each player’s updated number 
	of wins (lines 236-237), and finally display an announcement of the game being a tie (line 241).

### styles.css
		For our CSS file, we aimed to create a clear and simple look to our application with vivid colors to visually differentiate 
	between different buttons both in the game page itself and in the other pages as well. In addition, we used relative positioning 
	rather than absolute positioning to create the visual layout of each page to keep everything as simple as possible for the user to 
	understand. Bold print and larger font size were used to demarcate important information, and contrasting colors were used to 
	distinguish between different rows in the tables organizing information about a user’s personal stats regarding their performance 
	in the game and the leaderboard comparing the records of all users.

## Template Files (in the “templates” folder)

### HTML files
	apology.html
		apology.html is taken from CS50: Finance, but is used much more sparingly than it is in Problem Set 9, since we believed 
	that redirecting users to a completely different html page would be too disruptive for players. Instead, we utilize flash in most 
	scenarios, reserving apology.html for whenever the error handler runs into a serious issue, which should not happen, but we keep in 
	our code just in case.

	change.html
		change.html is the page we use to let user’s change their password should they ever feel the need to. It was decided that a 
	simple form with fields for the current password, a new password, and the new password’s confirmation would suffice for the layout 
	of this page.

	index.html 
		index.html is the main home-page for Catch 21: Dice players. We use <p> and <ul> tags to log down the rules, and include 
	some interactive elements. Players can 	click the roll button on the homepage so see what it looks like in actual gameplay, relying 
	on the “roll” function in the catch_21.js file. Players can also click the “play” button at the bottom, which takes them to the 
	second_player_login.html page to let the second player play as a guest or log into their account.

	layout.html 
		Layout.html is taken from CS50: Finance. We made some minor stylistic changes to the nav-bar, and added a note of gratitude 
	to Prof. Malan, the debugging duck, and the rest of the CS50 staff in the footer.

	leaderboard.html 
		leaderboard.html is where the aggregate performances of each register player are ranked. This page uses jinja to present 
	each of the rows that it receives from 	the leaderboard function from application.py.

	login.html 
		login.html is where users log in. It is almost identical to CS50: Finance’s log-in page. There is an added header. Login 
	presents a form whose information is sent to application.py’s login function for verification via POST.

	play.html 
		play.html is where players can play matches. Please see catch_21.js for information about the actual gameplay. We used a 
	disabled input form to contain the number of wins/losses accrued by each player, allowing us to easily POST the results of the match 
	to the play function in application.py by clicking the “End Match!” button, sidestepping the need for AJAX in this case.

	register.html 
		register.html contains a form allowing users to register for accounts. It consists of a form asking for a username, a 
	password, and a confirmation, which are sent to application.py’s registration function via POST. See application.py for more 
	information on how registration is verified.

	second_player_login.html 
		second_player_login is where the second player for a match can log in. login.html presents a form whose information is 
	sent to application.py’s second_player_login login function for verification via POST. We also included a button that ties to the 
	“guest” function in application.py, in case the second player has no account and wishes to just go straight to the match.

	stats.html 
		stats.html is where the individual match performances for the players are listed, ranked by time. This page uses jinja 
	to present each of the rows that it receives from the stats function of application.py
		
### application.py
	index()
	index() renders index.html, the home page.
	
	login()
		Adapted from Pset 9: CS50 Finance. Instead of rendering the apology template when the inputted username/password 
	combination is not in the users table in dice.db, we used the flash() function to let the user know that they’ve made a mistake.
	This involved modifying the logic and rendering the exact same logic page every time our code detects a human error, since we’re 
	no longer rendering the apology template.

	logout()
		Adapted from PSet 9: CS50 Finance.

	register()
		Adapted from Pset 9: CS50 Finance. Like login(), we used flash instead of the apology template, leading to similar 
	changes in the render conditions to the ones we made in login().

	change()
		Again, adapted from Pset 9: CS50 Finance. Like login() and register(), we used flash instead of the apology template, 
	leading to similar changes in the render conditions to the ones we made in login() and register().

	second_login()
		Renders the second_player_login.html page once the user clicks play on the home page or on the navigation bar. Once 
	it receives a “POST” request, the function checks for the second player’s login credentials in the exact same manner that 
	login() does, and redirects the player to play.html for the actual game, with the usernames of the first and second player 
	as parameters.

	guest()
		Executes whenever the second user selects the “Play as Guest” option. This sets the username of the second player as 
	“Guest,” and renders the play.html template with the username of the player that was originally logged in, along with “guest” 
	for player 2’s username. 

	end()
		Executes whenever one of the users selects the “End Match” button on the play.html page. When it receives a POST request, 
	the function takes whatever was in the input fields (the wins/losses scoreboard) on the play.html page, and translates them into 
	numerical scores. It then adds the wins and losses for player 1 to get the total number of games played. Having collected player 
	1’s wins, losses, and total games played, the code then adds each of the values to the corresponding lines  (lines 216-218) and 
	adds them to corresponding fields in the row in the database that is registered under player 1’s id. The function then inserts the 
	game into the play_history table, storing player 1’s id, the opponent’s name (“Guest” or the username of a registered player), games
	won, games lost, total games played, and the time in which the match.

		Player 2’s leaderboard update is a little different. First, the function makes sure that player 2 didn’t play as a guest 
	(nothing is stored in the leaderboard if it is), and then gets player 2’s id via a sQL query. Then, it moves on to perform the 
	same exact actions that it did with player 1, this time with player 2’s id and stats, with player 1’s username as the opponent. 
	Then, the function redirects the user to the home page (index.html) via the “/” route.

	stats()
		stats() queries the play_history table in dice.db for all the rows with an id of the player that is currently logged in, 
	and orders them by time in descending order, so the most recent time is first. It then renders the stats.html page with these rows 
	as a parameter.

	leaderboard()
		leaderboard() queries for all the users data from users table, orders it in descending order by total number of games won 
	(so the person with the highest number of wins will be first), and renders leaderboard.html with these rows as a parameter.


### dice.db
	dice.db contains two tables, users, and play history. 

	users
		Each entry in the users will contain a player’s username, id, hashed password, 
	total games won, total games lost, and total games played. 

	play_history
		Each entry in the play_history table corresponds to a match results for a player, 
	and contains their id, the match end time, the player’s opponent, the number of matches 
	the player won, and the number of matches the player lost. 

### helpers.py
	helpers.py is identical to the one in CS50: Finance, but some of the finance-related 
	functions, like lookup and usd, have been removed.

let player1_score = 0, player2_score = 0, dice = 0, current_player = 1, not_current_player = 2, playersFolded = 0, player1_wins = 0, player1_losses = 0, player2_wins = 0, player2_losses = 0;
const WINNING_SCORE = 21;

//rolls the dice and increments the player scores by the number that the dice image displays
//deals with all possible scenarios if a player chooses to roll the dice
function roll() {
    console.log('Player ' + current_player + 'is rolling the dice...');

    //randomly chooses an integer between 1 and 6
    let dice = Math.ceil(Math.random()*6);

    //selects the dice image that displays the most recent randomly selected number
    document.getElementById('dice-img').src = './static/dice' + dice + '.jpg';
    document.getElementById('dice-img').alt = 'Dice landed on' + dice;

    //increments the score of the player who chose to roll the dice
    if(dice >= 1) {
        if(current_player === 1) {
            player1_score += dice;
            document.getElementById('player1-score').innerHTML = 'Score: ' + player1_score;

            //checks if the amount by which a player's score was incremented results in that player's score equaling twenty-one
            if(player1_score === WINNING_SCORE) {
                game_won(1);
                setTimeout(function(){ reset_score() }, 140);
            }
        }
        else {
            player2_score += dice;
            document.getElementById('player2-score').innerHTML = 'Score: ' + player2_score;
            if(player2_score === WINNING_SCORE) {
                game_won(2);
                setTimeout(function(){ reset_score() }, 140);
            }
        }

        //checks if a player's score exceeds 21, which is the winning score, and displays the appropriate winner
        if(player1_score > WINNING_SCORE || player2_score > WINNING_SCORE) {
            if(current_player === 1) {
                game_won(2);
                //delays the resetting of both player's scores by 140 milliseconds
                setTimeout(function(){ reset_score() }, 140);
            }
            else {
                game_won(1);
                setTimeout(function(){ reset_score() }, 140);
            }
        }
    }
}

//updates both players' number of wins and losses for the current gaming session if a winner of the current game is declared
//the game_won function takes in an integer parameter, x, which is the number of the player who won a game
function game_won(x) {
    if (x === 1){
        player1_wins++;
        player2_losses++;
        document.getElementById("player1-wins").value = player1_wins;
        document.getElementById("player2-losses").value = player2_losses;
    }
    else {
        player2_wins++;
        player1_losses++;
        document.getElementById("player2-wins").value = player2_wins;
        document.getElementById("player1-losses").value = player1_losses;
    }

    //displays the winner of the game on the front end
    console.log(x + ' just WON!');
    document.querySelector('#result').innerHTML = "Congratulations Player " + x + " just won!!!";
}

//deals with all possible scenarios that may occur when one player chooses to stay
function stay() {
    console.log('Player ' + current_player + ' just chose to stay');

    let current_player_background, current_player_text;
    let other_player_background, other_player_text;

    /*
    changes the color of the background for both players, with the player who is currently rolling always having the green background
    and the player who is not currently rolling always having the grey background
    */
    if(playersFolded === 0) {
        if(current_player === 1) {
            current_player_background = 'player2-background';
            current_player_text = 'player2-text';
            other_player_background = 'player1-background';
            other_player_text = 'player1-text';
            current_player = 2;
            not_current_player = 1;
        } else {
            current_player_background = 'player1-background';
            current_player_text = 'player1-text';
            other_player_background = 'player2-background';
            other_player_text = 'player2-text';
            current_player = 1;
            not_current_player = 2;
        }
    }

    //ensures that if one player has already folded, that same player can not have the option to roll again
    //For example, if player 1 folds and player 2 chooses to stay, one player must win or a tie is called.
    else if(playersFolded >= 1) {
        if(player1_score < WINNING_SCORE && player2_score < WINNING_SCORE) {
            if(player1_score > player2_score) {
                game_won(1);
                setTimeout(function(){ reset_score() }, 140);
            }
            else if(player1_score < player2_score) {
                game_won(2);
                setTimeout(function(){ reset_score() }, 140);
            }
            else if(player1_score === player2_score) {
                game_tie();
                setTimeout(function(){ reset_score() }, 140);
            }
        }
    }

    //changes the backgrounds on the front end according to which player's turn it now is
    document.getElementById(current_player_background).style.background = '#90EE90';
    document.getElementById(current_player_background).style.color = '#000000';
    document.getElementById(current_player_text).innerHTML = 'It is your turn';

    document.getElementById(other_player_background).style.background = '#DCDCDC';
    document.getElementById(other_player_background).style.color = '#A9A9A9';
    document.getElementById(other_player_text).innerHTML = 'It is NOT your turn';

}

//deals with all possible scenarios if one player or both players choose to fold.
function fold() {
    console.log('Player ' + current_player + ' just folded');

    //notifies both players on the front end which player has just chosen to fold
    document.querySelector('#result').innerHTML = 'Player ' + current_player + ' just folded!';

    let current_player_background, current_player_text;
    let other_player_background, other_player_text;

    /*
    changes the color of the background for both players, with the first player who chose to fold having a permanent grey background,
    indicating they can no longer roll until the current game ends,
    and the player whose turn it now is to roll having a permanent green background
    */
    if(current_player === 1) {
        current_player_background = 'player2-background';
        current_player_text = 'player2-text';
        other_player_background = 'player1-background';
        other_player_text = 'player1-text';
        current_player = 2;
        not_current_player = 1;
    } else {
        current_player_background = 'player1-background';
        current_player_text = 'player1-text';
        other_player_background = 'player2-background';
        other_player_text = 'player2-text';
        current_player = 1;
        not_current_player = 2;
    }

    //changes the backgrounds on the front end according to which player's turn it now is
    document.getElementById(current_player_background).style.background = '#90EE90';
    document.getElementById(current_player_background).style.color = '#000000';
    document.getElementById(current_player_text).innerHTML = 'It is your turn';

    document.getElementById(other_player_background).style.background = '#DCDCDC';
    document.getElementById(other_player_background).style.color = '#A9A9A9';
    document.getElementById(other_player_text).innerHTML = 'It is NOT your turn';

    playersFolded += 1;

    //ensures that if both players have already folded, a winner or a tie must be announced
    if(playersFolded === 2) {
        //comparing both players' scores to determine the appropriate outcome of the game
        if(player1_score < WINNING_SCORE && player2_score < WINNING_SCORE) {
            if(player1_score > player2_score) {
                game_won(1);
                setTimeout(function(){ reset_score() }, 140);
            }
            else if(player1_score < player2_score) {
                game_won(2);
                setTimeout(function(){ reset_score() }, 140);
            }
            else if(player1_score === player2_score) {
                game_tie();
                setTimeout(function(){ reset_score() }, 140);
            }
        }
    }
}

//deals with resetting the scores and adjusting the backgrounds of both players after the current game ends, in order to have a new game begin
function reset_score() {
    //resetting the variables
    player1_score = 0;
    player2_score = 0;
    playersFolded = 0;
    current_player = 1;
    not_current_player = 2;

    let current_player_background, current_player_text;
    let other_player_background, other_player_text;

    //resetting the backgrounds
    current_player_background = 'player1-background';
    current_player_text = 'player1-text';
    other_player_background = 'player2-background';
    other_player_text = 'player2-text';

    //resetting the backgrounds on the front end
    document.getElementById(current_player_background).style.background = '#90EE90';
    document.getElementById(current_player_background).style.color = '#000000';
    document.getElementById(current_player_text).innerHTML = 'It is your turn';

    document.getElementById(other_player_background).style.background = '#DCDCDC';
    document.getElementById(other_player_background).style.color = '#A9A9A9';
    document.getElementById(other_player_text).innerHTML = 'It is NOT your turn';

    //synchronizes the timing by which the scores are reset and a new round is annouced
    setTimeout(() => {document.getElementById('player1-score').innerHTML = 'Score: 0'},1500);
    setTimeout(() => {document.getElementById('player2-score').innerHTML = 'Score: 0'},1500);
    setTimeout(() => {document.querySelector('#result').innerHTML = "Time for a new round!"}, 3000);

}

//updates both players' number of wins and losses for the current gaming session if a tie is declared for the current game
function game_tie() {
    player1_wins++;
    player2_wins++;
    document.getElementById('player1-wins').value = player1_wins;
    document.getElementById('player2-wins').value = player2_wins;
    console.log('The game is a tie!');

    //announces a tie game on the front end
    setTimeout(() => {document.querySelector('#result').innerHTML = "The game is a tie!"}, 3000);
}
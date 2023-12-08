import pyautogui
import random

score_level_1 = score_level_2 = score_level_3 = name_check = coins = cheat_code_use = 0
play_check_r = play_check_mg = play_check_cf = play_check_gtn = play_check_mt = play_check_tod = 0
one_star = two_stars = three_stars = four_stars = five_stars = 0
name_list_1 = ['Lukas', 'mia', 'leon', 'julia', 'anna', 'lea']
name_list_2 = ['fynn', 'ben', 'lena', 'tobias', 'laura']
roshambo_choice_list = ['rock ✊', 'paper ✋', 'scissors ✌️']
operator_1_list = ['+', '-']
operator_2_list = ['+', '*', '-', '*']
operator_3_list = ['+', '*', '-', '*', '//']
coin_list = ['heads \n🧑', 'tails \n🏰']
Coordinates_list = [[985, 325], [1190, 530], [985, 730], [790, 530]]
players_name_list = []
review_list = []
lower_case_alphabet = 'abcdefghijklmnopqrstuvwxuz'
upper_case_alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXUZ'
cheat_code = str(random.randint(0, 9))+random.choice(lower_case_alphabet)+random.choice(upper_case_alphabet)+str(random.randint(0, 9))
unlock_mt = unlock_cf =  coin_alert = False

#this is the review and rating block code
def feedback () :
    global one_star
    global two_stars
    global three_stars 
    global four_stars 
    global five_stars
    global review_list
    rating = pyautogui.confirm(text = 'how would you rate this game?', title = 'thank you for playing roshambo!', buttons = ['⭐', '⭐⭐', '⭐⭐⭐', '⭐⭐⭐⭐', '⭐⭐⭐⭐⭐'])
    if rating == '⭐⭐⭐⭐⭐' :
        five_stars += 1
        asking_for_review = pyautogui.confirm(text = 'thank you so much for the 5-star rating! 🌟 \n we are thrilled to hear that you are enjoying our game 😍 \ndo like to give us a review too? 📜', title = 'Review', buttons = ['yes', 'no'])
        if asking_for_review == 'yes' :
            review = pyautogui.prompt(text = 'please write your review here', title = 'reviewing 🔍' , default = 'write here')
            if  review !=  '' and  review != 'write here':
                review_list.append(review)
        else :
            pyautogui.alert(text = 'we hope you have a review for us next time! \nwe stick to the five-star rating for now 😎', title = 'no review!? thats ok', button = 'OK')
                
    elif rating == '⭐⭐⭐⭐' :
        four_stars += 1
        asking_for_review = pyautogui.confirm(text = 'we are so glad to hear that you love  our \ngame 😄 do like to give us a review too? \nwe will appreciate that 💭', title = 'Review', buttons = ['yes', 'no'])
        if asking_for_review == 'yes' :
            review = pyautogui.prompt(text = 'please write your review here', title = 'reviewing 🔍' , default = 'write here')
            if review !=  '' and  review != 'write here':
                review_list.append(review)
        else :
            pyautogui.alert(text = 'we hope you have a review for us next time! \nwe stick to the four-star rating for now 😎', title = 'no review!? thats ok', button = 'OK')
                
    elif rating == '⭐⭐⭐' :
        three_stars += 1
        asking_for_review = pyautogui.confirm(text = 'we appreciate your feedback, we would love \nto hear more about your experience,  would \nyou like to write a review? 📜', title = 'Review', buttons = ['yes', 'no'])
        if asking_for_review == 'yes' :
            review = pyautogui.prompt(text = 'please write your review here', title = 'reviewing 🔍' , default = 'write here')
            if  review !=  '' and  review != 'write here':
                review_list.append(review)
        else :
            pyautogui.alert(text = 'we hope you have a review for us next time! \nwe stick to the three-star rating for now 😅', title = 'no review!? thats ok', button = 'OK')

    elif rating == '⭐⭐' :
        two_stars += 1
        asking_for_review = pyautogui.confirm(text = 'we noticed that you gave us a two-star rating 😔\nwe would like to underestand your experience,  would \nyou like to write a review? ✉️ ', title = 'Review', buttons = ['yes', 'no'])
        if asking_for_review == 'yes' :
            review = pyautogui.prompt(text = 'please write your review here', title = 'reviewing 🔍' , default = 'write here')
            if  review !=  '' and  review != 'write here':
                review_list.append(review)
        else :
            pyautogui.alert(text = 'we hope you have a review for us next time! \nwe stick to the two-star rating for now 😅', title = 'no review!? thats ok', button = 'OK')
                
    elif rating == '⭐' :
        one_star += 1
        asking_for_review = pyautogui.confirm(text = 'we are sorry that this game wasn\'t a pleasant 😢\nexperince for you do you like to write a review about it?', title = 'Review', buttons = ['yes', 'no'])
        if asking_for_review == 'yes' :
            review = pyautogui.prompt(text = 'please write your review here', title = 'reviewing 🔍' , default = 'write here')
            if  review !=  '' and  review != 'write here':
                review_list.append(review)
        else :
            pyautogui.alert(text = 'we hope you have a review for us next time! \nwe stick to the one-star rating for now 😕', title = 'no review!? thats ok', button = 'OK')

pyautogui.alert(text = f'wellcome  to  the  game  center 🏖️ \nuse this cheat code to recive coins : \n                            {cheat_code}', title = 'wellcome!', button = 'thanks')

while True :
    player_1_Score = player_2_Score = bot_1_score = bot_2_score = correct = wrong = 0
    truth_list = ['what is your biggest fear?','What is the most embarrassing thing you\'ve ever done?' ,'When was the last time you cried?' ,'Have you ever broken the law? ', 'When was the last time you lied?', 'What\'s the worst thing you\'ve ever done at work?', 'Who\'s the last person you searched on Instagram?', 'What\'s the worst date you\'ve been on?', 'What\'s your guilty pleasure?', 'What\'s one thing you only do when you\'re alone?', 'If you had to get back with an ex, who would you choose?', 'What\'s your biggest pet peeve?', 'If you could become invisible, what\'s the worst thing you\'d do?', 'If you could become invisible, what\'s the worst thing you\'d do?', 'If you were the opposite sex for one day, what would you do?']
    dare_list = ['What is the most embarrassing photo of you?','Yell out the first word that comes to your mind.' ,'Hold three ice cubes in your mouth until they melt.' ,'Try to lick your elbow.', 'Quack like a duck until your next turn.', 'Argue with a wall and pretend like it talks back for one minute.', 'Smile as widely as you can and hold it for two minutes', 'Say everything in a whisper for the next 10 minutes', 'Eat a snack without using your hands', 'For the next 10 minutes, every time someone asks you something, respond with a bark', 'Reply to the first five Instagram Stories on your timeline', 'Try and make the group laugh as quickly as possible', 'Keep your eyes closed until it\'s your go again', 'Repeat everything the person on your right is saying until it\'s your turn again', ' Yell out the first word that comes to your mind.']

    # tells you to buy a game when you have enough coins
    if (coins >= 5) and (coin_alert == False) :
        coin_alert = True
        enough_coin_alert = pyautogui.confirm(text = 'you have enough coins to buy a game 🎉\nyou can buy : \n  1.mousetrap \n   2.coin flip', title = 'coins', buttons = ['menu', 'buying game 1', 'buying game 2'])
        if enough_coin_alert == 'buying game 1' :
            coins -= 5
            unlock_mt = True
            pyautogui.alert(text = 'you just bought mousetrap \nyou can play it by going to games', title = 'mouse trap', button = 'menu')
        elif enough_coin_alert == 'buying game 2' :
            coins -= 5
            unlock_cf = True
            pyautogui.alert(text = 'you just bought coin flip \nyou can play it by going to games', title = 'coin flip', button = 'menu')


    menu = pyautogui.confirm(text = 'game center', title = 'game center\'s menu', buttons = ['games', 'about us', 'reviews', 'shop', 'exit'])

    if menu == 'games' :
        game = pyautogui.confirm(text = 'choose one of the games below', title = 'games', buttons = ['roshambo', 'math game', 'coin flip', 'guess the number', 'mousetrap','truth or dare' , 'menu'])

        #----game number 1 'roshambo'----#
        if game == 'roshambo' :
            if play_check_r == 0 :
                how_to_play = pyautogui.confirm(text = 'have you ever played roshambo before?', title = 'roshambo', buttons = ['yes', 'no'])
                play_check_r += 1
                if how_to_play == 'no' :
                    pyautogui.alert(text = 'roshambo or Rock, paper, scissors is a fun and easy game that anyone can learn and enjoy.\n\nrules : \nRock beats scissors   ✊ \nscissors beat paper   ✌️ \nand paper beats rock   ✋', title = 'how to play roshambo', button = 'got it')
                
            mode = pyautogui.confirm(text = 'choose a game mode', title = 'mode', buttons = ['player vs player', 'player vs bot', 'bot vs bot', 'menu'])

            #----roshambo's player vs player mood----#
            if mode == 'player vs player' :
                mode_alert = pyautogui.confirm(text = 'you have selected the two player 🧍🧍 mode.', title = 'player vs player', buttons = ['play', 'menu'])
                if mode_alert == 'menu' :
                    continue

                player_1_name = pyautogui.prompt(text = 'hi player 1 \nenter your name if you don\'t, \ni will choose name for you hehe 🤭', title = 'name of the player 1' , default = '') 
                if player_1_name == '' :
                    player_1_name = random.choice(name_list_1)
                    pyautogui.alert(text = f'your name is {player_1_name} from now on 😁', title = 'player 1', button = 'OK')

                player_2_name = pyautogui.prompt(text = 'hi player 2 \nenter your name if you don\'t, \ni will choose name for you hehe 🤭', title = 'name of the player 2' , default = '') 
                if player_2_name == '' :
                    player_2_name = random.choice(name_list_2)
                    pyautogui.alert(text = f'your name is {player_2_name} from now on 😁', title = 'player 2', button = 'OK')

                game_type = pyautogui.confirm(text = 'how do you like to play? \n\n1.restrict the number of game rounds. 🔁 \n2.specify the final score. 🏅', title = 'game type', buttons = ['rounds', 'score'])
                
                #----player vs player game based on rounds----#
                if game_type == 'rounds' :  
                    rounds = int(pyautogui.prompt(text = 'how many rounds do you want to play? 🕵️', title = 'rounds' , default = '2',))

                    for round in range(1,rounds+1) :
                        player_1_choice = pyautogui.confirm(text = f'{player_1_name}\'s turn \nchoose your move', title = f'round {round}', buttons = ['rock ✊', 'paper ✋', 'scissors ✌️'])
                        player_2_choice = pyautogui.confirm(text = f'{player_2_name}\'s turn \nchoose your move', title = f'round {round}', buttons = ['rock ✊', 'paper ✋', 'scissors ✌️'])

                        if player_1_choice == 'rock ✊' and player_2_choice == 'paper ✋' :
                            player_2_Score += 1
                            pyautogui.alert(text = f'{player_2_name} won this round ✋🎉 \nscores so far : \n{player_1_name} : {player_1_Score} \n{player_2_name} : {player_2_Score}', title = f'round {round} result', button = 'OK')
                        elif player_1_choice == 'rock ✊' and player_2_choice == 'scissors ✌️' :
                            player_1_Score += 1
                            pyautogui.alert(text = f'{player_1_name} won this round ✊🎉 \nscores so far : \n{player_1_name} : {player_1_Score} \n{player_2_name} : {player_2_Score}', title = f'round {round} result', button = 'OK')
                        elif player_1_choice == 'paper ✋' and player_2_choice == 'rock ✊' :
                            player_1_Score += 1
                            pyautogui.alert(text = f'{player_1_name} won this round ✋🎉 \nscores so far : \n{player_1_name} : {player_1_Score} \n{player_2_name} : {player_2_Score}', title = f'round {round} result', button = 'OK')
                        elif player_1_choice == 'paper ✋' and player_2_choice == 'scissors ✌️' :
                            player_2_Score += 1
                            pyautogui.alert(text = f'{player_2_name} won this round ✌️🎉 \nscores so far : \n{player_1_name} : {player_1_Score} \n{player_2_name} : {player_2_Score}', title = f'round {round} result', button = 'OK')
                        elif player_1_choice == 'scissors ✌️' and player_2_choice == 'rock ✊' :
                            player_2_Score += 1
                            pyautogui.alert(text = f'{player_2_name} won this round ✊🎉 \nscores so far : \n{player_1_name} : {player_1_Score} \n{player_2_name} : {player_2_Score}', title = f'round {round} result', button = 'OK')
                        elif player_1_choice == 'scissors ✌️' and player_2_choice == 'paper ✋' :
                            player_1_Score += 1
                            pyautogui.alert(text = f'{player_1_name} won this round ✌️🎉 \nscores so far : \n{player_1_name} : {player_1_Score} \n{player_2_name} : {player_2_Score}', title = f'round {round} result', button = 'OK')
                        else :
                            pyautogui.alert(text = f'draw 🙄\n{player_1_name} and {player_2_name} both choose {player_1_choice} \nscores so far : \n{player_1_name} : {player_1_Score} \n{player_2_name} : {player_2_Score}', title = f'round {round} result', button = 'OK')
                    
                    #----player vs player based on rounds  game's result----# 
                    if player_1_Score > player_2_Score :
                        pyautogui.alert(text = f'{player_1_name} won the game 🥰✨', title = 'winner!', button = 'OK')
                    elif player_1_Score < player_2_Score :
                        pyautogui.alert(text = f'{player_2_name} won the game 🥰✨', title = 'winner!', button = 'OK')
                    else :
                        pyautogui.alert(text = 'the score of the players was equal 🤷', title = 'nobody won!', button = 'OK')
                    
                #----player vs player game based on score----#
                elif game_type == 'score' :
                    wining_score = int(pyautogui.prompt(text = 'Choose the desired score to select the winner', title = 'wining score' , default = '2'))
                    round = 0

                    while True :
                        round += 1

                        player_1_choice = pyautogui.confirm(text = f'{player_1_name}\'s turn \nchoose your move', title = f'round {round}', buttons = ['rock ✊', 'paper ✋', 'scissors ✌️'])
                        player_2_choice = pyautogui.confirm(text = f'{player_2_name}\'s turn \nchoose your move', title = f'round {round}', buttons = ['rock ✊', 'paper ✋', 'scissors ✌️'])

                        if player_1_choice == 'rock ✊' and player_2_choice == 'paper ✋' :
                            player_2_Score += 1
                            pyautogui.alert(text = f'{player_2_name} won this round ✋🎉 \nscores so far : \n{player_1_name} : {player_1_Score} \n{player_2_name} : {player_2_Score}', title = f'round {round} result', button = 'OK')
                        elif player_1_choice == 'rock ✊' and player_2_choice == 'scissors ✌️' :
                            player_1_Score += 1
                            pyautogui.alert(text = f'{player_1_name} won this round ✊🎉 \nscores so far : \n{player_1_name} : {player_1_Score} \n{player_2_name} : {player_2_Score}', title = f'round {round} result', button = 'OK')
                        elif player_1_choice == 'paper ✋' and player_2_choice == 'rock ✊' :
                            player_1_Score += 1
                            pyautogui.alert(text = f'{player_1_name} won this round ✋🎉 \nscores so far : \n{player_1_name} : {player_1_Score} \n{player_2_name} : {player_2_Score}', title = f'round {round} result', button = 'OK')
                        elif player_1_choice == 'paper ✋' and player_2_choice == 'scissors ✌️' :
                            player_2_Score += 1
                            pyautogui.alert(text = f'{player_2_name} won this round ✌️🎉 \nscores so far : \n{player_1_name} : {player_1_Score} \n{player_2_name} : {player_2_Score}', title = f'round {round} result', button = 'OK')
                        elif player_1_choice == 'scissors ✌️' and player_2_choice == 'rock ✊' :
                            player_2_Score += 1
                            pyautogui.alert(text = f'{player_2_name} won this round ✊🎉 \nscores so far : \n{player_1_name} : {player_1_Score} \n{player_2_name} : {player_2_Score}', title = f'round {round} result', button = 'OK')
                        elif player_1_choice == 'scissors ✌️' and player_2_choice == 'paper ✋' :
                            player_1_Score += 1
                            pyautogui.alert(text = f'{player_1_name} won this round ✌️🎉 \nscores so far : \n{player_1_name} : {player_1_Score} \n{player_2_name} : {player_2_Score}', title = f'round {round} result', button = 'OK')
                        else :
                            pyautogui.alert(text = f'draw 🙄\n{player_1_name} and {player_2_name} both choose {player_1_choice} \nscores so far : \n{player_1_name} : {player_1_Score} \n{player_2_name} : {player_2_Score}', title = f'round {round} result', button = 'OK')

                        #----player vs player based on score game's result----#
                        if player_1_Score == wining_score :
                            pyautogui.alert(text = f'{player_1_name} reached the selected score ({wining_score}) \nand won the game 🥰✨', title = 'winner!', button = 'OK')
                            break
                        elif player_2_Score == wining_score :
                            pyautogui.alert(text = f'{player_2_name} reached the selected score ({wining_score}) \nand won the game 🥰✨', title = 'winner!', button = 'OK')
                            break
                    
                coins += 2
                feedback()

            #----roshambo's player vs bot mood----#   
            elif mode == 'player vs bot' :
                mode_alert = pyautogui.confirm(text = 'you have selected the player 🙋 vs bot 🤖 mode.', title = 'player vs bot', buttons = ['play', 'menu'])
                if mode_alert == 'menu' :
                    continue

                player_1_name = pyautogui.prompt(text = 'hi player \nenter your name if you don\'t, \ni will choose name for you hehe 🤭', title = 'name of the player' , default = '') 
                if player_1_name == '' :
                    player_1_name = random.choice(name_list_1)
                    pyautogui.alert(text = f'your name is {player_1_name} from now on 😁', title = 'player', button = 'OK')

                bot_1_name = pyautogui.prompt(text = 'choose a name for the bot if you don\'t, \ni will choose name for it hehe 🤭', title = 'name of the bot' , default = '') 
                if bot_1_name == '' :
                    bot_1_name = random.choice(name_list_2)
                    pyautogui.alert(text = f'the bot\'s name is {bot_1_name} from now on 😁', title = 'bot', button = 'OK')

                game_type = pyautogui.confirm(text = 'how do you like to play? \n\n1.restrict the number of game rounds. 🔁 \n2.specify the final score. 🏅', title = 'game type', buttons = ['rounds', 'score'])
                
                #----player vs bot based on rounds----#
                if game_type == 'rounds' : 
                    rounds = int(pyautogui.prompt(text = 'how many rounds do you want to play?', title = 'rounds' , default = '2',))

                    for round in range(1,rounds+1) :
                        player_1_choice = pyautogui.confirm(text = f'{player_1_name}\'s turn \nchoose your move', title = f'round {round}', buttons = ['rock ✊', 'paper ✋', 'scissors ✌️'])
                        bot_1_choice = random.choice(roshambo_choice_list)

                        if player_1_choice == 'rock ✊' and bot_1_choice == 'paper ✋' :
                            bot_1_score += 1
                            pyautogui.alert(text = f'{bot_1_name} won this round ✋🎉 \nscores so far : \n{player_1_name} : {player_1_Score} \n{bot_1_name} : {bot_1_score}', title = f'round {round} result', button = 'OK')
                        elif player_1_choice == 'rock ✊' and bot_1_choice == 'scissors ✌️' :
                            player_1_Score += 1
                            pyautogui.alert(text = f'{player_1_name} won this round ✊🎉 \nscores so far : \n{player_1_name} : {player_1_Score} \n{bot_1_name} : {bot_1_score}', title = f'round {round} result', button = 'OK')
                        elif player_1_choice == 'paper ✋' and bot_1_choice == 'rock ✊' :
                            player_1_Score += 1
                            pyautogui.alert(text = f'{player_1_name} won this round ✋🎉 \nscores so far : \n{player_1_name} : {player_1_Score} \n{bot_1_name} : {bot_1_score}', title = f'round {round} result', button = 'OK')
                        elif player_1_choice == 'paper ✋' and bot_1_choice == 'scissors ✌️' :
                            bot_1_score += 1
                            pyautogui.alert(text = f'{bot_1_name} won this round ✌️🎉 \nscores so far : \n{player_1_name} : {player_1_Score} \n{bot_1_name} : {bot_1_score}', title = f'round {round} result', button = 'OK')
                        elif player_1_choice == 'scissors ✌️' and bot_1_choice == 'rock ✊' :
                            bot_1_score += 1
                            pyautogui.alert(text = f'{bot_1_name} won this round ✊🎉 \nscores so far : \n{player_1_name} : {player_1_Score} \n{bot_1_name} : {bot_1_score}', title = f'round {round} result', button = 'OK')
                        elif player_1_choice == 'scissors ✌️' and bot_1_choice == 'paper ✋' :
                            player_1_Score += 1
                            pyautogui.alert(text = f'{player_1_name} won this round ✌️🎉 \nscores so far : \n{player_1_name} : {player_1_Score} \n{bot_1_name} : {bot_1_score}', title = f'round {round} result', button = 'OK')
                        else :
                            pyautogui.alert(text = f'draw 🙄\n{player_1_name} and {bot_1_name} both choose {player_1_choice} \nscores so far : \n{player_1_name} : {player_1_Score} \n{bot_1_name} : {bot_1_score}', title = f'round {round} result', button = 'OK')

                    #----player vs bot based on rounds game's result----# 
                    if player_1_Score > bot_1_score :
                        pyautogui.alert(text = f'{player_1_name} won the game 🥰✨', title = 'winner!', button = 'OK')
                    elif player_1_Score < bot_1_score :
                        pyautogui.alert(text = f'{bot_1_name} won the game 🥰✨', title = 'winner!', button = 'OK')
                    else :
                        pyautogui.alert(text = 'the score of the players was equal 🤷', title = 'nobody won!', button = 'OK')

                #----player vs bot based on score----#
                elif game_type == 'score' :
                    wining_score = int(pyautogui.prompt(text = 'Choose the desired score to select the winner', title = 'wining score' , default = '2'))
                    round = 0

                    while True :
                        round += 1
                        player_1_choice = pyautogui.confirm(text = f'{player_1_name}\'s turn \nchoose your move', title = f'round {round}', buttons = ['rock ✊', 'paper ✋', 'scissors ✌️'])
                        bot_1_choice = random.choice(roshambo_choice_list)

                        if player_1_choice == 'rock ✊' and bot_1_choice == 'paper ✋' :
                            bot_1_score += 1
                            pyautogui.alert(text = f'{bot_1_name} won this round ✋🎉 \nscores so far : \n{player_1_name} : {player_1_Score} \n{bot_1_name} : {bot_1_score}', title = f'round {round} result', button = 'OK')
                        elif player_1_choice == 'rock ✊' and bot_1_choice == 'scissors ✌️' :
                            player_1_Score += 1
                            pyautogui.alert(text = f'{player_1_name} won this round ✊🎉 \nscores so far : \n{player_1_name} : {player_1_Score} \n{bot_1_name} : {bot_1_score}', title = f'round {round} result', button = 'OK')
                        elif player_1_choice == 'paper ✋' and bot_1_choice == 'rock ✊' :
                            player_1_Score += 1
                            pyautogui.alert(text = f'{player_1_name} won this round ✋🎉 \nscores so far : \n{player_1_name} : {player_1_Score} \n{bot_1_name} : {bot_1_score}', title = f'round {round} result', button = 'OK')
                        elif player_1_choice == 'paper ✋' and bot_1_choice == 'scissors ✌️' :
                            bot_1_score += 1
                            pyautogui.alert(text = f'{bot_1_name} won this round ✌️🎉 \nscores so far : \n{player_1_name} : {player_1_Score} \n{bot_1_name} : {bot_1_score}', title = f'round {round} result', button = 'OK')
                        elif player_1_choice == 'scissors ✌️' and bot_1_choice == 'rock ✊' :
                            bot_1_score += 1
                            pyautogui.alert(text = f'{bot_1_name} won this round ✊🎉 \nscores so far : \n{player_1_name} : {player_1_Score} \n{bot_1_name} : {bot_1_score}', title = f'round {round} result', button = 'OK')
                        elif player_1_choice == 'scissors ✌️' and bot_1_choice == 'paper ✋' :
                            player_1_Score += 1
                            pyautogui.alert(text = f'{player_1_name} won this round ✌️🎉 \nscores so far : \n{player_1_name} : {player_1_Score} \n{bot_1_name} : {bot_1_score}', title = f'round {round} result', button = 'OK')
                        else :
                            pyautogui.alert(text = f'draw 🙄\n{player_1_name} and {bot_1_name} both choose {player_1_choice} \nscores so far : \n{player_1_name} : {player_1_Score} \n{bot_1_name} : {bot_1_score}', title = f'round {round} result', button = 'OK')

                        #----player vs bot based on rounds game's result----#
                        if player_1_Score == wining_score :
                            pyautogui.alert(text = f'{player_1_name} reached the selected score ({wining_score}) \nand won the game 🥰✨', title = 'winner!', button = 'OK')
                            break
                        elif bot_1_score == wining_score :
                            pyautogui.alert(text = f'{bot_1_name} reached the selected score ({wining_score}) \nand won the game 🥰✨', title = 'winner!', button = 'OK')
                            break

                coins += 2
                feedback()

            #----roshambo's bot vs bot mood----# 
            elif mode == 'bot vs bot' :
                mode_alert = pyautogui.confirm(text = 'you have selected the bot 🤖 vs bot 🤖 mode. \nyou have to guess which bot will win', title = 'bot vs bot', buttons = ['play', 'menu'])
                if mode_alert == 'menu' :
                    continue

                bot_1_name = pyautogui.prompt(text = 'choose a name for bot 1 if you don\'t, \ni will choose name for you hehe 🤭', title = 'name of the bot 1' , default = '') 
                if bot_1_name == '' :
                    bot_1_name = random.choice(name_list_1)
                    pyautogui.alert(text = f'your name is {bot_1_name} from now on 😁', title = 'player', button = 'OK')

                bot_2_name = pyautogui.prompt(text = 'choose a name for the bot 2 if you don\'t, \ni will choose name for it hehe 🤭', title = 'name of the bot 2' , default = '') 
                if bot_2_name == '' :
                    bot_2_name = random.choice(name_list_2)
                    pyautogui.alert(text = f'the bot\'s name is {bot_2_name} from now on 😁', title = 'bot', button = 'OK')

                game_type = pyautogui.confirm(text = 'how do you like to play? \n\n1.restrict the number of game rounds. 🔁 \n2.specify the final score. 🏅', title = 'game type', buttons = ['rounds', 'score'])
                
                #----bot vs bot based on rounds----#
                if game_type == 'rounds' : 
                    players_guess = pyautogui.confirm(text = 'guess which bot will win 🕵️ :', title = 'guess the winner', buttons = [f'{bot_1_name}', 'draw', f'{bot_2_name}'])
                    rounds = int(pyautogui.prompt(text = 'how many rounds do you want them to play?', title = 'rounds' , default = '2',))

                    for round in range(1,rounds+1) :
                        bot_1_choice = random.choice(roshambo_choice_list)
                        bot_2_choice = random.choice(roshambo_choice_list)
                        pyautogui.alert(text = f'{bot_1_name} chose {bot_1_choice}\n\n{bot_2_name} chose {bot_2_choice}', title = f'round {round}', button = 'OK')

                        if bot_1_choice == 'rock ✊' and bot_2_choice == 'paper ✋' :
                            bot_2_score += 1
                            pyautogui.alert(text = f'{bot_2_name} won this round ✋🎉 \nscores so far : \n{bot_1_name} : {bot_1_score} \n{bot_2_name} : {bot_2_score}', title = f'round {round} result', button = 'OK')
                        elif bot_1_choice == 'rock ✊' and bot_2_choice == 'scissors ✌️' :
                            bot_1_score += 1
                            pyautogui.alert(text = f'{bot_1_name} won this round ✊🎉 \nscores so far : \n{bot_1_name} : {bot_1_score} \n{bot_2_name} : {bot_2_score}', title = f'round {round} result', button = 'OK')
                        elif bot_1_choice == 'paper ✋' and bot_2_choice == 'rock ✊' :
                            bot_1_score += 1
                            pyautogui.alert(text = f'{bot_1_name} won this round ✋🎉 \nscores so far : \n{bot_1_name} : {bot_1_score} \n{bot_2_name} : {bot_2_score}', title = f'round {round} result', button = 'OK')
                        elif bot_1_choice == 'paper ✋' and bot_2_choice == 'scissors ✌️' :
                            bot_2_score += 1
                            pyautogui.alert(text = f'{bot_2_name} won this round ✌️🎉 \nscores so far : \n{bot_1_name} : {bot_1_score} \n{bot_2_name} : {bot_2_score}', title = f'round {round} result', button = 'OK')
                        elif bot_1_choice == 'scissors ✌️' and bot_2_choice == 'rock ✊' :
                            bot_2_score += 1
                            pyautogui.alert(text = f'{bot_2_name} won this round ✊🎉 \nscores so far : \n{bot_1_name} : {bot_1_score} \n{bot_2_name} : {bot_2_score}', title = f'round {round} result', button = 'OK')
                        elif bot_1_choice == 'scissors ✌️' and bot_2_choice == 'paper ✋' :
                            bot_1_score += 1
                            pyautogui.alert(text = f'{bot_1_name} won this round ✌️🎉 \nscores so far : \n{bot_1_name} : {bot_1_score} \n{bot_2_name} : {bot_2_score}', title = f'round {round} result', button = 'OK')
                        else :
                            pyautogui.alert(text = f'draw 🙄\n{bot_1_name} and {bot_2_name} both choose {bot_1_choice} \nscores so far : \n{bot_1_name} : {bot_1_score} \n{bot_2_name} : {bot_2_score}', title = f'round {round} result', button = 'OK')

                    #----bot vs bot based on rounds game's result----#
                    if bot_1_score > bot_2_score and players_guess == f'{bot_1_name}' :
                        pyautogui.alert(text = 'your guess was right 😄 ', title = f'{bot_1_name} won', button = 'yay!')
                    elif bot_1_score < bot_2_score and players_guess == f'{bot_2_name}' :
                        pyautogui.alert(text = 'your guess was right 😄 ', title = f'{bot_2_name} won', button = 'yay!')
                    elif bot_1_score == bot_2_score and players_guess == 'draw' :
                        pyautogui.alert(text = f'your guess was right 😄 \n{bot_1_name} and {bot_2_name} score was equal', title = f'draw', button = 'yay!')
                    elif bot_1_score > bot_2_score and players_guess != f'{bot_1_name}' :
                        pyautogui.alert(text = 'your guess was wrong 🙁 ', title = f'{bot_1_name} won', button = 'ok')
                    elif bot_1_score < bot_2_score and players_guess != f'{bot_2_name}' :
                        pyautogui.alert(text = 'your guess was wrong 🙁 ', title = f'{bot_2_name} won', button = 'ok')
                    elif bot_1_score == bot_2_score and players_guess != 'draw' :
                        pyautogui.alert(text = f'your guess was wrong 🙁 \n{bot_1_name} and {bot_2_name} score was equal', title = f'draw', button = 'ok')

                #----bot vs bot based on score----#
                elif game_type == 'score' :
                    players_guess = pyautogui.confirm(text = 'guess which bot will win 🕵️ :', title = 'guess the winner', buttons = [f'{bot_1_name}', f'{bot_2_name}'])
                    wining_score = int(pyautogui.prompt(text = 'Choose the desired score to select the winner', title = 'wining score' , default = '2'))
                    round = 0

                    while True :
                        round += 1
                        bot_1_choice = random.choice(roshambo_choice_list)
                        bot_2_choice = random.choice(roshambo_choice_list)
                        pyautogui.alert(text = f'{bot_1_name} chose {bot_1_choice}\n\n{bot_2_name} chose {bot_2_choice}', title = f'round {round}', button = 'OK')

                        if bot_1_choice == 'rock ✊' and bot_2_choice == 'paper ✋' :
                            bot_2_score += 1
                            pyautogui.alert(text = f'{bot_2_name} won this round ✋🎉 \nscores so far : \n{bot_1_name} : {bot_1_score} \n{bot_2_name} : {bot_2_score}', title = f'round {round} result', button = 'OK')
                        elif bot_1_choice == 'rock ✊' and bot_2_choice == 'scissors ✌️' :
                            bot_1_score += 1
                            pyautogui.alert(text = f'{bot_1_name} won this round ✊🎉 \nscores so far : \n{bot_1_name} : {bot_1_score} \n{bot_2_name} : {bot_2_score}', title = f'round {round} result', button = 'OK')
                        elif bot_1_choice == 'paper ✋' and bot_2_choice == 'rock ✊' :
                            bot_1_score += 1
                            pyautogui.alert(text = f'{bot_1_name} won this round ✋🎉 \nscores so far : \n{bot_1_name} : {bot_1_score} \n{bot_2_name} : {bot_2_score}', title = f'round {round} result', button = 'OK')
                        elif bot_1_choice == 'paper ✋' and bot_2_choice == 'scissors ✌️' :
                            bot_2_score += 1
                            pyautogui.alert(text = f'{bot_2_name} won this round ✌️🎉 \nscores so far : \n{bot_1_name} : {bot_1_score} \n{bot_2_name} : {bot_2_score}', title = f'round {round} result', button = 'OK')
                        elif bot_1_choice == 'scissors ✌️' and bot_2_choice == 'rock ✊' :
                            bot_2_score += 1
                            pyautogui.alert(text = f'{bot_2_name} won this round ✊🎉 \nscores so far : \n{bot_1_name} : {bot_1_score} \n{bot_2_name} : {bot_2_score}', title = f'round {round} result', button = 'OK')
                        elif bot_1_choice == 'scissors ✌️' and bot_2_choice == 'paper ✋' :
                            bot_1_score += 1
                            pyautogui.alert(text = f'{bot_1_name} won this round ✌️🎉 \nscores so far : \n{bot_1_name} : {bot_1_score} \n{bot_2_name} : {bot_2_score}', title = f'round {round} result', button = 'OK')
                        else :
                            pyautogui.alert(text = f'draw 🙄\n{bot_1_name} and {bot_2_name} both choose {bot_1_choice} \nscores so far : \n{bot_1_name} : {bot_1_score} \n{bot_2_name} : {bot_2_score}', title = f'round {round} result', button = 'OK')
                        

                        #----bot vs bot based on score game's result----#
                        if bot_1_score == wining_score and players_guess == f'{bot_1_name}' :
                            pyautogui.alert(text = f'your guess was right 😄 \n{bot_1_name} reached the selected ({wining_score}) score and won!', title = f'{bot_1_name} won', button = 'yay!')
                            break
                        elif bot_2_score == wining_score and players_guess == f'{bot_2_name}' :
                            pyautogui.alert(text = f'your guess was right 😄 \n{bot_2_name} reached the selected ({wining_score}) score and won!', title = f'{bot_2_name} won', button = 'yay!')
                            break
                        elif bot_1_score == wining_score and players_guess != f'{bot_1_name}' :
                            pyautogui.alert(text = f'your guess was wrong 🙁 \n{bot_1_name} reached the selected ({wining_score}) score and won!', title = f'{bot_1_name} won', button = 'ok')
                            break
                        elif bot_2_score == wining_score and players_guess != f'{bot_2_name}' :
                            pyautogui.alert(text = f'your guess was wrong 🙁 \n{bot_2_name} reached the selected ({wining_score}) score and won!', title = f'{bot_2_name} won', button = 'ok')
                            break   

                coins += 2
                feedback()

            
         # game number 2  'math game' #
        elif game == 'math game' :
            if play_check_mg == 0 :
                play_check_mg += 1
                how_to_play = pyautogui.confirm(text = 'have you ever played math game before?', title = 'math game', buttons = ['yes', 'no'])
                if how_to_play == 'no' :
                    pyautogui.alert(text = 'This  is  a  game  with  four  simple \nmathematical   operators,  questions \nare asked according to the difficulty \nof  the stage,  and  each  stage has \n7 rounds.', title = 'how to play the math game', button = 'got it')

            if name_check == 0 :
                player_1_name = pyautogui.prompt(text = 'hi friend \nenter your name if you don\'t, \ni will choose name for you hehe 🤭', title = 'name of the player' , default = '')
                name_check += 1
            if player_1_name == '' :
                player_1_name = random.choice(name_list_1)
                pyautogui.alert(text = f'your name is {player_1_name} from now on 😁', title = 'player 1', button = 'OK')
        
            while True :
                level = pyautogui.confirm(text = f'it\'s time to choose the difficulty level, {player_1_name}', title = 'game difficulty levels', buttons = ['level 1\n(easy)', 'level 2\n(medium)', 'level 3\n(hard)', 'menu'])

                if level == 'level 1\n(easy)' :
                    pyautogui.alert(text='starting level 1, these are the rules 🤓 :\n \n1_to win this level you must answer\n   answer at least three questions correctly\n \n2_their will be 6 question asked\n \n3_You will be given questions \n   with + and - operators', title='level 1', button='got it')

                    for round in range(1,6+1) :
                        number_1 = random.randint(1,50)
                        number_2 = random.randint(1,50)
                        operator_1 = random.choice(operator_1_list)
                        answer = int(pyautogui.prompt(text = f'What is the answer to the following question? 🧐\n{number_1} {operator_1} {number_2} = ?', title = f'round {round}' , default = '101'))

                        if operator_1 == '+' :
                            correct_answer = number_1 + number_2
                        elif operator_1 == '-' :
                            correct_answer = number_1 - number_2
                        if answer == correct_answer :
                            score_level_1 += 1 
                            pyautogui.alert(text = f'your answer was right 😄\nyour score so far : {score_level_1}', title = 'result', button = 'yay!')
                        elif answer != correct_answer :
                            if score_level_1 > 0 :
                                score_level_1 -= 1
                            pyautogui.alert(text = f'your answer was wrong! 🤨\nyour score so far : {score_level_1}', title = 'result', button = 'dang!')
                    if score_level_1 >= 3 :
                        coins += 2
                        finall_alert = pyautogui.confirm(text = f'you finished level 1 and you won! 🏆\nyour final score is  {score_level_1}\nyou can play level 2 now\nif you want to continue playing, click menu otherwise click exit', title = 'congrats', buttons = ['levels','menu'])
                    else :
                        finall_alert = pyautogui.confirm(text = f'you finished level 1 but you lost! 😩\nyour final score is  {score_level_1}\nfor playing the next level your score should be 4 or higher\nif you want to continue playing, click menu otherwise click exit', title = 'oh shoot', buttons = ['levels','menu'])
                    if finall_alert == 'menu' :
                        break


                elif level == 'level 2\n(medium)' :
                    if score_level_1 >= 3 :
                        pyautogui.alert(text='starting level 2, these are the rules 🤓 :\n \n1_to win this level you must answer\n   answer at least three questions correctly\n \n2_their will be 7 question asked\n \n3_You will be given questions \n   with +, - and * operators', title='level 1', button='got it')
                        for round in range(1,7+1) :
                            number_1 = random.randint(1,30)
                            number_2 = random.randint(1,12)
                            operator_2 = random.choice(operator_2_list)
                            answer = int(pyautogui.prompt(text = f'What is the answer to the following question? 🧐\n{number_1} {operator_2} {number_2} = ?', title = f'round {round}' , default = '362'))
                            if operator_2 == '+' :
                                correct_answer = number_1 + number_2
                            elif operator_2 == '-' :
                                correct_answer = number_1 - number_2
                            elif operator_2 == '*' :
                                correct_answer = number_1 * number_2 
                            if answer == correct_answer :
                                score_level_2 += 1
                                pyautogui.alert(text = f'your answer was right 😄\nyour score so far : {score_level_2}', title = 'result', button = 'yay!')
                            else :
                                if score_level_2 > 0 :
                                    score_level_2 -= 1
                                pyautogui.alert(text = f'your answer was wrong! 😶\nyour score so far : {score_level_2}', title = 'result', button = 'dang!')
                        if score_level_2 >= 3 :
                            coins += 2
                            finall_alert = pyautogui.confirm(text = f'you finished level 2 and you won! 🏆\nyour final score is  {score_level_2}\nyou can play level 3 now\nif you want to continue playing, click menu otherwise click exit', title = 'congrats', buttons = ['levels','menu'])
                        else :
                            finall_alert = pyautogui.confirm(text = f'you finished level 2 but you lost! 😩\nyour final score is  {score_level_2}\nfor playing the next level your score should be 4 or higher\nif you want to continue playing, click menu otherwise click exit', title = 'oh shoot', buttons = ['levels','menu'])
                        if finall_alert == 'menu' :
                            break
                    else :
                        info = pyautogui.confirm(text = f'you can\'t play level 2 🙅 because\nthe score of the first level is less than 4\n\nyour current score  {score_level_1}', title = 'leve 2', buttons = ['menu', 'levels'])
                        if info == 'levels' :
                            continue
                        else :
                            break


                elif level == 'level 3\n(hard)' :
                    if score_level_2 >= 0 :
                        pyautogui.alert(text='starting level 3, these are the rules 🤓 :\n \n1_to win this level you must answer\n   answer at least four questions correctly\n \n2_their will be 7 question asked\n \n3_You will be given questions \n   with +, -, // and * operators', title='level 1', button='got it')
                        for round in range(1,7+1) :
                            number_1 = random.randint(1,30)
                            number_2 = random.randint(1,12)
                            operator_3 = random.choice(operator_3_list)
                            answer = int(pyautogui.prompt(text = f'What is the answer to the following question? 🧐\n{number_1} {operator_3} {number_2} = ?', title = f'round {round}' , default = '365'))
                            if operator_3 == '-' :
                                correct_answer = number_1 - number_2
                            elif operator_3 == '+' :
                                correct_answer = number_1 + number_2
                            elif operator_3 == '*' :
                                correct_answer = number_1 * number_2
                            elif operator_3 == '//' :
                                correct_answer = number_1 // number_2
                            if answer == correct_answer :
                                score_level_3 += 1
                                pyautogui.alert(text = f'your answer was right 😄\nyour score so far : {score_level_3}', title = 'result', button = 'yay!')
                            else :
                                if score_level_3 > 0 :
                                    score_level_3 -= 1
                                pyautogui.alert(text = f'your answer was wrong! 😑\nyour score so far : {score_level_3}', title = 'result', button = 'dang!')
                        if score_level_3 >= 4 :
                            coins += 2
                            finall_alert = pyautogui.confirm(text = f'you finished level 3 and you won! 🏆\nyour final score is  {score_level_3}', title = 'congrats', buttons = ['levels','menu'])
                        else :
                            finall_alert = pyautogui.confirm(text = f'you finished level 3 but you lost! 😩\nyour final score is  {score_level_3}\nfor winning this level your score should be 4 or higher\nif you want to continue playing, click menu otherwise click exit', title = 'oh shoot', buttons = ['levels','menu'])

                        feedback()

                        if finall_alert == 'menu' :
                            break
                    else :
                        info = pyautogui.confirm(text = f'you can\'t play level 3 🙅 because\nthe score of the first level is less than 4\n\nyour current score  {score_level_2}', title = 'leve 2', buttons = ['menu', 'levels'])
                        if info == 'levels' :
                            continue
                        else :
                            break
                else :
                    break

         # game number 3 'coin flip' #
        elif game == 'coin flip' :
            if unlock_cf == True :
                if play_check_cf == 0 :
                    play_check_cf += 1
                    how_to_play = pyautogui.confirm(text = 'have you ever played coin flip before?', title = 'coin flip', buttons = ['yes', 'no'])
                    if how_to_play == 'no' :
                        pyautogui.alert(text = 'a coin is thrown into the air and \nyou have to guess which side it \nlands on', title = 'coin flip', button = 'got it')

                rounds = int(pyautogui.prompt(text = 'how many rounds to you want to play?', title = 'rounds' , default = '2'))
                for round in range(1,rounds+1) :
                    guess = pyautogui.confirm(text = 'which side does the coin land on ?🧐', title = f'round {round}', buttons = ['heads \n🧑', 'tails \n🏰'])
                    coin = random.choice(coin_list)
                    
                    if guess == coin :
                        correct += 1
                        if coin == 'heads \n🧑' :
                            pyautogui.alert(text = f'you guessed it right, \nthe coin landed on heads 🧑', title = 'correct ✔️', button = 'OK')
                        else :
                            pyautogui.alert(text = f'you guessed it right, \nthe coin landed on tails 🏰', title = 'correct ✔️', button = 'OK')
                    else :
                        wrong += 1
                        if coin == 'heads \n🧑' :
                            pyautogui.alert(text = f'you guessed it wrong, \nthe coin landed on heads 🧑', title = 'wrong ❌', button = 'OK')
                        else :
                            pyautogui.alert(text = f'you guessed it wrong, \nthe coin landed on tails 🏰', title = 'wrong ❌', button = 'OK')

                coins += 2
                pyautogui.alert(text = f'you had : \n    {correct} correct guesses ✔️ \n    {wrong} wrong guesses ❌', title = 'the game is over', button = 'OK')

                feedback()
            
            else :
                buying = pyautogui.confirm(text = 'for playing this game you have to buy it for 5 coins  first', title = 'the game is locked', buttons = ['menu', 'buying this game'])
                if buying == 'buying this game' :
                    if coins >= 5 :
                        buying = pyautogui.confirm(text = 'are you sure about buying this game?', title = 'buying coin flip', buttons = ['yes', 'no'])
                        if buying == 'yes' :
                            coins -= 5
                            unlock_cf = True
                            pyautogui.alert(text = f'congrats! you bought coin flip \nand your have {coins} left', title = 'coin flip is unlocked now', button = 'OK')

                    else :
                        pyautogui.alert(text = f'your coins are not enough for buying this game \nyou need 5 coins to buy this \n you only have {coins} coins', title = 'sorry', button = 'menu')

         # game number 4 'guess the number' #
        elif game == 'guess the number' :
            if play_check_gtn == 0 :
                play_check_gtn += 1
                how_to_play = pyautogui.confirm(text = 'have you ever played guess the number before?', title = 'guess the number', buttons = ['yes', 'no'])
                if how_to_play == 'no' :
                    pyautogui.alert(text = 'the game selects a mystery number and the player enters their initial guess. Players receive feedback on whether their guess is greater than or less than the mystery number.', title = 'guess the number', button = 'got it')

            while True :

                mode = pyautogui.confirm(text = 'choose a game mode', title = 'mode', buttons = ['1 player', '2 player', 'menu'])

                if mode == '1 player' :
                    level = pyautogui.confirm(text = 'choose a difficulty', title = 'level', buttons = ['easy\n😃', 'medium\n🙂', 'hard\n😕', 'menu'])

                    #----guess the number level easy----#
                    if level == 'easy\n😃' :
                        play = pyautogui.confirm(text = 'A number between 1 and 50 \nYou have 4 chances to guess it', title = 'guess the number', buttons = ['play', 'players', 'menu'])
                        if play == 'players' :
                            continue
                        elif play == 'menu' :
                            break
                        answer = random.randint(1,50)
                        for round in range(1,5+1) :
                            guess = int(pyautogui.prompt(text = 'guess the number', title = f'round {round}' , default = '0'))
                            if guess > 50 or guess <= 0 :
                                pyautogui.alert(text = '❗ The number you entered is not within the defined range', title = f'guess {round}', button = 'OK')
                            elif 0 < guess > answer :
                                pyautogui.alert(text = f'🎈 Your guess of {guess} is too high!', title = f'guess {round}', button = 'OK')
                            elif 0 < guess < answer :
                                pyautogui.alert(text = f'⚓ Your guess of {guess} is too low!', title = f'guess {round}', button = 'OK')
                            
                            if guess == answer :
                                coins += 2
                                pyautogui.alert(text = f'🎉 Your guess of {guess} is correct!', title = 'winner!', button = 'OK')
                                break
                            elif round == 5 :
                                coins += 2
                                pyautogui.alert(text = f'💣 The answer was number {answer}, \nbut you could not guess it', title = 'game over!', button = 'OK')
                        
                    elif level == 'medium\n🙂' :
                        play = pyautogui.confirm(text = 'A number between 1 and 100 \nYou have 4 chances to guess it', title = 'guess the number', buttons = ['play', 'players', 'menu'])
                        if play == 'players' :
                            continue
                        elif play == 'menu' :
                            break
                        answer = random.randint(1,100)
                        for round in range(1,7+1) :
                            guess = int(pyautogui.prompt(text = 'guess the number', title = f'round {round}' , default = '0'))
                            if guess > 100 or guess <= 0 :
                                pyautogui.alert(text = '❗ The number you entered is not within the defined range', title = f'guess {round}', button = 'OK')
                            elif 0 < guess > answer :
                                pyautogui.alert(text = f'🎈 Your guess of {guess} is too high!', title = f'guess {round}', button = 'OK')
                            elif 0 < guess < answer :
                                pyautogui.alert(text = f'⚓ Your guess of {guess} is too low!', title = f'guess {round}', button = 'OK')
                            if guess == answer :
                                coins += 2
                                pyautogui.alert(text = f'🎉 Your guess of {guess} is correct!', title = 'winner!', button = 'OK')
                                break
                            elif round == 7 :
                                coins += 2
                                pyautogui.alert(text = f'💣 The answer was number {answer}, \nbut you could not guess it', title = 'game over!', button = 'OK')
                        

                    elif level == 'hard\n😕' :
                        play = pyautogui.confirm(text = 'A number between 1 and 300 \nYou have 4 chances to guess it', title = 'guess the number', buttons = ['play', 'players', 'menu'])
                        if play == 'players' :
                            continue
                        elif play == 'menu' :
                            break
                        answer = random.randint(1,300)
                        for round in range(1,10+1) :
                            guess = int(pyautogui.prompt(text = 'guess the number', title = f'round {round}' , default = '0'))
                            if guess > 300 or guess <= 0 :
                                pyautogui.alert(text = '❗ The number you entered is not within the defined range', title = f'guess {round}', button = 'OK')
                            elif 0 < guess > answer :
                                pyautogui.alert(text = f'🎈 Your guess of {guess} is too high!', title = f'guess {round}', button = 'OK')
                            elif 0 < guess < answer :
                                pyautogui.alert(text = f'⚓ Your guess of {guess} is too low!', title = f'guess {round}', button = 'OK')
                            if guess == answer :
                                coins += 2
                                pyautogui.alert(text = f'🎉 Your guess of {guess} is correct!', title = 'winner!', button = 'OK')
                                break
                            elif round == 10 :
                                coins += 2
                                pyautogui.alert(text = f'💣 The answer was number {answer}, \nbut you could not guess it', title = 'game over!', button = 'OK')
                    else :
                        break
                elif mode == '2 player' :
                    level = pyautogui.confirm(text = 'choose a difficulty', title = 'level', buttons = ['easy\n😃', 'medium\n🙂', 'hard\n😕', 'menu'])

                    #----guess the number level easy----#
                    if level == 'easy\n😃' :
                        play = pyautogui.confirm(text = 'A number between 1 and 50 \nYou have 4 chances to guess it', title = 'guess the number', buttons = ['play', 'players', 'menu'])
                        if play == 'players' :
                            continue
                        elif play == 'menu' :
                            break
                        elif play == 'play' :
                            player_1_name = pyautogui.prompt(text = 'hi player 1 \nenter your name if you don\'t, \ni will choose name for you hehe 🤭', title = 'name of the player 1' , default = '') 
                            if player_1_name == '' :
                                player_1_name = random.choice(name_list_1)
                                pyautogui.alert(text = f'your name is {player_1_name} from now on 😁', title = 'player 1', button = 'OK')

                            player_2_name = pyautogui.prompt(text = 'hi player 2 \nenter your name if you don\'t, \ni will choose name for you hehe 🤭', title = 'name of the player 2' , default = '') 
                            if player_2_name == '' :
                                player_2_name = random.choice(name_list_2)
                                pyautogui.alert(text = f'your name is {player_2_name} from now on 😁', title = 'player 2', button = 'OK')

                            answer = random.randint(1,50)
                            for round in range(1,5+1) :
                                player_1_guess = int(pyautogui.prompt(text = f'{player_1_name}\'s trun \nguess the number', title = f'round {round}' , default = '0'))
                                
                                if player_1_guess > 50 or player_1_guess <= 0 :
                                    pyautogui.alert(text = '❗ The number you entered is not within the defined range', title = f'guess {round}', button = 'OK')
                                elif 0 < player_1_guess > answer :
                                    pyautogui.alert(text = f'🎈 Your guess of {guess} is too high!', title = f'guess {round}', button = 'OK')
                                elif 0 < player_1_guess < answer :
                                    pyautogui.alert(text = f'⚓ Your guess of {guess} is too low!', title = f'guess {round}', button = 'OK')
                                
                                player_2_guess = int(pyautogui.prompt(text = f'{player_1_name}\'s trun \nguess the number', title = f'round {round}' , default = '0'))
                                
                                if player_2_guess > 50 or player_2_guess <= 0 :
                                    pyautogui.alert(text = '❗ The number you entered is not within the defined range', title = f'guess {round}', button = 'OK')
                                elif 0 < player_2_guess > answer :
                                    pyautogui.alert(text = f'🎈 Your guess of {guess} is too high!', title = f'guess {round}', button = 'OK')
                                elif 0 < player_2_guess < answer :
                                    pyautogui.alert(text = f'⚓ Your guess of {guess} is too low!', title = f'guess {round}', button = 'OK')

                                if player_1_guess == answer :
                                    coins += 2
                                    pyautogui.alert(text = f'🎉 {player_1_name}\'s guess of {guess} is correct!', title = 'winner!', button = 'OK')
                                    break
                                elif player_2_guess == answer :
                                    coins += 2
                                    pyautogui.alert(text = f'🎉 {player_2_name}\'s guess of {guess} is correct!', title = 'winner!', button = 'OK')
                                    break
                                elif round == 5 :
                                    coins += 2
                                    pyautogui.alert(text = f'💣 The answer was number {answer}, \nbut both of you could not guess it', title = 'game over!', button = 'OK')
                        
                    elif level == 'medium\n🙂' :
                        play = pyautogui.confirm(text = 'A number between 1 and 100 \nYou have 4 chances to guess it', title = 'guess the number', buttons = ['play', 'players', 'menu'])
                        if play == 'players' :
                            continue
                        elif play == 'menu' :
                            break
                        elif play == 'play' :
                            player_1_name = pyautogui.prompt(text = 'hi player 1 \nenter your name if you don\'t, \ni will choose name for you hehe 🤭', title = 'name of the player 1' , default = '') 
                            if player_1_name == '' :
                                player_1_name = random.choice(name_list_1)
                                pyautogui.alert(text = f'your name is {player_1_name} from now on 😁', title = 'player 1', button = 'OK')

                            player_2_name = pyautogui.prompt(text = 'hi player 2 \nenter your name if you don\'t, \ni will choose name for you hehe 🤭', title = 'name of the player 2' , default = '') 
                            if player_2_name == '' :
                                player_2_name = random.choice(name_list_2)
                                pyautogui.alert(text = f'your name is {player_2_name} from now on 😁', title = 'player 2', button = 'OK')

                        answer = random.randint(1,100)
                        
                        for round in range(1,7+1) :
                            player_1_guess = int(pyautogui.prompt(text = f'{player_1_name}\'s trun \nguess the number', title = f'round {round}' , default = '0'))
                                
                            if player_1_guess > 50 or player_1_guess <= 0 :
                                pyautogui.alert(text = '❗ The number you entered is not within the defined range', title = f'guess {round}', button = 'OK')
                            elif 0 < player_1_guess > answer :
                                pyautogui.alert(text = f'🎈 Your guess of {guess} is too high!', title = f'guess {round}', button = 'OK')
                            elif 0 < player_1_guess < answer :
                                pyautogui.alert(text = f'⚓ Your guess of {guess} is too low!', title = f'guess {round}', button = 'OK')
                                
                            player_2_guess = int(pyautogui.prompt(text = f'{player_1_name}\'s trun \nguess the number', title = f'round {round}' , default = '0'))
                                
                            if player_2_guess > 50 or player_2_guess <= 0 :
                                pyautogui.alert(text = '❗ The number you entered is not within the defined range', title = f'guess {round}', button = 'OK')
                            elif 0 < player_2_guess > answer :
                                pyautogui.alert(text = f'🎈 Your guess of {guess} is too high!', title = f'guess {round}', button = 'OK')
                            elif 0 < player_2_guess < answer :
                                pyautogui.alert(text = f'⚓ Your guess of {guess} is too low!', title = f'guess {round}', button = 'OK')

                            if player_1_guess == answer :
                                coins += 2
                                pyautogui.alert(text = f'🎉 {player_2_name}\'s guess of {guess} is correct!', title = 'winner!', button = 'OK')
                                break
                            elif player_2_guess == answer :
                                coins += 2
                                pyautogui.alert(text = f'🎉 {player_2_name}\'s guess of {guess} is correct!', title = 'winner!', button = 'OK')
                                break
                            elif round == 7 :
                                coins += 2
                                pyautogui.alert(text = f'💣 The answer was number {answer}, \nbut both of you you could not guess it', title = 'game over!', button = 'OK')
                        

                    elif level == 'hard\n😕' :
                        play = pyautogui.confirm(text = 'A number between 1 and 300 \nYou have 4 chances to guess it', title = 'guess the number', buttons = ['play', 'players', 'menu'])
                        if play == 'players' :
                            continue
                        elif play == 'menu' :
                            break
                        elif play == 'play' :
                            player_1_name = pyautogui.prompt(text = 'hi player 1 \nenter your name if you don\'t, \ni will choose name for you hehe 🤭', title = 'name of the player 1' , default = '') 
                            if player_1_name == '' :
                                player_1_name = random.choice(name_list_1)
                                pyautogui.alert(text = f'your name is {player_1_name} from now on 😁', title = 'player 1', button = 'OK')

                            player_2_name = pyautogui.prompt(text = 'hi player 2 \nenter your name if you don\'t, \ni will choose name for you hehe 🤭', title = 'name of the player 2' , default = '') 
                            if player_2_name == '' :
                                player_2_name = random.choice(name_list_2)
                                pyautogui.alert(text = f'your name is {player_2_name} from now on 😁', title = 'player 2', button = 'OK')

                        answer = random.randint(1,300)
                        
                        for round in range(1,10+1) :
                            player_1_guess = int(pyautogui.prompt(text = f'{player_1_name}\'s trun \nguess the number', title = f'round {round}' , default = '0'))
                                
                            if player_1_guess > 50 or player_1_guess <= 0 :
                                pyautogui.alert(text = '❗ The number you entered is not within the defined range', title = f'guess {round}', button = 'OK')
                            elif 0 < player_1_guess > answer :
                                pyautogui.alert(text = f'🎈 Your guess of {guess} is too high!', title = f'guess {round}', button = 'OK')
                            elif 0 < player_1_guess < answer :
                                pyautogui.alert(text = f'⚓ Your guess of {guess} is too low!', title = f'guess {round}', button = 'OK')
                                
                            player_2_guess = int(pyautogui.prompt(text = f'{player_1_name}\'s trun \nguess the number', title = f'round {round}' , default = '0'))
                                
                            if player_2_guess > 50 or player_2_guess <= 0 :
                                pyautogui.alert(text = '❗ The number you entered is not within the defined range', title = f'guess {round}', button = 'OK')
                            elif 0 < player_2_guess > answer :
                                pyautogui.alert(text = f'🎈 Your guess of {guess} is too high!', title = f'guess {round}', button = 'OK')
                            elif 0 < player_2_guess < answer :
                                pyautogui.alert(text = f'⚓ Your guess of {guess} is too low!', title = f'guess {round}', button = 'OK')

                            if player_1_guess == answer :
                                coins += 2
                                pyautogui.alert(text = f'🎉 {player_2_name}\'s guess of {guess} is correct!', title = 'winner!', button = 'OK')
                                break
                            elif player_2_guess == answer :
                                coins += 2
                                pyautogui.alert(text = f'🎉 {player_2_name}\'s guess of {guess} is correct!', title = 'winner!', button = 'OK')
                                break
                            elif round == 10 :
                                coins += 2
                                pyautogui.alert(text = f'💣 The answer was number {answer}, \nbut both of you could not guess it', title = 'game over!', button = 'OK')
                    else :
                        break

                else :
                    break
                feedback()

         # game number 5 'mousetrap' #
        elif game == 'mousetrap' :
            if unlock_mt == True :
                if play_check_mt == 0 :
                    play_check_mt += 1
                    how_to_play = pyautogui.confirm(text = 'have you ever played mousetrap before?', title = 'coin flip', buttons = ['yes', 'no'])
                    if how_to_play == 'no' :
                        pyautogui.alert(text = 'a mouse is hiding somewhere in the \nscreen,  you have to guess its place \nand set a trap for it, and if you catch \nit, you win. 🕵️', title = 'mousetrap', button = 'got it 🐁')

                play = pyautogui.confirm(text = 'you have 3 chances to find the mouse', title = 'play', buttons = ['play\n🐭', 'menu'])

                if play == 'play\n🐭' :
                    hiding_spot = random.choice(Coordinates_list)
                    for attempt in range(1,3+1) :
                        trap = pyautogui.confirm(text = 'where do you want to place the trap? 🧀', title = f'attempt {attempt}', buttons = ['spot 1 \n ⬅️', 'spot 2 \n ⬇️', 'spot 3 \n ⬆️', 'spot 4 \n ➡️'])

                        if hiding_spot == [790, 530] and trap == 'spot 1 \n ⬅️' :
                            coins += 2
                            pyautogui.moveTo(790, 530, 2)
                            pyautogui.alert(text = f'the mouse was hiding in spot 1 ⬅️ and you found it with {attempt} attempt.', title = 'you caught the mouse', button = 'OK')
                            break
                            
                        elif hiding_spot == [985, 730] and trap == 'spot 2 \n ⬇️' :
                            coins += 2
                            pyautogui.moveTo(985, 730, 2)
                            pyautogui.alert(text = f'the mouse was hiding in spot 2 ⬇️ and you found it with {attempt} attempt.', title = 'you caught the mouse', button = 'OK')
                            pyautogui.alert(text = 'winner winner chicken dinner! \n', title = 'you won the game', button = 'OK')
                            break

                        elif hiding_spot == [985, 325] and trap == 'spot 3 \n ⬆️' :
                            coins += 2
                            pyautogui.moveTo(985, 325, 2)
                            pyautogui.alert(text = f'the mouse was hiding in spot 3 ⬆️ and you found it with {attempt} attempt.', title = 'you caught the mouse', button = 'OK')
                            break

                        elif hiding_spot == [1190, 530] and trap == 'spot 4 \n ➡️' :
                            coins += 2
                            pyautogui.moveTo(1190, 530, 2)
                            pyautogui.alert(text = f'the mouse was hiding in spot 4 ➡️ and you found it with {attempt} attempt.', title = 'you caught the mouse', button = 'OK')
                            break

                        elif hiding_spot != [790, 530] and trap == 'spot 1 \n ⬅️' :
                            pyautogui.moveTo(790, 530, 2)
                            pyautogui.alert(text = f'the mouse wasn\'t hiding in spot 1 ⬅️ ', title = f'attempte {attempt}', button = 'OK')
                            
                        elif hiding_spot != [985, 730] and trap == 'spot 2 \n ⬇️' :
                            pyautogui.moveTo(985, 730, 2)
                            pyautogui.alert(text = f'the mouse wasn\'t hiding in spot 2 ⬇️ ', title = f'attempte {attempt}', button = 'OK')

                        elif hiding_spot != [985, 325] and trap == 'spot 3 \n ⬆️' :
                            pyautogui.moveTo(985, 325, 2)
                            pyautogui.alert(text = f'the mouse wasn\'t hiding in spot 3 ⬆️ ', title = f'attempte {attempt}', button = 'OK')

                        elif hiding_spot != [1190, 530] and trap == 'spot 4 \n ➡️' :
                            pyautogui.moveTo(1190, 530, 2)
                            pyautogui.alert(text = f'the mouse wasn\'t hiding in spot 4 ➡️ ', title = f'attempte {attempt}', button = 'OK')
                        if attempt == 3 :
                            if hiding_spot == [985, 730] :
                                pyautogui.alert(text = 'that was your last chance and you did not \nfound the mouse, it was hiding in spot 2 🐁', title = 'the mouse is still out there!', button = 'menu')
                            elif hiding_spot == [985, 325] :
                                pyautogui.alert(text = 'that was your last chance and you did not \nfound the mouse, it was hiding in spot 3 🐁', title = 'the mouse is still out there!', button = 'menu')
                            elif hiding_spot == [1190, 530] :
                                pyautogui.alert(text = 'that was your last chance and you did not \nfound the mouse, it was hiding in spot 4 🐁', title = 'the mouse is still out there!', button = 'menu')
                            elif hiding_spot == [790, 530] :
                                pyautogui.alert(text = 'that was your last chance and you did not \nfound the mouse, it was hiding in spot 1 🐁', title = 'the mouse is still out there!', button = 'menu')
                else :
                    continue

                feedback()
            
            else :
                buying = pyautogui.confirm(text = 'for playing this game you have to buy it for 5 coins  first', title = 'the game is locked', buttons = ['menu', 'buying this game'])
                if buying == 'buying this game' :
                    if coins >= 5 :
                        buying = pyautogui.confirm(text = 'are you sure about buying this game?', title = 'buying mousetrap', buttons = ['yes', 'no'])
                        if buying == 'yes' :
                            coins -= 5
                            unlock_mt = True
                            pyautogui.alert(text = f'congrats! you bought mouse trap \nand your have {coins} coins left', title = 'mouse trap is unlocked now', button = 'menu')

                    else :
                        pyautogui.alert(text = f'your coins are not enough for buying this game \nyou need 5 coins to buy this \n you only have {coins} coins', title = 'sorry', button = 'menu')

        # game number 6 'truth or dare' #
        elif game == 'truth or dare' :
            if play_check_tod == 0 :
                how_to_play = pyautogui.confirm(text = 'have you ever played truth or dare before?', title = 'truth or dare', buttons = ['yes', 'no'])
                play_check_r += 1
                if how_to_play == 'no' :
                    pyautogui.alert(text = 'truth or dare  is a  game  requiring  two  or \nmore players. players are given the choice \nbetween  answering a  question  truthfully, \nor performing a "dare".', title = 'how to play truth or dare', button = 'got it')
            
            while True :    
                number_of_players = int(pyautogui.prompt(text = 'How many people wants to play', title = 'number_of_players' , default = '2'))
                
                #----this game only accepts 2 - 7 players and if the number of players are too high or too low it warns you till you fix it----#
                while number_of_players < 2 or number_of_players > 7 :
                    if number_of_players < 2 :
                        number_of_players = int(pyautogui.prompt(text = 'this game requires two or more people to play', title = 'not enough players' , default = '2'))
                    else :
                        number_of_players = int(pyautogui.prompt(text = 'this game requires seven or less people to play', title = 'too much players!' , default = '2'))

                for player in range(1,number_of_players+1) :
                    name = pyautogui.prompt(text = f'enter a name for player {player}', title = f'naming player {player}' , default = f'player {player}')
                    players_name_list.append(name)

                rounds = int(pyautogui.prompt(text = 'how many times do you want to play?', title = 'rounds' , default = '2'))
                for round in range(1,rounds+1) :
                    chosen_player = random.choice(players_name_list)
                    players_choice = pyautogui.confirm(text = f'{chosen_player}\'s turn \ntruth  or  dare', title = f'round {round}', buttons = ['truth', 'dare'])
                    if players_choice == 'truth' :
                        truth = random.choice(truth_list)
                        pyautogui.alert(text = f'truth : \n   {truth}', title = f'{chosen_player}\'s turn', button = f'round {round+1}')
                        truth_list.remove(truth)

                    elif players_choice == 'dare' :
                        dare = random.choice(dare_list)
                        pyautogui.alert(text = f'dare : \n   {dare}', title = f'{chosen_player}\'s turn', button = f'round {round+1}')
                        dare_list.remove(dare)
                finall_alert = pyautogui.confirm(text = 'you finished the game', title = 'the game is over', buttons = ['play again', 'menu'])
                coins += 2
                if finall_alert == 'play again' :
                    continue
                else :
                    break
            
            feedback()

    elif menu == 'about us' :
        about_us = pyautogui.confirm(text = 'thank you for playing this game \nhana made this game with love ! \nyou can find more about the creator of the \ngame by clicking on contact hana', title = 'hana made this! 👩‍💻', buttons = ['menu', 'contact hana', 'exit', 'write a review'])
        if about_us == 'exit' :
            exiting = pyautogui.confirm(text = 'are you sure you want to exit the game?', title = 'exit', buttons = ['yes', 'no'])
            if exiting == 'yes' :
                break
        elif about_us == 'contact hana' :
            pyautogui.alert(text = 'you can find hana on : \ninstagram : one.b.y.one \nthreads : one.b.y.one \nwhatsapp : +98 996 211 3243', title = 'hana\'s info', button = 'menu')
        elif about_us == 'write a review' :
            feedback()
    elif menu == 'reviews' :
        if review_list == [] and one_star == two_stars == three_stars == four_stars == five_stars == 0 :
             pyautogui.alert(text = 'there are no rating or reviews yet! 😩', title = 'oops!', button = 'menu')
        
        elif review_list == [] and not one_star == two_stars == three_stars == four_stars == five_stars == 0 :
            pyautogui.alert(text = f'so far we had : \n  {five_stars}   5-star rating ✨\n  {four_stars}   4-star rating 🌟\n  {three_stars}   3-star rating ⭐️\n  {two_stars}   2-star rating ⚡️\n  {one_star}   1-star rating 💫', title = 'ratings and reviews', button = 'menu')

        else :
            while True :
                chosen_review = random.choice(review_list)
                showing_rating = pyautogui.confirm(text = f'so far we had : \n  {five_stars} 5-star rating ✨\n  {four_stars} 4-star rating 🌟\n  {three_stars} 3-star rating ⭐️\n  {two_stars} 2-star rating ⚡️\n  {one_star} 1-star rating 💫\n\nreview : ✍️\n     {chosen_review}', title = 'ratings and reviews', buttons = ['next review', 'menu'])
                if showing_rating == 'menu' :
                    break

    elif menu == 'shop' :
        while True :
            shop = pyautogui.confirm(text = f'you can unlocking the games using coins that \nyou can collect from playing games or using cheat code \nyour have {coins} coins now', title = 'shop', buttons = ['buying mousetrap', 'buying coin flip', 'cheat code', 'menu'])
            if shop == 'buying mousetrap' :
                if unlock_mt == False :
                    if coins >= 5 :
                        buying = pyautogui.confirm(text = 'are sure you about buying this game? \nthis will cost you 5 coins', title = 'buying mouse trap', buttons = ['yes', 'no'])
                        if buying == 'yes' :
                            coins -= 5
                            unlock_mt =  True
                            pyautogui.alert(text = f'congrats! you bought mousetrap \nand your have {coins} left', title = 'mouse trap is unlocked now', button = 'OK')
                    else :
                        pyautogui.alert(text = f'you dont have enough coin to buy this game \nyou need 5 coins to buy this \n you only have {coins} coins', title = 'sorry', button = 'OK')
                else :
                    pyautogui.alert(text = 'this game has already been purchased', title = 'coin flip', button = 'OK')
            
            elif shop == 'buying coin flip' :
                if unlock_cf == False :
                    if coins >= 5 :
                        buying = pyautogui.confirm(text = 'are sure you about buying this game? \nthis will cost you 5 coins', title = 'buying mouse trap', buttons = ['yes', 'no'])
                        if buying == 'yes' :
                            coins -= 5
                            unlock_cf = True
                            pyautogui.alert(text = f'congrats! you bought coin flip \nand your have {coins} left', title = 'coin flip is unlocked now', button = 'OK')
                    else :
                        pyautogui.alert(text = f'you dont have enough coin to buy this game \nyou need 5 coins to buy this \n you only have {coins} coins', title = 'sorry', button = 'OK')
                else :
                    pyautogui.alert(text = 'this game has already been purchased', title = 'coin flip', button = 'OK')

            elif shop == 'cheat code' :
                cheat_code_input = pyautogui.prompt(text = 'for earning 10 coins enter the cheat code \nthat was shown at the wellcoming alert', title = 'cheat code' , default = '')
                if cheat_code_use == 0 :
                    if cheat_code_input == cheat_code :
                        coins += 10
                        cheat_code_use += 1
                        coin_alert = True
                        pyautogui.alert(text = f'you earned 10 coins and now you have {coins} coins', title = 'cograts!', button = 'OK')
                    else :
                        pyautogui.alert(text = 'the code you entered didn\'s match \nthe cheat code please try again', title = 'try again', button = 'OK')
                else :
                    pyautogui.alert(text = 'the cheat code is one-time use and you have already \nused it! for earning more coin you have to play', title = '', button = 'OK')
            else :
                break

    else :
        exiting = pyautogui.confirm(text = 'are you sure you want to exit the game?', title = 'exit', buttons = ['yes', 'no'])
        if exiting == 'yes' :
            break
        else :
            continue
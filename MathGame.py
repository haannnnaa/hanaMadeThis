import random
import pyautogui
# each leve has a different operator list Based on the difficulty of each level

opL1 = ['+', '-']   # opL1 is an abbreviation for operator level 1
opL2 = ['+','*' , '-', '*']
opL3 = ['+','*', '-', '*', '//']
nameList = ['akbar', 'kobra', 'ardeshir', 'soghra']
scoreL1 = 0 
scoreL2 = 0
scoreL3 = 0
nCheck = 0

while True :
    menu = pyautogui.confirm(text='      math game :', title='math game', buttons=['play', 'how to play', 'about us','exit'])
    if menu == 'exit' :
        break
    elif menu == 'how to play' :
        pyautogui.alert(text='are you dumb?\nthat\'s what i thought bish', title='how to play', button='menu')
    elif menu == 'about us' :
        pyautogui.alert(text='hana made it', title='about us', button='menu')
    elif menu == 'play' :

        if nCheck == 0 : 
            player = pyautogui.prompt(text = 'hi friend what\'s your name? \nif you don\'t tell me your name i will call you something that i like hehe ', title = 'lets play!' , default = '')
            nCheck += 1
            if player == '' :
                player = random.choice(nameList)
                pyautogui.alert(text=f'your name is {player} from now on hihi', title=f'{player}', button='OK .__.')

        level = pyautogui.confirm(text = f'it\'s time to choose the difficulty level, {player}', title = 'game difficulty levels', buttons = ['level 1\n(easy)', 'level 2\n(medium)', 'level 3\n(hard)'])

        if level == 'level 1\n(easy)' :
            pyautogui.alert(text='starting level 1, these are the rules :\n \n1_to win this level you must answer\n   answer at least four questions correctly\n \n2_their will be 7 question asked\n \n3_You will be given questions \n   with + and - operators', title='level 1', button='got it')
            for round in range(1,7+1) :
                num1 = random.randint(1,50)
                num2 = random.randint(1,50)
                op1 = random.choice(opL1)
                answer = int(pyautogui.prompt(text = f'What is the answer to the following question?\n{num1} {op1} {num2} = ?', title = f'round {round}' , default = '101'))
                if op1 == '+' :
                    correctAnswer = num1 + num2
                elif op1 == '-' :
                    correctAnswer = num1 - num2
                if answer == correctAnswer :
                    scoreL1 += 1 
                    pyautogui.alert(text = f'your answer was right \nyour score so far : {scoreL1}', title = 'result', button = 'yay!')
                elif answer != correctAnswer :
                    scoreL1 -= 1
                    pyautogui.alert(text = f'your answer was wrong! \nyour score so far : {scoreL1}', title = 'result', button = 'dang!')
            if scoreL1 >= 4 :
                fin = pyautogui.confirm(text = f'you finished level 1 and you won!\nyour final score is  {scoreL1}\nyou can play level 2 now\nif you want to continue playing, click menu otherwise click exit', title = 'congrats', buttons = ['menu','exit'])
            else :
                fin = pyautogui.confirm(text = f'you finished level 1 but you lost!\nyour final score is  {scoreL1}\nfor playing the next level your score should be 4 or higher\nif you want to continue playing, click menu otherwise click exit', title = 'oh shoot', buttons = ['menu','exit'])
            if fin == 'exit' :
                break
        elif level == 'level 2\n(medium)' :
            if scoreL1 >= 4 :
                pyautogui.alert(text='starting level 2, these are the rules :\n \n1_to win this level you must answer\n   answer at least four questions correctly\n \n2_their will be 7 question asked\n \n3_You will be given questions \n   with +, - and * operators', title='level 1', button='got it')
                for round in range(1,7+1) :
                    num1 = random.randint(1,30)
                    num2 = random.randint(1,12)
                    op2 = random.choice(opL2)
                    answer = int(pyautogui.prompt(text = f'What is the answer to the following question?\n{num1} {op2} {num2} = ?', title = f'round {round}' , default = '362'))
                    if op2 == '+' :
                        correctAnswer = num1 + num2
                    elif op2 == '-' :
                        correctAnswer = num1 - num2
                    elif op2 == '*' :
                        correctAnswer = num1 * num2 
                    if answer == correctAnswer :
                        scoreL2 += 1
                        pyautogui.alert(text = f'your answer was right \nyour score so far : {scoreL2}', title = 'result', button = 'yay!')
                    else :
                        scoreL1 -= 1
                        pyautogui.alert(text = f'your answer was wrong! \nyour score so far : {scoreL1}', title = 'result', button = 'dang!')
                if scoreL2 >= 4 :
                    fin = pyautogui.confirm(text = f'you finished level 2 and you won!\nyour final score is  {scoreL2}\nyou can play level 3 now\nif you want to continue playing, click menu otherwise click exit', title = 'congrats', buttons = ['menu','exit'])
                else :
                    fin = pyautogui.confirm(text = f'you finished level 2 but you lost!\nyour final score is  {scoreL2}\nfor playing the next level your score should be 4 or higher\nif you want to continue playing, click menu otherwise click exit', title = 'oh shoot', buttons = ['menu','exit'])
                if fin == 'exit' :
                    break
            else :
                pyautogui.alert(text = f'you can\'t play level 2 because\nthe score of the first level is less than 4\n\nyour current score  {scoreL1}', title = 'leve 2', button = 'menu')
        elif level == 'level 3\n(hard)' :
            if scoreL2 >= 4 :
                pyautogui.alert(text='starting level 3, these are the rules :\n \n1_to win this level you must answer\n   answer at least four questions correctly\n \n2_their will be 7 question asked\n \n3_You will be given questions \n   with +, -, // and * operators', title='level 1', button='got it')
                for round in range(1,7+1) :
                    num1 = random.randint(1,30)
                    num2 = random.randint(1,12)
                    op3 = random.choice(opL3)
                    answer = int(pyautogui.prompt(text = f'What is the answer to the following question?\n{num1} {op3} {num2} = ?', title = f'round {round}' , default = '365'))
                    if op3 == '-' :
                        correctAnswer = num1 - num2
                    elif op3 == '+' :
                        correctAnswer = num1 + num2
                    elif op3 == '*' :
                        correctAnswer = num1 * num2
                    elif op3 == '//' :
                        correctAnswer = num1 // num2
                    if answer == correctAnswer :
                        scoreL3 += 1
                        pyautogui.alert(text = f'your answer was right \nyour score so far : {scoreL3}', title = 'result', button = 'yay!')
                    else :
                        scoreL3 -= 1
                        pyautogui.alert(text = f'your answer was wrong! \nyour score so far : {scoreL3}', title = 'result', button = 'dang!')
                if scoreL3 >= 4 :
                    fin = pyautogui.confirm(text = f'you finished level 3 and you won!\nyour final score is  {scoreL3}\nif you want to continue playing, click menu otherwise click exit', title = 'congrats', buttons = ['menu','exit'])
                else :
                    fin = pyautogui.confirm(text = f'you finished level 3 but you lost!\nyour final score is  {scoreL3}\nfor winning this level your score should be 4 or higher\nif you want to continue playing, click menu otherwise click exit', title = 'oh shoot', buttons = ['menu','exit'])
                if fin == 'exit' :
                    break
            else :
                pyautogui.alert(text = f'you can\'t play level 3 because\nthe score of the second level is less than 4\n\nyour current scores:  \nlevel one  {scoreL1} - level two  {scoreL2}', title = 'leve 3', button = 'menu')
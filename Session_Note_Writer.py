import pyperclip
import random
import setup
import os
import time


# Function that makes the title pop up
def Title():
    os.system('cls')
    print('\033[31m')
    print('  __  __       _   _                 _                     \n'
          ' |  \/  |     | | | |               (_)                    \n'
          ' | \  / | __ _| |_| |__  _ __   __ _ _ ___ _   _ _ __ ___  \n'
          ' | |\/| |/ _` | __| \'_ \| \'_ \ / _` | / __| | | | \'_ ` _ \ \n'
          ' | |  | | (_| | |_| | | | | | | (_| | \__ \ |_| | | | | | |\n'
          ' |_|  |_|\__,_|\__|_| |_|_| |_|\__,_|_|___/\__,_|_| |_| |_|\n'
          '                                                           \n'
          '   _____               _               _   _       _        __          __   _ _            \n'
          '  / ____|             (_)             | \ | |     | |       \ \        / /  (_) |           \n'
          ' | (___   ___  ___ ___ _  ___  _ __   |  \| | ___ | |_ ___   \ \  /\  / / __ _| |_ ___ _ __ \n'
          '  \___ \ / _ \/ __/ __| |/ _ \| \'_ \  | . ` |/ _ \| __/ _ \   \ \/  \/ / \'__| | __/ _ \ \'__|\n'
          '  ____) |  __/\__ \__ \ | (_) | | | | | |\  | (_) | ||  __/    \  /\  /| |  | | ||  __/ |   \n'
          ' |_____/ \___||___/___/_|\___/|_| |_| |_| \_|\___/ \__\___|     \/  \/ |_|  |_|\__\___|_|   ')
    print('\033[0m')
    print('\033[36mDeveloped by https://github.com/VincentWangVW\033[0m')


Title()

# Lists that the program will randomly select phrases from for the session note writer
# TODO add more phrases
greetingList = ['Hello!',
                'Howdy!',
                'Hi!',
                'Greetings!']
endingList = ['Overall, they did fine and worked very hard today. Good job!',
              'They did well overall and put forth a lot of effort today. Well Done!',
              'They performed admirably and demonstrated a strong level of dedication throughout the day!']
scaleList1 = ['very focused and worked hard',
              'super focused and didn\'t stop working',
              'diligently working to finish their math']
scaleList2 = ['not very focused and worked on and off',
              'working hard but often took breaks',
              'diligent in their work, but also made sure to take regular breaks',
              'hardworking but took a lot of breaks']
mistakeList1 = ['They had some mistakes with',
                'There were a few errors with',
                'Some inaccuracies were present in',
                'They encountered a few mistakes with']
mistakeList2 = ['but were soon able to figure out what they were doing wrong and fix it!',
                'but with a little bit of troubleshooting, they identified the issue and resolve it quickly!',
                'but they were eventually able to pinpoint the source of the problem and resolve it!']
mistakeList3 = ['They made some mistakes with it and were able to fix them quickly.',
                'Initially, they encountered some issues but were able to quickly correct them',
                'They came across some errors but were able to solve them efficiently.',
                'They made a few blunders but were able to rectify them swiftly.',
                'They faced some challenges but were able to overcome them by addressing and fixing them promptly.',
                'They encountered some problems but were able to fix them promptly.']
mistakeList4 = ['They made some mistakes with it but were unable to fix their mistakes.',
                'They encountered some errors but were unable to rectify them.',
                'They had some issues with it but couldn\'t find a solution.',
                'They had some inaccuracies but were unable to correct them.',
                'They made some blunders but couldn\'t resolve them.']
mistakeList5 = ['They didn\'t make any major mistakes and were quick to correct the small ones they made.',
                'They were cautious in their approach and quickly corrected any minor errors they encountered.',
                'They didn\'t make any grave mistakes and were quick to fix the small ones.',
                'They were thorough in their work and quickly corrected any minor inaccuracies that occurred.',
                'They were attentive in their work and quickly fixed any small mistakes they encountered.']

# imports name/initial as well as selects a random ending and greeting
ending = random.choice(endingList)
greeting = random.choice(greetingList)
initial = setup.initial()
instructorName = setup.name()
date = input('\033[32mDate: \033[0m')


# Main function for the session note writer
def writer():
    name = input('\033[32mStudent Name: \033[0m')
    Title()
    choice = input(
        'What did the student work on today?\n1. Assessment Only\n2. PK\'s\n3. PK\'s and Mastery Checks\n4. Homework'
        '\n5. PK\'s and Homework\n\033[32mPlease enter the number: \033[0m')
    if choice == '1':
        student_note = name + ' only worked on their assessment today.'
    if choice == '2':
        pk()
        student_note = ' Today ' + name + ' worked on ' + work + '. They were ' + scale + ' the whole time. ' + mistake
    if choice == '3':
        pk()
        title = []
        pf = []
        amount = int(input('\033[32mEnter the amount of mastery checks they completed: \033[0m'))
        if amount == 1:
            mast = input('\033[32mEnter the Mastery check\'s topic: \033[0m')
            ppf = input('\033[32mDid they pass that mastery check (y/: \033[0m')
            if ppf == 'y':
                ppf = 'passed'
            else:
                ppf = 'failed'
            mastery = 'They completed one mastery check and it was about ' + mast + ' and they ' + ppf + '.'
        else:
            bruh = 0
            while amount > bruh:
                bruh1 = bruh + 1
                Title()
                mast = input('\033[32mEnter mastery check #' + str(bruh1) + '\'s topic: \033[0m')
                ppf = input('\033[32mDid they pass that mastery check (y/n): \033[0m')
                if ppf == 'y':
                    ppf = 'passed'
                    pf.append(ppf)
                else:
                    ppf = 'failed'
                    pf.append(ppf)
                title.append(mast)
                bruh = bruh1
                x = 0
            mastery = ''
            while len(title) > x:
                q = x + 1
                mastery = mastery + 'Mastery check #' + str(q) + ' was about ' + str(title[x]) + ' and they ' + str(
                    pf[x]) + '. '
                x = x + 1
            mastery = 'They did ' + str(len(title)) + ' mastery checks. ' + mastery
        student_note = 'Today ' + name + ' worked on ' + work + '. They were ' + scale + ' the whole time. ' + mistake + ' ' + mastery
    if choice == '4':
        hw()
        student_note = 'Today ' + name + ' had homework over ' + a + ' and they worked on it the whole time. ' + c
    if choice == '5':
        hw()
        pk()
        student_note = 'Today ' + name + ' had homework over ' + a + '. ' + c + ' Then they worked on ' + work + '. They were ' + scale + ' the whole time. ' + mistake
    session_note = initial + ' ' + date + ' '
    special_note = input('If no additional notes, press "Enter" to continue!\n\033[32mEnter additional notes: \033[0m')
    Title()
    ringCentral = greeting + ' This is ' + instructorName + ' from Mathnasium. '
    copied_note1 = session_note + student_note + special_note + ' ' + ending
    copied_note2 = ringCentral + student_note + special_note + ' ' + ending
    # TODO make paraphraser
    print('Here is your session note:\n')
    print(f'\033[36m{copied_note1}\033[0m\n\nAbove Message Copied!')
    pyperclip.copy(copied_note1)
    temp = input('\033[32mPress Enter to continue...\033[0m')
    print(f'\n\033[36m{copied_note2}\033[0m\n\nAbove Message Copied!')
    pyperclip.copy(copied_note2)


# Function for homework add-on
def hw():
    global a
    global b
    global c
    a = input('\033[32mWhat was the students homework about: \033[0m')
    b = input('\033[32mDid they make mistakes with their homework? (y/n): \033[0m')
    if b == 'y':
        c = input('\033[32mDid they fix their mistakes? (y/n): \033[0m')
        if c == 'y':
            c = random.choice(mistakeList3)
        else:
            c = random.choice(mistakeList4)
    else:
        c = ''
        b = 'They didn\'t make any mistakes with their homework'


# Function for pk add-on
def pk():
    global work
    global scale
    global mistake
    work = input('\033[32mWhat did they work on: \033[0m')
    scale = input('\033[32mWere they focused (y/n): \033[0m')
    if scale == 'y':
        scale = random.choice(scaleList1)
    else:
        scale = random.choice(scaleList2)
    mistake = input('\033[32mDid they make any mistakes (y/n): \033[0m')
    if mistake == 'y':
        a = input('\033[32mWhat did they make mistakes on: \033[0m')
        b = input('\033[32mWere they able to fix their mistakes (y/n): \033[0m')
        if b == 'y':
            mistake = random.choice(mistakeList1) + a + random.choice(mistakeList2)
        else:
            mistake = random.choice(mistakeList1) + a + ' and may need some more work with it.'
    else:
        mistake = random.choice(mistakeList5)


# Main program, very cool, awesome, developed, etc.
while True:
    Title()
    writer()
    again = input('\033[32mPress "Enter" to continue, Type "n" to leave: \033[0m')
    if again == 'n':
        print('Thank you for using this service!\n'
              '\033[35m |\__/,|   (`\ \n'
              ' |_ _  |.--.) )\n'
              ' ( T   )     /\n'
              '(((^_(((/(((_/\033[0m')
        time.sleep(2)
        break

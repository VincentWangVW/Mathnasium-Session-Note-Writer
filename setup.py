import os
import time


# Creates folder labeled as "Personalized Files" where setup files will be stored
def setup():
    currentDir = os.getcwd()
    fileDir = os.path.join(currentDir, r'Personalized Files')
    if not os.path.exists(fileDir):
        os.makedirs(fileDir)
    setupFile = os.path.join(fileDir, 'setup.txt')
    readME = os.path.join(fileDir, 'README.txt')
    file = open(setupFile, 'w')
    file0 = open(readME,'w')
    file0.write('-----------------------------------------------------------------\n'
                'Welcome to Mathnasium Session Note Writer !\n'
                'The file labeled "setup.txt" is where your name/initial is stored\n'
                'The Format will be "Initial 1","Initial 2","First Name"\n'
                'Ex: "Mai Sakurajima" will be MSMai\n'
                '-----------------------------------------------------------------\n')
    print('\033[36m   _____ ______ _______ _    _ _____  \n'
          '  / ____|  ____|__   __| |  | |  __ \ \n'
          ' | (___ | |__     | |  | |  | | |__) |\n'
          '  \___ \|  __|    | |  | |  | |  ___/ \n'
          '  ____) | |____   | |  | |__| | |     \n'
          ' |_____/|______|  |_|   \____/|_|     \033[0m')
    initial = input('\033[32mPlease enter your initials: \033[0m')
    os.system('cls')
    print('\033[36m   _____ ______ _______ _    _ _____  \n'
          '  / ____|  ____|__   __| |  | |  __ \ \n'
          ' | (___ | |__     | |  | |  | | |__) |\n'
          '  \___ \|  __|    | |  | |  | |  ___/ \n'
          '  ____) | |____   | |  | |__| | |     \n'
          ' |_____/|______|  |_|   \____/|_|     \033[0m')
    name = input('\033[32mPlease enter your first name: \033[0m')
    os.system('cls')
    print('\033[36m   _____ ______ _______ _    _ _____  \n'
          '  / ____|  ____|__   __| |  | |  __ \ \n'
          ' | (___ | |__     | |  | |  | | |__) |\n'
          '  \___ \|  __|    | |  | |  | |  ___/ \n'
          '  ____) | |____   | |  | |__| | |     \n'
          ' |_____/|______|  |_|   \____/|_|     \033[0m')
    print('\033[32mSetup Complete!')
    time.sleep(1)
    print('Closing...')
    time.sleep(2)
    file.write(initial)
    file.write(name)
    file.close()
    file0.close()


# Returns the inputted initials
def initial():
    file = open('Personalized Files\setup.txt', 'r')
    content = file.read(2)
    return content

# Returns the inputted name
def name():
    file = open('Personalized Files\setup.txt', 'r')
    file.read(2)
    content = file.read()
    return content

# Runs the setup feature
if __name__ == "__main__":
    setup()
import random

sonad = ['electricity', 'donkey', 'hardware', 'xerox', 'transistor', 'computer', 'desktop','engineering', 'hangman', 'circuit', 'imagination', 'robot', 'memory', 'power', 'submarine', 'chess', 'resistance', 'matrix', 'function', 'laser', 'mechanism', 'bodyguard', 'titanic', 'global', 'ozone', 'bridge', 'technology', 'spider','pyramid', 'sphere', 'member', 'warning', 'yourself', 'screen', 'language', 'system', 'internet', 'parameter', 'traffic', 'network', 'filter', 'nucleus','automatic', 'microphone', 'cassette', 'operation', 'country', 'beautiful', 'picture', 'teacher', 'superman', 'undertaker', 'alarm', 'process', 'keyboard', 'electron', 'certificate', 'grandfather', 'landmark', 'relativity', 'eraser', 'design', 'football', 'human', 'musician', 'egyptian', 'elephant', 'queen', 'message', 'wallpaper', 'nationality', 'answer', 'wrong', 'statement', 'forest','puzzle', 'voltage', 'current', 'mathematics', 'wisdom', 'dream', 'supermarket','database', 'collection', 'barrier', 'project', 'sunlight', 'figure', 'graph', 'battle', 'hundred', 'signal', 'thousand', 'transformation', 'daughter', 'communication', 'microwave', 'electronic', 'peace', 'wireless', 'delete', 'brain', 'control', 'prophet', 'freedom', 'harbour', 'confidence', 'positive', 'harvest', 'hunger', 'woman', 'children', 'stranger', 'garden', 'pleasure', 'between', 'recognition', 'tomorrow', 'autumn', 'monkey', 'spring', 'winter', 'classification', 'typewriter', 'success', 'difference', 'acoustics', 'astronomy', 'agreement', 'sorrow', 'christmas', 'silver', 'birthday', 'championship', 'friend', 'comfortable', 'diffusion', 'murder', 'policeman', 'science', 'desert', 'basketball', 'blood', 'funeral', 'silence', 'garment', 'merchant', 'spirit', 'punishment', 'measurement', 'ocean', 'digital', 'illusion', 'tyrant', 'castle', 'passion', 'magician', 'remedy', 'knowledge', 'threshold', 'number', 'vision', 'expectation', 'absence', 'mystery', 'morning', 'device', 'thoughts', 'spirit', 'future', 'mountain', 'treasure', 'machine', 'whispering', 'eternity', 'reflection', 'achievement', 'lightning', 'secret', 'environment', 'shepherd', 'confusion', 'grave', 'promise', 'honour', 'reward', 'temple', 'distance', 'eagle', 'saturn', 'finger', 'belief', 'crystal', 'fashion', 'direction', 'captain', 'moment', 'permission', 'logic', 'analysis', 'password', 'english', 'equalizer']

def get_word():
    vastus = random.choice(sonad)
    return vastus.upper()

def game(vastus):
    asona = "-" * len(vastus)  #arvuti sõna
    tehtud = False
    atahed = [] #arvatud tähed
    asonad = [] #arvatud sõnad
    tries = 10

    print("Hangman!")
    print(asona)
    print("\n")

    while not tehtud and tries > 0:

        pakkumine = input("Paku: ").upper()

        if len(pakkumine) == 1 and pakkumine.isalpha():
            if pakkumine in atahed:
                print("Sa juba pakkusid seda! (", pakkumine, ")")
            elif pakkumine not in vastus:
                print("Vale pakkumine")
                asonad.append(pakkumine)
                #tires -=
            else:
                print("Sinu pakutud täht on vastuses!")
                asonad.append(pakkumine)
                vastus_list = list(asona)
                indices = [i for i, letter in enumerate(vastus) if letter == pakkumine]
                for index in indices:
                    vastus_list[index] = pakkumine
                asona = "".join(vastus_list)
                if "_" not in asona:
                    #tehtud = True
                    pass
        elif len(pakkumine) == len(vastus) and pakkumine.isalpha():
                if pakkumine in asonad:
                    print("Sa juba pakkusid seda seda")
                elif pakkumine != vastus:
                    print(pakkumine, "ei ole sobiv")
                    asonad.append(pakkumine)
                    tries -= 1
                else:
                    #tehtud = True
                    asona = vastus
        else:
            print("Mitte sobiv pakkumine.")
        print(asona)
        print("\n")
    if tehtud:
        print("Sa said hakkama!", vastus, "on õige!")

def main():
    vastus = get_word()
    game(vastus)
    while input("Teeme veel? (Y/N) ").upper() =="Y":
        vastus = get_word()
        game(vastus)

if __name__ == "__main__":
    main()




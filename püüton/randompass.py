import random
tahed = "abcdefghijklmnopqrstuvwxyz"
tahed_list = list(tahed) # muudab tahed listiks
parool = input("Sisesta oma parool ")

if any(c not in tahed for c in parool): ## vaatab ega mingi sümbol, mis ei esine muutujas tahed, ei esineks paroolis. any retunib
    print("Keelatud tähemärgid")
else:
    guess = ""
    proov = 0

    while (guess != parool):
        guess = random.choices(tahed_list,k=len(parool)) #random choices- paneb listi suvalisse järjekorda. k näitab listi pikkust e. paneb selle võrduma kasutaja sisestatud koodi pikkusega.
        guess = "".join(guess) #paneb listis olevad sümbolid tagasi kokku
        proov += 1
        print(guess)

        if (guess == parool):
            print("Arvasin su parooli ära", proov, "korraga! Su parool oli", guess, "!")
            break
    


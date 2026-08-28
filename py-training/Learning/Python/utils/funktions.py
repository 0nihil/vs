import sys
import datetime
import subprocess

num = 1

def clear():
  subprocess.run(["clear"])

def templ():
    print("Sehr geehrte Damen und Herren,")
    print("hiermit Bewerbe ich mich auf eine Ausbildung zum [Ausbildungsberuf] in Ihrem Betrieb.")
    print("Mit großem Interesse habe ich Ihre Stellenausschreibung auf [Stellen-Anzeige] gelesen.")
    print("Ich bewerbe mich bei Ihnen weil [Grund].")
    print("Ich habe Erfahrngen mit: [Erfahrung]")
    print("\n")
    print("Anbei mein Lebenslauf und [Zeugniss].")
    print("\n")
    print("Mit freundlichen Grüßen,")
    print("[Name]")

def out():
    global num
    Ausbildungsberuf = input('Ausbildungsberuf: ')
    Anzeige = input('Name der Platform der Stellenanzeige: ')
    Grund = input('Ich bewerbe mich weil...: ')
    Erfahrung = input('Mit was hast du Erfahrung: ')
    Zeugniss = input('Art des Zeugnisses: ')
    Name = input('Name: ')
    time = datetime.datetime.now().strftime(f"BW{num}(%d.%m.%Y %H:%M)")

    num += 1

    with open(f"Python/out/{time}.txt", "w") as f:

        print(f"Sehr geehrte Damen und Herren,",file=f)
        print(f"hiermit Bewerbe ich mich auf eine Ausbildung zum {Ausbildungsberuf} in Ihrem Betrieb.",file=f)
        print(f"Mit großem Interesse habe ich Ihre Stellenausschreibung auf {Anzeige} gelesen.",file=f)
        print(f"Ich bewerbe mich bei Ihnen weil {Grund}.",file=f)
        print(f"Ich habe Erfahrngen mit: {Erfahrung}",file=f)
        print("\n",file=f)
        print(f"Anbei mein Lebenslauf und {Zeugniss}.",file=f)
        print("\n")
        print("Mit freundlichen Grüßen,",file=f)
        print(f"{Name}",file=f)
        
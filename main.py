import random

import colorama as colorama


class Voivodeship:
    def __init__(self, voivodeship_dict):
        self.voivodeship_dict = voivodeship_dict

    def get_random_question(self):
        # wybieramy losowy klucz i wartość ze słownika
        question, answer = random.choice(list(self.voivodeship_dict.items()))
        return question, answer

    def generate_answers(self, correct_answer):
        # generujemy listę odpowiedzi, w tym poprawnej odpowiedzi
        answers = [correct_answer]
        while len(answers) < 4:
            # wybieramy losową wartość ze słownika, ale tylko jeśli nie jest już na liście
            random_answer = random.choice(list(self.voivodeship_dict.values()))
            for similar_answer in list(self.voivodeship_dict.values()):
                if random_answer and similar_answer not in answers:
                    if similar_answer == random_answer:
                        answers.append(random_answer)
                        if len(answers) == 4:
                            break
                    elif similar_answer[0].lower() == correct_answer[0].lower():
                        answers.append(similar_answer)
                        if len(answers) == 4:
                            break

        # losowo przemieszczamy poprawną odpowiedź
        random.shuffle(answers)
        return answers

    def ask_question(self):
        question, correct_answer = self.get_random_question()
        answers = self.generate_answers(correct_answer)

        print(f"\nCo to za rejestracja?: {question}")
        for i, answer in enumerate(answers, start=1):
            print(f"{i}. {answer}")
        while True:
            guess = input("Odpowiedź: ")
            if guess == "0":
                return False
            try:
                guess = int(guess)
                if 1 <= guess <= 4:
                    if guess - 1 == answers.index(correct_answer):
                        print(colorama.Fore.GREEN + "Poprawna odpowiedź!")
                        return True
                    else:
                        print(colorama.Fore.RED + "\nNiepoprawna odpowiedź!")
                        return False
            except ValueError:
                pass


def menu():
    podlaskie = {
        "BAU": "Augustów",
        "BBI": "Bielsk Podlaski",
        "BGR": "Grajewo",
        "BHA": "Hajnówka",
        "BI": "Białystok(miasto)",
        "BIA": "Białystok(powiat)",
        "BKL": "Kolno",
        "BL": "Łomża(miasto)",
        "BLM": "Łomża(powiat)",
        "BMN": "Mońki",
        "BS": "Suwałki",
        "BSE": "Sejny",
        "BSI": "Siemiatycze",
        "BSK": "Sokółka",
        "BSU": "Suwałki",
        "BWM": "Wysokie Mazowieckie",
        "BZA": "Zambrów",
    }
    kujawsko_pomorskie = {
        "CAL": "Aleksandrów Kujawski",
        "CB": "Bydgoszcz(miasto)",
        "CBR": "Brodnica",
        "CBY": "Bydgoszcz(powiat)",
        "CCH": "Chełmno",
        "CG": "Grudziądz",
        "CGR": "Grudziądz(powiat)",
        "CGD": "Golub Dobrzyń",
        "CIN": "Inowrocław",
        "CLI": "Lipno",
        "CMG": "Mogilno",
        "CNA": "Nakło nad Notecią",
        "CRA": "Radziejów",
        "CRY": "Rypin",
        "CSW": "Świecie",
        "CSE": "Sępólno Krajeńskie",
        "CT": "Toruń(miasto)",
        "CTR": "Toruń(powiat)",
        "CTU": "Tuchola",
        "CWA": "Wąbrzeźno",
        "CW": "Włocławek(miasto)",
        "CWL": "Włocławek(powiat)",
        "CZN": "Żnin"
    }
    dolnoslaskie = {
        "DB": "Wałbrzych(miasto)",
        "DBA": "Wałbrzych(powiat)",
        "DBL": "Bolesławiec",
        "DDZ": "Dzierżoniów",
        "DGL": "Głogów",
        "DGR": "Góra",
        "DJ": "Jelenia Góra(miasto)",
        "DJA": "Jawor",
        "DJE": "Jelenia Góra(powiat)",
        "DKA": "Kamienna Góra",
        "DKL": "Kłodzko",
        "DL": "Legnica(miasto)",
        "DLB": "Lubań",
        "DLE": "Legnica(powiat)",
        "DLU": "Lubin",
        "DLW": "Lwówek Śląski",
        "DMI": "Milicz",
        "DOA": "Oława",
        "DOL": "Oleśnica",
        "DPL": "Polkowice",
        "DSR": "Środa Śląska",
        "DST": "Strzelin",
        "DSW": "Świdnica",
        "DTR": "Trzebnica",
        "DW": "Wrocław(miasto)",
        "DWL": "Wołów",
        "DWR": "Wrocław(powiat)",
        "DZA": "Ząbkowice Ślaskie",
        "DZG": "Zgorzelec",
        "DZL": "Złotoryja"
    }
    lodzkie = {
        "EBE": "Bełchatów",
        "EBR": "Brzeziny",
        "EKU": "Kutno",
        "EL": "Łódź(miasto)",
        "ELA": "Łask",
        "ELC": "Łowicz",
        "ELE": "Łęczyca",
        "ELW": "Łódź Wschód",
        "EOP": "Opoczno",
        "EP": "Piotrków Trybunalski(miasto)",
        "EPA": "Pabianice",
        "EPD": "Poddębice",
        "EPI": "Piotrków Trybunalski(powiat)",
        "EPJ": "Pajęczno",
        "ERA": "Radomsko",
        "ERW": "Rawa Mazowiecka",
        "ES": "Skierniewice",
        "ESI": "Sieradz",
        "ESK": "Skierniewice",
        "ETM": "Tomaszów Mazowiecki",
        "EWE": "Wieruszów",
        "EWI": "Wieluń",
        "EZD": "Zduńska Wola",
        "EZG": "Zgierz"
    }
    lubuskie = {
        "FG": "Gorzów Wielkopolski(miasto)",
        "FGW": "Gorzów Wielkopolski(powiat)",
        "FKR": "Krosno Odrzańskie",
        "FMI": "Międzyrzecz",
        "FNW": "Nowa Sól",
        "FSD": "Strzelce Krajeńskie",
        "FSL": "Słubice",
        "FSU": "Sulęcin",
        "FSW": "Świebodzin",
        "FWS": "Wschowa",
        "FZ": "Zielona Góra(miasto)",
        "FZA": "Żary",
        "FZG": "Żagań",
        "FZI": "Zielona Góra(powiat)"
    }
    pomorskie = {
        "GA": "Gdynia",
        "GBY": "Bytów",
        "GCH": "Chojnice",
        "GCZ": "Człuchów",
        "GD": "Gdańsk(miasto)",
        "GDA": "Gdańsk(powiat Pruszcz Gdański)",
        "GKA": "Kartuzy",
        "GKS": "Kościerzyna",
        "GKW": "Kwidzyn",
        "GLE": "Lębork",
        "GMB": "Malbork",
        "GND": "Nowy Dwór Gdański",
        "GPU": "Puck",
        "GS": "Słupsk(miasto)",
        "GSL": "Słupsk(powiat)",
        "GSP": "Sopot",
        "GST": "Starogard Gdański",
        "GSZ": "Sztum",
        "GTC": "Tczew",
        "GWE": "Wejherowo",
        "GWO": "Wejherowo(powiat)"
    }
    malopolskie = {
        "KBC": "Bochnia",
        "KBA": "Bochnia 2",
        "KBR": "Brzesko",
        "KCH": "Chrzanów",
        "KDA": "Dąbrowa Tarnowska",
        "KGR": "Gorlice",
        "KLI": "Limanowa",
        "KMI": "Miechów",
        "KMY": "Myślenice",
        "KN": "Nowy Sącz (miasto)",
        "KNS": "Nowy Sącz (powiat)",
        "KNT": "Nowy Targ",
        "KOL": "Olkusz",
        "KOS": "Oświęcim",
        "KPR": "Proszowice",
        "KR": "Kraków (miasto)",
        "KRA": "Kraków (powiat)",
        "KK": "Kraków(miasto) 2 numeracja",
        "KSU": "Sucha Beskidzka",
        "KT": "Tarnów (miasto)",
        "KTA": "Tarnów (powiat)",
        "KTT": "Zakopane",
        "KWA": "Wadowice",
        "KWI": "Wieliczka"}
    lubelskie = {
        "LB": "Biała Podlaska (miasto)",
        "LBI": "Biała Podlaska (powiat)",
        "LBL": "Biłgoraj",
        "LC": "Chełm (miasto)",
        "LCH": "Chełm (powiat)",
        "LHR": "Hrubieszów",
        "LJA": "Janów Lubelski",
        "LKR": "Kraśnik",
        "LKS": "Krasnystaw",
        "LLB": "Lubartów",
        "LLE": "Łęczna",
        "LLU": "Łuków",
        "LOP": "Opole Lubelskie",
        "LPA": "Parczew",
        "LPU": "Puławy",
        "LRA": "Radzyń Podlaski",
        "LRY": "Ryki",
        "LSW": "Świdnik",
        "LTM": "Tomaszów Lubelski",
        "LU": "Lublin (miasto)",
        "LUB": "Lublin (powiat)",
        "LWL": "Włodawa",
        "LZ": "Zamość (miasto)",
        "LZA": "Zamość (powiat)"}
    warminsko_mazurskie = {
        "NBA": "Bartoszyce",
        "NBR": "Braniewo",
        "NDZ": "Działdowo",
        "NE": "Elbląg(miasto)",
        "NEB": "Elbląg(powiat)",
        "NEL": "Ełk",
        "NGI": "Giżycko",
        "NGO": "Gołdap",
        "NIL": "Iława",
        "NKE": "Kętrzyn",
        "NLI": "Lidzbark Warmiński",
        "NMR": "Mrągowo",
        "NNI": "Nidzica",
        "NNM": "Nowe Miasto Lubawskie",
        "NO": "Olsztyn(miasto)",
        "NOE": "Olecko(od 2002r.)",
        "NOG": "Olecko(do 2002r.)",
        "NOL": "Olsztyn(powiat)",
        "NOS": "Ostróda",
        "NPI": "Pisz",
        "NSZ": "Szczytno",
        "NWE": "Węgorzewo"
    }
    opolskie = {
        "OB": "Brzeg",
        "OGL": "Głubczyce",
        "OK": "Kędzierzyn-Koźle",
        "OKL": "Kluczbork",
        "OKR": "Krapkowice",
        "ONA": "Namysłów",
        "ONY": "Nysa",
        "OOL": "Olesno",
        "OP": "Opole(miasto)",
        "OPO": "Opole(powiat)",
        "OPR": "Prudnik",
        "OST": "Strzelce Opolskie"
    }
    wielkopolskie = {
        "PCH": "Chodzież",
        "PCT": "Czarnków",
        "PGN": "Gniezno",
        "PGO": "Grodzisk Wielkopolski",
        "PGS": "Gostyń",
        "PJA": "Jarocin",
        "PK": "Kalisz(miasto)",
        "PKA": "Kalisz(powiat)",
        "PKE": "Kępno",
        "PKL": "Koło",
        "PKN": "Konin(powiat)",
        "PKO": "Konin(miasto do 2002r.)",
        "PKR": "Krotoszyn",
        "PKS": "Kościan",
        "PL": "Leszno(miasto)",
        "PLE": "Leszno(powiat)",
        "PMI": "Międzychód",
        "PN": "Konin(miasto od 2002r.)",
        "PNT": "Nowy Tomyśl",
        "PO": "Poznań(miasto)",
        "POB": "Oborniki",
        "POS": "Ostrów Wielkopolski",
        "POT": "Ostrzeszów",
        "POZ": "Poznań(powiat do 2002r.)",
        "PP": "Piła",
        "PPL": "Pleszew",
        "PRA": "Rawicz",
        "PSE": "Śrem",
        "PSL": "Słupca",
        "PSR": "Środa Wielkopolska",
        "PSZ": "Szamotuły",
        "PTU": "Turek",
        "PWA": "Wągrowiec",
        "PWL": "Wolsztyn",
        "PWR": "Września",
        "PZ": "Poznań(powiat od 2002r.)",
        "PZL": "Złotów"
    }
    podkarpackie = {
        "RBI": "Ustrzyki Dolne",
        "RBR": "Brzozów",
        "RDE": "Dębica",
        "RJA": "Jarosław",
        "RJS": "Jasło",
        "RK": "Krosno(miasto)",
        "RKL": "Kolbuszowa",
        "RKR": "Krosno(powiat)",
        "RLA": "Łańcut",
        "RLE": "Leżajsk",
        "RLS": "Lesko",
        "RLU": "Lubaczów",
        "RMI": "Mielec",
        "RNI": "Nisko",
        "RP": "Przemyśl(miasto)",
        "RPR": "Przemyśl(powiat)",
        "RPZ": "Przeworsk",
        "RRS": "Ropczyce",
        "RSA": "Sanok",
        "RSR": "Strzyżów",
        "RST": "Stalowa Wola",
        "RT": "Tarnobrzeg(miasto)",
        "RTA": "Tarnobrzeg(powiat)",
        "RZ": "Rzeszów(miasto)",
        "RZE": "Rzeszów(powiat)"
    }
    slaskie = {
        "SB": "Bielsko - Biała(miasto)",
        "SBE": "Będzin",
        "SBI": "Bielsko - Biała(powiat)",
        "SBL": "Bieruńsko - Lędziński",
        "SC": "Częstochowa(miasto)",
        "SCI": "Cieszyn",
        "SCZ": "Częstochowa(powiat)",
        "SD": "Dąbrowa Górnicza",
        "SG": "Gliwice(miasto)",
        "SGL": "Gliwice(powiat)",
        "SH": "Chorzów",
        "SI": "Siemianowice Śląskie",
        "SJ": "Jaworzno",
        "SJZ": "Jastrzębie Zdrój",
        "SK": "Katowice",
        "SKL": "Kłobuck",
        "SL": "Ruda Śląska(od 2002r.)",
        "SLU": "Lubliniec",
        "SM": "Mysłowice",
        "SMI": "Mikołów",
        "SMY": "Myszków",
        "SO": "Sosnowiec",
        "SPI": "Piekary Śląskie",
        "SPS": "Pszczyna",
        "SR": "Rybnik(miasto)",
        "SRB": "Rybnik(powiat)",
        "SRC": "Racibórz",
        "SRS": "Ruda Śląska(do 2002r.)",
        "ST": "Tychy",
        "STA": "Tarnowskie Góry",
        "STY": "Tychy(powiat do 2002r.)",
        "SW": "Świętochłowice",
        "SWD": "Wodzisław Śląski",
        "SY": "Bytom",
        "SZ": "Zabrze",
        "SZA": "Zawiercie",
        "SZO": "Żory",
        "SZY": "Żywiec"
    }
    swietokrzyskie = {
        "TBU": "Busko Zdrój",
        "TJE": "Jędrzejów",
        "TK": "Kielce(miasto)",
        "TKA": "Kazimierza Wielka",
        "TKI": "Kielce(powiat)",
        "TKN": "Końskie",
        "TLW": "Włoszczowa",
        "TOP": "Opatów",
        "TOS": "Ostrowiec Świętokrzyski",
        "TPI": "Pińczów",
        "TSA": "Sandomierz",
        "TSK": "Skarżysko - Kamienna",
        "TST": "Starachowice",
        "TSZ": "Staszów"
    }
    mazowieckie = {
        "WA": "Warszawa Białołęka",
        "WB": "Warszawa Bemowo",
        "WBR": "Białobrzegi",
        "WCI": "Ciechanów",
        "WD": "Warszawa Bielany",
        "WE": "Warszawa Mokotów",
        "WF": "Warszawa Praga Południe",
        "WG": "Garwolin",
        "WGM": "Grodzisk Mazowiecki",
        "WGR": "Grójec",
        "WGS": "Gostynin",
        "WH": "Warszawa Praga Północ",
        "WI": "Warszawa Śródmieście",
        "WJ": "Warszawa Targówek",
        "WK": "Warszawa Ursus",
        "WKZ": "Kozienice",
        "WL": "Legionowo",
        "WLI": "Lipsko",
        "WLS": "Łosice",
        "WM": "Mińsk Mazowiecki",
        "WMA": "Maków Mazowiecki",
        "WML": "Mława",
        "WN": "Warszawa Ursynów",
        "WND": "Nowy Dwór Mazowiecki",
        "WO": "Ostrołęka(miasto)",
        "WOR": "Ostrów Mazowiecka",
        "WOS": "Ostrołęka(powiat)",
        "WOT": "Otwock",
        "WP": "Płock(miasto)",
        "WPI": "Piaseczno",
        "WPL": "Płock(powiat)",
        "WPN": "Płońsk",
        "WPP": "Pruszków(powiat)",
        "WPR": "Pruszków(miasto)",
        "WPS": "Pruszków(powiat 2)",
        "WPU": "Pułtusk",
        "WPY": "Przysucha",
        "WPZ": "Przasnysz",
        "WR": "Radom(miasto)",
        "WRA": "Radom(powiat)",
        "WS": "Siedlce(miasto)",
        "WSC": "Sochaczew",
        "WSE": "Sierpc",
        "WSK": "Sokołów Podlaski",
        "WSI": "Siedlce(powiat)",
        "WSZ": "Szydłowiec",
        "WT": "Warszawa Wawer",
        "WU": "Warszawa Ochota",
        "WV": "Wołomin(od 2003r. - jeszcze nieużywane)",
        "WW": "Warszawa Rembertów, Wilanów, Włochy",
        "WWE": "Węgrów",
        "WWL": "Wołomin",
        "WWY": "Wyszków",
        "WX": "Warszawa Wesoła, Żoliborz",
        "WY": "Warszawa Wola",
        "WZ": "Warszawa Zachód",
        "WZU": "Żuromin",
        "WZW": "Zwoleń",
        "WZY": "Żyrardów"
    }
    zachodniopomorskie = {
        "ZBI": "Białogard",
        "ZCH": "Choszczno",
        "ZDR": "Drawsko Pomorskie",
        "ZGL": "Goleniów",
        "ZGR": "Gryfino",
        "ZGY": "Gryfice",
        "ZK": "Koszalin(miasto)",
        "ZKA": "Kamień Pomorski",
        "ZKL": "Kołobrzeg",
        "ZKO": "Koszalin(powiat)",
        "ZLO": "Łobez",
        "ZMY": "Myślibórz",
        "ZPL": "Police",
        "ZPY": "Pyrzyce",
        "ZS": "Szczecin",
        "ZZ": "Szczecin(nowa pula)",
        "ZSD": "Świdwin",
        "ZSL": "Sławno",
        "ZST": "Stargard",
        "ZSW": "Świnoujście",
        "ZSZ": "Szczecinek",
        "ZWA": "Wałcz"
    }

    print()
    print("0. Exit")
    print("1. Podlaskie")
    print("2. Kujawsko-Pomorskie")
    print("3. Dolnośląskie")
    print("4. Łódzkie")
    print("5. Lubuskie")
    print("6. Pomorskie")
    print("7. Małopolskie")
    print("8. Lubelskie")
    print("9. Warmińsko-Mazurskie")
    print("10. Opolskie")
    print("11. Wielkopolskie")
    print("12. Podkarpackie")
    print("13. Śląskie")
    print("14. Świętokrzyskie")
    print("15. Mazowieckie")
    print("16. Zachodnipomorskie")
    print()

    choice = int(input("Wybierz numer województwa do nauki lub 0 aby wyjść: "))

    if choice == 1:
        voivode = podlaskie
    if choice == 2:
        voivode = kujawsko_pomorskie
    if choice == 3:
        voivode = dolnoslaskie
    if choice == 4:
        voivode = lodzkie
    if choice == 5:
        voivode = lubuskie
    if choice == 6:
        voivode = pomorskie
    if choice == 7:
        voivode = malopolskie
    if choice == 8:
        voivode = lubelskie
    if choice == 9:
        voivode = warminsko_mazurskie
    if choice == 10:
        voivode = opolskie
    if choice == 11:
        voivode = wielkopolskie
    if choice == 12:
        voivode = podkarpackie
    if choice == 13:
        voivode = slaskie
    if choice == 14:
        voivode = swietokrzyskie
    if choice == 15:
        voivode = mazowieckie
    if choice == 16:
        voivode = zachodniopomorskie

    return voivode


def main():
    # inicjalizujemy moduł colorama
    colorama.init(autoreset=True)
    # tworzymy obiekt klasy Voivodeship

    while True:
        try:
            quiz = Voivodeship(menu())

            # pytamy użytkownika, czy chce zagrać w quiz
            while True:
                play = input("Czy chcesz zagrać w quiz? [Tak/Nie]: ")
                if play.lower() == "nie":
                    break
                elif play.lower() == "tak":
                    # uruchamiamy quiz
                    correct = 0
                    total = 1
                    while True:
                        result = quiz.ask_question()
                        if not result:
                            break
                        elif result:
                            correct += 1
                        total += 1

                    # podsumowanie wyników
                    print(f"Twój wynik to: {correct}/{total}\n")

            # kończymy program
            print("Dziękujemy za grę!")
        except UnboundLocalError:
            print()
            print("Do zobaczenia!")
            break
        except ValueError:
            print()
            print("Do zobaczenia!")
            break


if __name__ == "__main__":
    main()
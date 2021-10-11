meanCT = (int(input("Jakie Ct miała dana próbka ?\n")))

if meanCT < 36 and meanCT > 0:
    print("Twoja próbeczka jest zapewne dodatnia, ale sprawdz na pewno czy to nie poziomka")
    print("Jeśli jest wszystko ok sporządź raport i zanieś papiery do nadzorującego")

elif meanCT >= 36 and meanCT <= 38:
    print("Twoja próbeczka jest wątpliwa, weź może popracuj treshholdem i upewnij się\nże wszystko inne jest dobrze ustawione, ewentualnie zapytaj nadzorującego o zdanie")

elif meanCT > 38:
    print("Twoja próbka jest ujemna, wiec nie masz się czym martwić")

elif meanCT < 0:
    print("No no no .... Przecie Ct nie może być ujemne...")
else:
    print("Coś chyba robisz nie tak :P ")


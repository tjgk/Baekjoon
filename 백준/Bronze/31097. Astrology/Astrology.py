y, m, d = map(int, input().split("-"))

if m == 1:
    print("Capricorn" if d <= 19 else "Aquarius")
elif m == 2:
    print("Aquarius" if d <= 18 else "Pisces")
elif m == 3:
    print("Pisces" if d <= 20 else "Aries")
elif m == 4:
    print("Aries" if d <= 19 else "Taurus")
elif m == 5:
    print("Taurus" if d <= 20 else "Gemini")
elif m == 6:
    print("Gemini" if d <= 20 else "Cancer")
elif m == 7:
    print("Cancer" if d <= 22 else "Leo")
elif m == 8:
    print("Leo" if d <= 22 else "Virgo")
elif m == 9:
    print("Virgo" if d <= 22 else "Libra")
elif m == 10:
    print("Libra" if d <= 22 else "Scorpio")
elif m == 11:
    print("Scorpio" if d <= 22 else "Sagittarius")
elif m == 12:
    print("Sagittarius" if d <= 21 else "Capricorn")
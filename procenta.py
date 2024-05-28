def calculate_percentage(num, total):
    if total == 0:
        return 0
    
    percentage = (num / total) * 100
    return percentage

cislo = float(input("Napiš číslo: "))
total = float(input("Napiš celkouvou hodnotu: "))

vysledek = calculate_percentage(cislo, total)
print(f"{cislo} je {vysledek:.2f}% ze {total}")
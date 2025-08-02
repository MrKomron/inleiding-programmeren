#*********************************** Vraag 1 ***********************************#

def nieuwe_datum(maand, jaar, aantal_maanden):
    som=maand+aantal_maanden
    if (maand+aantal_maanden)>12:
        jaar+=1
        result_maand=som-12
    elif som==12:
        jaar=jaar
        result_maand=12
    result=f"{result_maand}-{jaar}"
    return result


print(nieuwe_datum(1, 2023, 1))       # Verwacht: "2-2023"
print(nieuwe_datum(12, 2023, 1))      # Verwacht: "1-2024"
print(nieuwe_datum(5, 2020, 15))      # Verwacht: "8-2021"
print(nieuwe_datum(11, 1999, 25))     # Verwacht: "12-2001"
print(nieuwe_datum(3, 2022, 60))      # Verwacht: "3-2027"


#*********************************** Vraag 2 ***********************************#

# vakken = {
#     "biologie": {"Anna": 70, "Bram": 80, "Caro": 90},
#     "scheikunde": {"Anna": 85, "Bram": 78, "Caro": 92}
# }
#
# resultaat = scores(vakken)
# print(resultaat["biologie"])     # Verwacht: (80.0, 90)
# print(resultaat["scheikunde"])   # Verwacht: (85.0, 92)

#*********************************** Vraag 3 ***********************************#

# print(is_gesorteerd([1, 2, 3]))         # Verwacht: True
# print(is_gesorteerd([3, 2, 1]))         # Verwacht: True
# print(is_gesorteerd([1, 3, 2]))         # Verwacht: False
# print(is_gesorteerd([7]))               # Verwacht: True
# print(is_gesorteerd([]))                # Verwacht: True

#*********************************** Vraag 4 ***********************************#

# r1 = Rechthoek((0, 0), (4, 4))
# r2 = Rechthoek((2, 2), (3, 3))   # Overlap
# r3 = Rechthoek((5, 5), (2, 2))   # Geen overlap
# r4 = Rechthoek((4, 4), (2, 2))   # Raakt hoek
# r5 = Rechthoek((1, 1), (2, 2))   # Volledig binnen
#
# print(r1.overlapt(r2))  # Verwacht: True
# print(r1.overlapt(r3))  # Verwacht: False
# print(r1.overlapt(r4))  # Verwacht: False of True, afhankelijk van hoe je overlap definieert
# print(r1.overlapt(r5))  # Verwacht: True


#*********************************** Vraag 5 ***********************************#


# print(driehoek_pascal(1))
# # Verwacht:
# # 1
#
# print(driehoek_pascal(2))
# # Verwacht:
# # 1
# # 1 1
#
# print(driehoek_pascal(3))
# # Verwacht:
# # 1
# # 1 1
# # 1 2 1
#
# print(driehoek_pascal(5))
# # Verwacht:
# # 1
# # 1 1
# # 1 2 1
# # 1 3 3 1
# # 1 4 6 4 1

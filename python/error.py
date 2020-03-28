try:
    resultat = 1/0
    assert resultat > 0
except ZeroDivisionError:
    print("Divisé par 0 t con")
except AssertionError:
    print("c negatif on veut pas de ca ici")
except:
    print("ca fait bim bam boom")
else: 
    print("Le résultat est ", resultat)
finally:
    print("c fini frero")

raise ValueError("raise yoouuuuuur glass (exception")
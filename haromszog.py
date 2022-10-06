def haromszog() :
    oldal = int(input("Kérem a háromszög oldalának a hosszát: "))
    magassag = int(input("Kérem a háromszög magasságát: "))
    terulet = (magassag * oldal) / 2
    print(f"A háromszög területe: {terulet}")
haromszog()
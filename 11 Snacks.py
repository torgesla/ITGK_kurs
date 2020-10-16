def generate_prime_numbers():  # Returnerer listen med alle primtall opp til 100
    primtall = []
    for tall in range(2, 100):
        isPrime = True
        for primfaktor in primtall:
            if(tall % primfaktor == 0):  # hvis primfaktoren går opp i tallet
                isPrime = False
        if(isPrime):  # Hvis ingen primfaktorer, legg til i listen
            primtall.append(tall)
    return primtall


square_prime_numbers = [x**2 for x in generate_prime_numbers()]

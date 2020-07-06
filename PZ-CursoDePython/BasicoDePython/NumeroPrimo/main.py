#Calcular un número primo
# Un número primo es un numero que solamente es divisible para 2 y para si mismo.
def is_prime(p_number):
    if p_number < 2:
        return False
    elif p_number == 2:
        return True
    elif p_number > 2 and p_number % 2 ==0:
        return False
    else:
        for target_list in range(3,p_number):
            if p_number % target_list == 0:
                return False
    
    return True
        


def run():
    num_prim = int(input("Escribe un número: "))
    print("¿El número es primo? ")
    if is_prime(num_prim):
        print("Tu número es primo")
    else:
        print("Tu número no es primo")


if __name__ == '__main__':
    run()
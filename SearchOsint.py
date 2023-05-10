import socialscan

from termcolor import colored



def search_email_from_phone(phone):

    email = None

    platforms = ["facebook", "twitter", "instagram", "linkedin", "tiktok", "telegram", "whatsapp"]

    for platform in platforms:

        try:

            result = socialscan.search(platform, phone)

            if result and "email" in result:

                email = result["email"]

                break

        except:

            pass

    return email



def search_phone_from_email(email):

    phone = None

    platforms = ["facebook", "twitter", "instagram", "linkedin", "tiktok", "telegram", "whatsapp"]

    for platform in platforms:

        try:

            result = socialscan.search(platform, email)

            if result and "phone" in result:

                phone = result["phone"]

                break

        except:

            pass

    return phone



print(colored("*** SearchOsint ***\n", "red"))

print(colored("rpuebg\n", "cyan"))



while True:

    print("Menu:")

    print("1. Introduzca número de teléfono")

    print("2. Introduzca e-mail")

    print("3. Salir")

    option = input("Elija una opción: ")

    if option == "1":

        phone = input("Introduzca el número de teléfono: ")

        email = search_email_from_phone(phone)

        if email:

            print(f"El correo electrónico asociado a {phone} es {email}")

        else:

            print(f"No se encontró información sobre el número de teléfono {phone}")

    elif option == "2":

        email = input("Introduzca el correo electrónico: ")

        phone = search_phone_from_email(email)

        if phone:

            print(f"El número de teléfono asociado a {email} es {phone}")

        else:

            print(f"No se encontró información sobre el correo electrónico {email}")

    elif option == "3":

        break

    else:

        print("Opción no válida. Por favor, elija una opción válida.")

def chatbot():
    print("Bonjour je suis le chatbox, envoyez moi un message voici les questions")
    print("1. ça va?")
    print("2. que fais tu ?")
    print("3. python?")
    print("4. Pourquoi ?")
    print("5. Non rien?")

    message = input("choisissez votre question (1/2/3/4/5):")
    if message == '5':
        print(" Au revoir!")
        return
    elif message == '1':
        print("Oui et toi?")
    elif message == '2':
        print("Je dev")
    elif message == '3':
        print("JS")
    elif message == '4':
        print("houhouhaha")
    chatbot()

chatbot()
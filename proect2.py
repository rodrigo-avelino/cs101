from cardapio import cardapio

dict_keys = [key for key in cardapio.keys()]


def get_user_input():
    return input("""
    selecione o tipo de cozinha que voce deseja experimentar hoje: Japonesa, Italiana, Arabe, Brasileira, Americana
    """)


def greetings():
    return print("""
    Ola, seja bem-vindo ao mundo na sua mesa restaurante, eu sou o carlos, seu assistente virtual.
    vamos começar!!
    """)

def ini():
    input = get_user_input()
    if input in dict_keys:
        print(cardapio[input])
    else:
        print('''
        Escolha invalida, tente novamente
        ''')
        ini()
        
        
        #if input == 'Japonesa':
        #    print(cardapio['Japonesa'])
        #elif input == 'Italiana':
        #    print(cardapio['Italiana'])
        #elif input == 'Arabe':
        #    print(cardapio['Arabe'])
        #elif input == 'Brasileira':
        #    print(cardapio['Brasileira'])  
        #elif input == 'Americana':
        #    print(cardapio['Americana']) 
    
    
def retry():
    again = input('''
    Deseja ver outro cardapio?(sim,nao)
    ''')
    if again == 'sim':
        return nucleo()



def despedida():
    return print('''
    Origado pela preferencia, volte sempre!!!
    ''')
def programa():
    greetings()
    nucleo()
    despedida()


def nucleo():
    ini()
    retry()




programa()

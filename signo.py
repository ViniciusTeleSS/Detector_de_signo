# Import de bibliotecas
import datetime as dt

# Variaveis
nome = input('Qual é o seu nome? ')
dia = int(input('Qual o dia de seu nascimento? '))
mes = int(input('Qual mês de seu nascimento? '))
ano = int(input('Qual o ano de seu nascimento? '))

# Variaveis de data
data_atual = dt.datetime.now()


# Cálculo de aniversário
print('Olá', nome, 'seja bem vindo(a)')

if mes <= data_atual.month:
    print('Você tem atualmente', data_atual.year - ano, 'anos')
else:
    print('Você tem atualmente', (data_atual.year - 1) - ano, 'anos')

# Definição de signos
# Signo de Aquário
if mes == 1 and dia >= 21 or mes == 2 and dia < 20:
    print('Com base na sua data de nascimento seu signo é: Aquário')
    print('Frase :Elevem seus corações. Cada nova hora traz novas chances. Aos recomeços!')
# Signo de Peixes
elif mes == 2 and dia >= 21 or mes == 3 and dia < 20:
    print('Com base na sua data de nascimento seu signo é: Peixes')
    print('Frase: A melhor coisa que você vai aprender é amar e ser correspondido.')
# Signo de Aries
elif mes == 3 and dia >= 21 or mes == 4 and dia < 20:
    print('Com base na sua data de nascimento seu signo é: Aries')
    print('Frase: Eu sou o mestre do meu destino. Eu sou o capitão da minha alma')
# Signo de Touro
elif mes == 4 and dia >= 21 or mes == 5 and dia < 20:
    print('Com base na sua data de nascimento seu signo é: Touro')
    print('Frase : Aquilo que não te mata, te fortalece.')
# Signo de Gêmeos
elif mes == 5 and dia >= 21 or mes == 6 and dia < 20:
    print('Com base na sua data de nascimento seu signo é: Gêmeos')
    print('Frase: Um dia sem risadas é um dia desperdiçado.')
# Signo de Câncer
elif mes == 6 and dia >= 21 or mes == 7 and dia < 20:
    print('Com base na sua data de nascimento seu signo é: Câncer')
    print('Frase: Eu consigo fazer coisas que você não consegue. Você consegue fazer coisas que eu não consigo. Juntos, podemos fazer coisas incríveis.')
# Signo de Leão
elif mes == 7 and dia >= 21 or mes == 8 and dia < 20:
    print('Com base na sua data de nascimento seu signo é: Leão')
    print('Frase: O seu amor me deixa mais forte. Mas o seu ódio me torna indomável.')
# Signo de Virgem
elif mes == 8 and dia >= 21 or mes == 9 and dia < 20:
    print('Com base na sua data de nascimento seu signo é: Virgem')
    print('Frase: Você ainda não viveu o dia, a menos que tenha feito algo para alguém que nunca poderá te retribuir a boa ação.')
# Signo de Libra
elif mes == 9 and dia >= 21 or mes == 10 and dia < 20:
    print('Com base na sua data de nascimento seu signo é: Libra')
    print('Frase: Se a raça humana quiser ter um período indefinido de prosperidade material, as pessoas terão apenas que se comportar de forma pacífica e prestativa umas com as outras.')
# Signo de Escorpião
elif mes == 10 and dia >= 21 or mes == 11 and dia < 20:
    print('Com base na sua data de nascimento seu signo é: Escorpião')
    print('</br> Frase : Eu não preciso do príncipe encantado para ter meu próprio final feliz.')
# Signo de Sagitário
elif mes == 11 and dia >= 21 or mes == 12 and dia < 20:
    print(' Com base na sua data de nascimento seu signo é: Sagitário')
    print('Frase: Não siga para onde o caminho te leva. Por outro lado, ande onde não há caminho e deixe uma trilha.')
# Signo de Capricórnio
elif mes == 12 and dia >= 21 or mes == 1 and dia < 20:
    print('Com base na sua data de nascimento seu signo é: Capricórnio')
    print('Frase: Existem coisas que são tão sérias, que você precisa rir delas.')

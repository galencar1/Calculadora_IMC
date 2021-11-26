while True:

    altura = float (input('Digite sua altura em metros: '))
    peso = float (input('Digite seu peso em quilogramas: '))


    IMC = peso / (altura ** 2)

    if IMC <= 18.5:
        print (f'Atenção!! Seu IMC é de {IMC:.1f}. Você está abaixo do peso.')

    elif IMC >= 18.6 and IMC <= 24.9:
        print (f'Parabéns! Seu IMC é de {IMC:.1f}. Você está no peso ideal. Continue Assim.')

    elif IMC >= 25.0 and IMC <= 29.9:
        print (f'Atenção!! Seu IMC é de {IMC:.1f}. Você está acima do peso.')

    elif IMC >= 30.0 and IMC <= 34.9:
        print (f'Cuidado!! Seu IMC é de {IMC:.1f}. Você está obeso.')

    elif IMC >= 35.0 and IMC <= 39.9:
        print (f'Cuidado!! Seu IMC é de {IMC:.1f}. Você está no segundo grau de obesidade. Procure ajuda médica!')

    elif IMC >= 40 and IMC <= 100:
        print (f'Muito cuidado!!! Seu IMC é de {IMC:.1f}, o que caracteriza obesidade morbida. Procure ajuda médica URGENTE!')

    else:
        print (' Erro de calculo. Digite novamente.')


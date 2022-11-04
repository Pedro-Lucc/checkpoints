from sklearn import tree

saudavel = 1
normal = 2
estragado = 3

diariamente = 1
as_vezes = 2
dificilmente = 3

# Declarando os valores para considerar entre saudavel, normal e estragado
qualidade = [[10, 30, diariamente, diariamente, diariamente],
             [5, 15, as_vezes, as_vezes, as_vezes],
             [5, 7, estragado, estragado, estragado]]

# Declarando os resultados possíveis
resultados = [saudavel, normal, estragado]

# Construindo uma árvore de decisão
classificador = tree.DecisionTreeClassifier()
classificador = classificador.fit(qualidade, resultados)

print('De acordo com o número de horas por ano (2.592.200h)\n'
      'é aconselhavel que tenhamos boas práticas:'
      '\n- 10% (25.922h) de EXERCÍCIOS FÍSICOS'
      '\n- 30% (777.660h) de HORAS DE SONO'
      '\n- Boas alimentação e absorção de sol diariamente.')

# Gerando inputs para solicitar as informações do usuário
f_exercicios = input('\nCOM QUE FREQUÊNCIA VOCÊ PRATICA ATIVIDADES FÍSICAS? (RESPONDER EM %): ')
f_sono = input('QUAL É A SUA FREQUÊNCIA DE SONO DIARIAMENTE? (RESPONDER EM %): ')
f_frutas = input('COM QUE FREQUÊNCIA VOCÊ COME FRUTAS? --> [1] DIARIAMENTE [2] ÀS VEZES [3] DIFICILMENTE: ')
f_refeicoes = input('COM QUE FREQUÊNCIA VOCÊ FAZ 3 REFEIÇÕES AO DIA?--> [1] DIARIAMENTE [2] ÀS VEZES 3] DIFICILMENTE: ')
f_sol = input('COM QUE FREQUÊNCIA VOCÊ TOMA SOL? --> [1] DIARIAMENTE [2] ÀS VEZES [3] DIFICILMENTE: ')
print('\n')
resultadoUsuario = classificador.predict([[f_exercicios, f_sono, f_frutas, f_refeicoes, f_sol]])

print('=-' * 40)
print('\033[1mVERIFICANDO A SUA SAÚDE ATUAL!!!\033[m')
print('=-' * 40)


# Cálculo do IMC
peso = float(input('\nQUAL É O SEU PESO (Kg)? '))
altura = float(input('QUAL A SUA ALTURA (m)? '))
imc = peso / (altura ** 2)

if resultadoUsuario == 1:
    print(f"\nSEU CORPO ESTARÁ \033[1;32mSAUDÁVEL\033[m \033[1mTIPO BRAD PITT\033[m")
elif resultadoUsuario == 2:
    print(f"\nSEU CORPO ESTARÁ \033[1;33mNORMAL\033[m. \033[1mBONITINHO VAI :)\033[m")
elif resultadoUsuario == 3:
    print(f"\nSEU CORPO ESTARÁ \033[1;32mESTRAGADO\033[m TA \033[1mFAZENDO O QUE DA VIDA AMIGO, QUER MORRER?!?!\033[m")

# Condições  do IMC
print(f"Seu IMC é: {imc:.2f}")

if imc < 16:
    print("\033[1mMagreza grave")
elif imc < 17:
    print("\033[1mMagreza moderada")
elif imc < 18.5:
    print("\033[1mMagreza leve")
elif imc < 25:
    print("\033[1mSaudável")
elif imc < 30:
    print("\033[1mSobrepeso")
elif imc < 35:
    print("\033[1;33mObesidade Grau I")
elif imc < 40:
    print("\033[1;34mObesidade Grau II (severa)")
else:
    print("\033[1;31mObesidade Grau III (mórbida)")

















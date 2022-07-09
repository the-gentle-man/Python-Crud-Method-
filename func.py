import pymysql.cursors


class Funcao:

    @staticmethod
    def operador(operacao):
        conexao = pymysql.connect(
        host='localhost',
        user='root',
        password='Teste@386',
        database='gamestore',
        cursorclass=pymysql.cursors.DictCursor
        )
        cursor = conexao.cursor()

        match operacao:
            case 'CREATE':
                colunas = ('Nome', 'Sobrenome', 'Idade', 'Plataforma')
                valorinserido = []

                for valor in range(4):
                    entrada = input(f'Digite o valor do campo: {colunas[valor]}\n')
                    if valor == 0:
                        entrada = entrada.strip(' ')
                        while not entrada.isalpha():
                            entrada = input('\nValor inválido, digite novamente:\n')
                        while len(entrada) > 20:
                            entrada = input('\nOs nomes tem de ser de no máximo 20 caracteres, digite novamente:\n')

                        entrada = entrada.capitalize()

                    elif valor == 1:
                        invalidanumero = entrada.replace(' ', '')
                        while not invalidanumero.isalpha():
                            entrada = input('\nValor inválido, digite novamente:\n')
                            invalidanumero = entrada.replace(' ', '')

                        entrada = entrada.split(' ')
                        for item in range(len(entrada)):
                            entrada[item] = entrada[item].capitalize()

                        entrada = ' '.join(entrada)

                    elif valor == 2:
                        while entrada.isnumeric() == False or int(entrada) > 150:
                            entrada = input('\nValor inválido! Digite novamente:\n')

                    elif valor == 3:
                        while len(entrada) > 20:
                            entrada = input('\nEste campo precisa ter 20 caracteres, digite novamente:\n')
                    valorinserido.append(entrada)

                comando = 'INSERT INTO clientes(nome, sobrenome, idade, plataforma) VALUES' \
                          '(%s, %s, %s, %s)'

                cursor.execute(comando, valorinserido)
                conexao.commit()
                cursor.close()
                conexao.close()

                print('\nRegistro inserido com sucesso!\n')
                reposta = input('\nDeseja inserir mais um registro?(S/N)\n')

                while reposta.upper() != 'S' and reposta.upper() != 'N':
                    reposta = input('\nDigite um valor válido:(S/N)\n')

                if reposta.upper() == 'S':
                    Funcao.operador('CREATE')
                else:
                    pass

            case 'READ':
                comando = f'SELECT * FROM clientes'
                cursor.execute(comando)
                result = cursor.fetchall()
                for linha in result:
                    print(f'\t{linha}')

                cursor.close()
                conexao.close()

            case 'UPDATE':
                idselecionado = input('Selecione o id(apenas números):\n')

                validacao = f'SELECT * FROM clientes WHERE id_cli = "{idselecionado}"'

                while not cursor.execute(validacao):
                    idselecionado = input('Id não encontrado, digite novamente: ')
                    validacao = f'SELECT * FROM clientes WHERE id_cli = "{idselecionado}"'

                campo = input('\nSelecione o campo que você deseja alterar: \n'
                                '[1] - Nome\n'
                                '[2] - Sobrenome\n'
                                '[3] - Idade\n'
                                '[4] - Plataforma\n')

                match campo:

                    case '1':
                        novonome = input('Digite o novo valor do campo Nome:\n')

                        novonome = novonome.strip(' ')

                        while not novonome.isalpha():
                            novonome = input('\nNúmeros não são aceitos, digite novamente:\n')
                        while len(novonome) > 20:
                            novonome = input('\nOs nomes tem de ser de no máximo 20 caracteres, digite novamente:\n')

                        novonome = novonome.capitalize()

                        comando = f'UPDATE clientes SET nome = "{novonome}" WHERE id_cli = "{idselecionado}"'
                        cursor.execute(comando)
                        conexao.commit()
                        print('\nRegistro alterado com sucesso!\n')

                        cursor.close()
                        conexao.close()

                    case '2':
                        novosobrenome = input('Digite o novo valor do campo Sobrenome:\n')
                        invalidanumero = novosobrenome.replace(' ', '')
                        while not invalidanumero.isalpha():
                            novosobrenome = input('\nValor inválido, digite novamente:\n')
                            invalidanumero = novosobrenome.replace(' ', '')

                        novosobrenome = novosobrenome.split(' ')

                        for item in range(len(novosobrenome)):
                            novosobrenome[item] = novosobrenome[item].capitalize()

                        novosobrenome = ' '.join(novosobrenome)

                        comando = f'UPDATE clientes SET sobrenome = "{novosobrenome}" WHERE id_cli = "{idselecionado}"'
                        cursor.execute(comando)
                        conexao.commit()
                        print('\nRegistro alterado com sucesso!\n')

                        cursor.close()
                        conexao.close()

                    case '3':
                        novaidade = input('Digite o novo valor do campo Idade\n')
                        while novaidade.isnumeric() == False or int(novaidade) > 150:
                            novaidade = input('\nValor inválido! Digite novamente:\n')

                        comando = f'UPDATE clientes SET idade = "{novaidade}" WHERE id_cli = "{idselecionado}"'
                        cursor.execute(comando)
                        conexao.commit()
                        print('\nRegistro alterado com sucesso!\n')

                        cursor.close()
                        conexao.close()

                    case '4':
                         novaplataforma = input('Digite o novo valor do campo Plataforma\n')
                         while len(novaplataforma) > 20:
                             novaplataforma = input('\nEste campo precisa ter 20 caracteres, digite novamente:\n')

                         comando = f'UPDATE clientes SET plataforma = "{novaplataforma}" WHERE id_cli = "{idselecionado}"'
                         cursor.execute(comando)
                         conexao.commit()
                         print('\nRegistro alterado com sucesso!\n')

                         cursor.close()
                         conexao.close()

                    case _:
                        campo = input('Valor inválido, digite novamente: \n'
                                '[1] - Nome\n'
                                '[2] - Sobrenome\n'
                                '[3] - Idade\n'
                                '[4] - Plataforma\n')

            case 'DELETE':
                idselecionado = input('Selecione o id(apenas números):\n')
                validacao = f'SELECT * FROM clientes WHERE id_cli = "{idselecionado}"'

                while not cursor.execute(validacao):
                    idselecionado = input('\nId não encontrado, digite novamente:\n')
                    validacao = f'SELECT * FROM clientes WHERE id_cli = "{idselecionado}"'

                comando = f'DELETE FROM clientes WHERE id_cli = "{idselecionado}"'
                cursor.execute(comando)
                conexao.commit()
                print('\nRegistro deletado com sucesso!\n')

                cursor.close()
                conexao.close()
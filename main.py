from func import Funcao

opcao = input('Escolha uma opção: \n'
              '[1](C) - Inserir\n'
              '[2](R) - Listar\n'
              '[3](U) - Alterar\n'
              '[4](D) - Deletar\n'
              '[5] - Sair\n'
              )

while opcao != '5':

    match opcao:

        case '1':
            Funcao.operador('CREATE')
            opcao = input('\nEscolha uma opção: \n'
                  '[1](C) - Inserir\n'
                  '[2](R) - Listar\n'
                  '[3](U) - Alterar\n'
                  '[4](D) - Deletar\n'
                  '[5] - Sair\n'
                  )

        case '2':
            Funcao.operador('READ')
            opcao = input('\nEscolha uma opção: \n'
                          '[1](C) - Inserir\n'
                          '[2](R) - Listar\n'
                          '[3](U) - Alterar\n'
                          '[4](D) - Deletar\n'
                          '[5] - Sair\n'
                          )

        case '3':
            Funcao.operador('UPDATE')
            opcao = input('\nEscolha uma opção: \n'
                          '[1](C) - Inserir\n'
                          '[2](R) - Listar\n'
                          '[3](U) - Alterar\n'
                          '[4](D) - Deletar\n'
                          '[5] - Sair\n'
                          )

        case '4':
            Funcao.operador('DELETE')
            opcao = input('\nEscolha uma opção: \n'
                          '[1](C) - Inserir\n'
                          '[2](R) - Listar\n'
                          '[3](U) - Alterar\n'
                          '[4](D) - Deletar\n'
                          '[5] - Sair\n'
                          )

        case _:
            opcao = input('\nInsira uma opção válida(de 1 a 5)\n'
                          '[1](C) - Inserir\n'
                          '[2](R) - Listar\n'
                          '[3](U) - Alterar\n'
                          '[4](D) - Deletar\n'
                          '[5] - Sair\n')
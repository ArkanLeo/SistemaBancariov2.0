import textwrap

def saque(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= limite_saques
    if limite_saques == 0:
        print("Limite de saques diário excedido.")

    elif excedeu_saldo:
        print("Operação falhou! Valor de saque excedido.")

    elif valor > 0:
        saldo -= valor
        extrato += f"Saque: R${valor:.2f} realizado com sucesso.\n"
        print(f"Saque: R${valor:.2f} realizado com sucesso.\n")
        numero_saques -= 1

    elif excedeu_saldo:
        print("Operação falhou! Valor de saque maior que saldo disponível.")

    else:
        print("Operação falhou! Tente novamente.")

    return saldo, extrato

def depositar(saldo, vdepos, extrato, /):
    if vdepos > 0:
        saldo += vdepos
        extrato += f"Depósito: R${vdepos:.2f} realizado com sucesso.\n"
        print(f"Depósito: R${vdepos:.2f} realizado com sucesso.\n")
    else:
        print("Operação falhou! O valor informado é inválido.")

    return saldo, extrato


def historico(saldo, /, *, extrato):
    print("*" * 15 + "Extrato" + "*" * 15)
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\n\nSaldo disponível de R${saldo:.2f}.")
    print("*" * 37)


def criar_usuario(usuarios):
    cpf = input('Informe o CPF (somente números): ')
    usuario = filtrar_usuario(cpf, usuarios)
    if usuario:
        print('\nJá existe usuário com o mesmo CPF')
        return

    nome = input('Informe o nome completo: ')
    data_nascimento = input('Informe a data de nascimento: ')
    endereco = input('Digite seu endereço (logradouro, nro - bairro - cidade/sigla estado): ')

    usuarios.append({'nome': nome, 'data_nascimento': data_nascimento, 'cpf': cpf, 'endereco': endereco})
    print('Usuários criados com sucesso!')

def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario['cpf'] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_conta(agencia, numero_conta, usuarios):
    cpf = input('Informe o CPF do usuário: ')
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print('Conta criada com sucesso!')
        return {'agencia': agencia, 'numero_conta': numero_conta, 'usuario': usuario}

    print('\nUsuário não encontrado, fluxo de criação de conta encerrado.')


def listar_contas(contas):
    for conta in contas:
        linha = f"""\
            Agência:\t{conta['agencia']}
            C/C:\t\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['nome']}
        """
        print('=' * 100)
        print(textwrap.dedent(linha))


menu = """
[d]   Depositar
[s]   Sacar
[e]   Extrato
[nc]  Nova Conta
[lc]  Listar Contas
[nu]  Novo Usuário
[q] Sair

=> """
AGENCIA = "0001"

saldo = 0
limite = 500
extrato = ''
numero_saques = 0
LIMITE_SAQUES = 3
usuarios = list()
contas = list()

while True:

    opcao = input(menu)
    if opcao == 'd':
        vdepos = float(input("Digite o valor do depósito: "))
        saldo, extrato = depositar(saldo, vdepos, extrato)

    elif opcao == 's':
        valor = float(input("Digite o valor para saque: "))

        saldo, extrato = saque(
            saldo=saldo,
            valor=valor,
            extrato=extrato,
            limite=limite,
            numero_saques=numero_saques,
            limite_saques=LIMITE_SAQUES
        )

    elif opcao == 'e':
        historico(saldo, extrato=extrato)

    elif opcao == 'q':
        print("Muito obrigado(a)! Volte sempre ;)")
        break

    elif opcao == 'nu':
        criar_usuario(usuarios)

    elif opcao == 'nc':
        numero_conta = len(contas) + 1
        conta = criar_conta(AGENCIA, numero_conta, usuarios)

        if conta:
            contas.append(conta)

    elif opcao == "lc":
        listar_contas(contas)

    else:
        print("Opção inválida, por favor selecione novamente a opção desejada.")

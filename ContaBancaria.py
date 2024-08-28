class ContaBancaria:
    def __init__(self):
        self.saldo = 0
        self.depositos = []
        self.saques = []
        self.limite_saques = 3
        self.saques_realizados = 0
        self.limite_por_saque = 500

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            self.depositos.append(valor)
            print(f"Depósito de R$ {valor:.2f} realizado com sucesso!")
        else:
            print("Valor de depósito inválido.")

    def sacar(self, valor):
        if self.saques_realizados < self.limite_saques and valor <= self.limite_por_saque and valor <= self.saldo:
            self.saldo -= valor
            self.saques.append(valor)
            self.saques_realizados += 1
            print(f"Saque de R$ {valor:.2f} realizado com sucesso!")
        else:
            if self.saques_realizados >= self.limite_saques:
                print("Limite de saques diários atingido.")
            elif valor > self.limite_por_saque:
                print("Valor do saque excede o limite por operação.")
            else:
                print("Saldo insuficiente.")

    def extrato(self):
        print("\nExtrato Bancário")
        print("-" * 30)
        for deposito in self.depositos:
            print(f"Depósito: R$ {deposito:.2f}")
        for saque in self.saques:
            print(f"Saque: R$ {saque:.2f}")
        print("-" * 30)
        print(f"Saldo: R$ {self.saldo:.2f}")

# Criando uma instância da conta
conta = ContaBancaria()

while True:
    print("\nOperações disponíveis:")
    print("1. Depósito")
    print("2. Saque")
    print("3. Extrato")
    print("4. Sair")

    opcao = int(input("Digite a opção desejada: "))

    if opcao == 1:
        valor = float(input("Digite o valor do depósito: "))
        conta.depositar(valor)
    elif opcao == 2:
        valor = float(input("Digite o valor do saque: "))
        conta.sacar(valor)
    elif opcao == 3:
        conta.extrato()
    elif opcao == 4:
        break
    else:
        print("Opção inválida.")

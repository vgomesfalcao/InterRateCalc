from cartao import Cartao
n=0
Cartao.ler()

while(not(n == -1)):
    
    listar = '1 - Listar Todas as Operadoras\n'
    add = '2 - Adicionar Operadora\n'
    exc = '3 - Excluir Operadora\n'
    sim = '4 - Simular Venda\n'
    sal = '5 - Salvar\n'
    ler = '6 - Ler arquivo Db\n'
    sim2 = '7 - Simular Vendas\n'
    sair = '-1 - Sair\n'
    n = int(input(listar+add+exc+sim+sal+ler+sim2+sair))
    if(n == 1):
        for op in Cartao.cartoes:
            print(op)
    elif(n == 2):
        Cartao.adiciona_operadora()
    elif(n == 3):
        print(Cartao.excluir_operadora())
    elif(n == 4):
        vlr = float(input('Digite o valor:\n'))
        num_parc = int(input('Digite num_parc:\n'))
        for op in Cartao.cartoes:
            print(f'{op.operadora.upper()} : R${op.sim_vlr_credito(vlr,num_parc):.2f}'.replace('.',','))
    elif(n == 5):
        Cartao.salvar()
    elif(n == 6):
        Cartao.ler()
    elif(n == 7):
        Cartao.simular()
    print('\n\n')

from card import Card
n=0
Card.read()

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
        for op in Card.cards:
            print(op)
    elif(n == 2):
        Card.add_company()
    elif(n == 3):
        Card.del_company()
    elif(n == 4):
        vlr = float(input('Digite o valor:\n'))
        num_parc = int(input('Digite num_parc:\n'))
        for op in Card.cards:
            print(f'{op.operadora.upper()} : R${op.sim_vlr_credito(vlr,num_parc):.2f}'.replace('.',','))
    elif(n == 5):
        Card.save()
    elif(n == 6):
        Card.read()
    elif(n == 7):
        Card.simular()
    print('\n\n')

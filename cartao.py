import yaml
arq = 'dados.bin'
class Cartao:
    cartoes = []
    vendas = {'Debito': 18004.89, '1x':11360.47, '2x':1754.43,'3x':1001.92}
    def __init__(self, operadora,debito,credito_avista, credito_1x, credito_nx, tx_antecipacao,aluguel,compra):
        self.__operadora = operadora
        self.__debito = debito/100
        self.__credito_1x  = credito_1x/100
        self.__credito_nx = credito_nx/100
        self.__tx_antecipacao = tx_antecipacao/100
        self.__credito_avista = credito_avista/100
        self.__aluguel = aluguel
        self.__compra = compra

    @property
    def operadora(self):
        return self.__operadora
    @classmethod
    def adiciona_operadora(cls):
        nome = input('Digite o nome da Operadora\n').upper()
        debito = float(input('Digite a taxa de Debito: (em %)\n'))
        creditov = float(input('Digite a taxa de Crédito à vista:\n'))
        credito1x = float(input('Digite a taxa de Credito primeira Parcela:\n'))
        creditonx = float(input('Digite a taxa de Credito 2x-6x:\n'))
        ant = input('Digite a taxa de antecipação se houver:\n')
        if (ant == ''):
            ant = 0.00
        else:
            ant = float(ant)
        alug = input('Digite o valor do aluguel da maquina se houver:\n')
        if (alug == ''):
            alug = 0.00
        else:
            alug = float(alug)
        comp = input('Digite o valor da compra da maquina se houver:\n')
        if (comp == ''):
            comp = 0.00
        else:
            comp = float(comp)
        cls.cartoes.append(Cartao(nome,debito,creditov,credito1x,creditonx,ant,alug,comp))
        
    def sim_vlr_credito(self,vlr, num_parc):
        vlr_parcela = vlr/num_parc
        if (num_parc > 1):
            result = (vlr_parcela*self.__credito_1x) + (num_parc-1)*(vlr_parcela*self.__credito_nx)
        else:
            result = (vlr_parcela*self.__credito_1x)
        return result

    def __str__(self):
        nome = f'Operadora {self.__operadora}\n'
        deb = f'Debito: {self.__debito*100:.4}%\n'
        credv = f'Credito à vista: {self.__credito_avista*100:.4}%\n'
        cred1 = f'Credito Primeira Parcela: {self.__credito_1x*100:.4}%\n'
        credn = f'Credito A partir da Segunda:{self.__credito_nx*100:.4}%\n'
        ant = f'Taxa Antecipação: {self.__tx_antecipacao*100:.4}%\n'
        alug = f'Aluguel: R${self.__aluguel:.4}\n'
        comp = f'Compra: R${self.__compra:.4}\n'
        return nome + deb + credv + cred1 + credn + ant + alug + comp
    @classmethod
    def salvar(cls):
        with open(arq,'w') as arquivo:
            dado = yaml.dump(cls.cartoes)
            arquivo.write(dado)
    @classmethod
    def ler(cls):
        with open(arq,'r') as db:
            txt = yaml.load(db,Loader=yaml.FullLoader)
            if txt != None:
                cls.cartoes = txt
    @classmethod
    def excluir_operadora(cls):
        if cls.cartoes == []:
            return 'Não há itens para Excluir'
        else:
            operadora = input('Digite a operadora para excluir:\n')
            op = cls.pesquisar_op(operadora)
            if (op):
                cls.cartoes.remove(op)
                return operadora +' Deletada'
        
    @classmethod
    def pesquisar_op(cls, operadora):
        for op in cls.cartoes:
            if (operadora.upper() == op.operadora):
                return op
        return False
    @classmethod
    def simular(cls):
        for op in cls.cartoes:
            
            deb = cls.vendas['Debito'] * op.__debito
            x1 = cls.vendas['1x'] * op.__credito_avista
            x2 = ((cls.vendas['2x']/2) * op.__credito_1x) + ((cls.vendas['2x']/2)* op.__credito_nx)
            x3 = ((cls.vendas['3x']/3) * op.__credito_1x) + (2*((cls.vendas['3x']/3)* op.__credito_nx))
            compra = op.__compra/12
            ant1 = (cls.vendas['1x'] - x1)*op.__tx_antecipacao
            ant2 = (cls.vendas['2x'] - x2)*op.__tx_antecipacao*2
            ant3 = (cls.vendas['3x'] - x3)*op.__tx_antecipacao*3
            ant = ant1 + ant2 + ant3
            print(op.__operadora)
            debi = f'Debito: R$ {deb:.2f}\n'
            cred1x = f'Credito à Vista: R$ {x1:.2f}\n'
            cred2x = f'Credito 2x: R$ {x2:.2f}\n'
            cred3x = f'Credito 3x: R$ {x3:.2f}\n'
            alu = f'Aluguel: R${op.__aluguel:.2f}\n'
            com = f'Valor Compra mensal: R${compra:.2f}\n'
            ante = f'Antecipação: R$ {ant:.2f}\n'
            total = f'Total: R$ {deb+x1+x2+x3+compra+op.__aluguel+ant:.2f}\n'
            print((debi + cred1x + cred2x + cred3x + ante + alu + com + total).replace('.',','))
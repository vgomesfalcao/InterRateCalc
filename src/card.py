import yaml
data_file = '../db/dados.bin'
class Card:
    cards = []
    sales = {'Debit': 18004.89, '1x':11360.47, '2x':1754.43,'3x':1001.92}
    def __init__(self, company,debit,credit_incash, credit_1x, credit_nx, antecipation_rate,rental,purchase):
        self.__company = company
        self.__debit = debit/100
        self.__credit_1x  = credit_1x/100
        self.__credit_nx = credit_nx/100
        self.__antecipation_rate = antecipation_rate/100
        self.__credit_incash = credit_incash/100
        self.__rental = rental
        self.__purchase = purchase

    @property
    def company(self):
        return self.__company
    @classmethod
    def add_company(cls):
        name = input('Enter company name\n').upper()
        debit = float(input('Enter debit rate: (in %)\n'))
        credit_incash = float(input('Enter credit in cash rate:\n'))
        credit1x = float(input('Enter credit 1x rate:\n'))
        creditnx = float(input('Enter credit 2x-6x rate:\n'))
        ant = input('Enter atecipation rate:\n')
        if (ant == ''):
            ant = 0.00
        else:
            ant = float(ant)
        alug = input('Enter the machine rental if exists:\n')
        if (alug == ''):
            alug = 0.00
        else:
            alug = float(alug)
        comp = input('Enter machine purchase value if exists:\n')
        if (comp == ''):
            comp = 0.00
        else:
            comp = float(comp)
        cls.cards.append(Card(name,debit,credit_incash,credit1x,creditnx,ant,alug,comp))
        
    def sim_vlr_credit(self,vlr, num_parc):
        vlr_parcela = vlr/num_parc
        if (num_parc > 1):
            result = (vlr_parcela*self.__credit_1x) + (num_parc-1)*(vlr_parcela*self.__credit_nx)
        else:
            result = (vlr_parcela*self.__credit_1x)
        return result

    def __str__(self):
        name = f'company {self.__company}\n'
        deb = f'debit: {self.__debit*100:.4}%\n'
        credv = f'credit in cash: {self.__credit_incash*100:.4}%\n'
        cred1 = f'credit first installment: {self.__credit_1x*100:.4}%\n'
        credn = f'credit from the second installment:{self.__credit_nx*100:.4}%\n'
        ant = f'Antecipation rate: {self.__antecipation_rate*100:.4}%\n'
        alug = f'Rental Value: R${self.__rental:.4}\n'
        comp = f'Purchase Value: R${self.__purchase:.4}\n'
        return name + deb + credv + cred1 + credn + ant + alug + comp
    
    @classmethod
    def save(cls):
        with open(data_file,'w') as data:
            dado = yaml.dump(cls.cards)
            data.write(dado)
            
    @classmethod
    def read(cls):
        with open(data_file,'r') as db:
            txt = yaml.load(db,Loader=yaml.FullLoader)
            if txt != None:
                cls.cards = txt
                
    @classmethod
    def del_company(cls):
        if cls.cards == []:
            return 'There are no items to delete'
        else:
            company = input('Enter company name to delete:\n')
            op = cls.search_op(company)
            if (op):
                cls.cards.remove(op)
                return company +' Deleted'
        
    @classmethod
    def search_op(cls, company):
        for op in cls.cards:
            if (company.upper() == op.company):
                return op
        return False
    
    @classmethod
    def simular(cls):
        for op in cls.cards:
            deb = cls.sales['debit'] * op.__debit
            x1 = cls.sales['1x'] * op.__credit_incash
            x2 = ((cls.sales['2x']/2) * op.__credit_1x) + ((cls.sales['2x']/2)* op.__credit_nx)
            x3 = ((cls.sales['3x']/3) * op.__credit_1x) + (2*((cls.sales['3x']/3)* op.__credit_nx))
            purchase = op.__purchase/12
            ant1 = (cls.sales['1x'] - x1)*op.__antecipation_rate
            ant2 = (cls.sales['2x'] - x2)*op.__antecipation_rate*2
            ant3 = (cls.sales['3x'] - x3)*op.__antecipation_rate*3
            ant = ant1 + ant2 + ant3
            
            print(op.__company)
            debi = f'debit: R$ {deb:.2f}\n'
            cred1x = f'credit in cash: R$ {x1:.2f}\n'
            cred2x = f'credit 2x: R$ {x2:.2f}\n'
            cred3x = f'credit 3x: R$ {x3:.2f}\n'
            alu = f'Rental: R${op.__rental:.2f}\n'
            com = f'Purchase value in one month: R${purchase:.2f}\n'
            ante = f'Antecipation: R$ {ant:.2f}\n'
            total = f'Total: R$ {deb+x1+x2+x3+purchase+op.__rental+ant:.2f}\n'
            
            print((debi + cred1x + cred2x + cred3x + ante + alu + com + total).replace('.',','))
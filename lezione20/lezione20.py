"""1. GESTIONALE PAGAMENTO
Si definisca una nuova classe Pagamento che contiene un attributo privato e di tipo float che memorizza l'importo del pagamento e si definiscano appropriati metodi get() e set(). 
L'importo non è un parametro da passare in input alla classe Pagamento ma deve essere inizializzato utilizzando il metodo set() dove opportuno. Si crei inoltre un metodo dettagliPagamento() 
che visualizza una frase che descrive l'importo del pagamento, ad esempio: "Importo del pagamento: €20.00". Quando viene stampato, l'importo è sempre con 2 cifre decimali.

Successivamente, si definisca una classe PagamentoContanti che sia derivata da Pagamento e definisca l'importo. Questa classe dovrebbe ridefinire il metodo dettagliPagamento() 
per indicare che il pagamento è in contanti. Si definisca inoltre il metodo inPezziDa() che stampa a schermo quante banconote da 500 euro, 200 euro, 100 euro, 50 euro, 20 euro, 10 euro, 
5 euro e/o in quante monete da 2 euro, 1 euro, 0,50 euro, 0,20 euro, 0,10 euro, 0,05 euro, 0,01 euro sono necessarie per pagare l'importo in contanti.

Si definisca una classe PagamentoCartaDiCredito derivata anch'essa da Pagamento e che definisce l'importo. Questa classe deve contenere gli attributi per il nome del titolare della carta, 
la data di scadenza, e il numero della carta di credito. Infine, si ridefinisca il metodo dettagliPagamento() per includere tutte le informazioni della carta di credito oltre all'importo 
del pagamento.

Per il test, si creino almeno due oggetti di tipo PagamentoContanti e due di tipo PagamentoCartaDiCredito con valori differenti e si invochi dettagliPagamento() per ognuno di essi.

Esempio di output:
Pagamento in contanti di: €150.00
150.00 euro da pagare in contanti con:
1 banconota da 100 euro
1 banconota da 50 euro

Pagamento in contanti di: €95.25
95.25 euro da pagare in contanti con:
1 banconota da 50 euro
2 banconote da 20 euro
1 banconota da 5 euro
1 moneta da 0.2 euro
1 moneta da 0.05 euro

Pagamento di: €200.00 effettuato con la carta di credito
Nome sulla carta: Mario Rossi
Data di scadenza: 12/24
Numero della carta: 1234567890123456

Pagamento di: €500.00 effettuato con la carta di credito
Nome sulla carta: Luigi Bianchi
Data di scadenza: 01/25
Numero della carta: 6543210987654321"""

class Pagamento:

    def __init__(self) -> None:
        self.__importo: float = 0


    def get_importo(self):
        return self.__importo

    def set_importo(self, importo: float):
        self.__importo = importo

    def dettagliPagamento(self):
        return f"Importo del pagamento: ${round(self.get_importo(), 2)}"
    
class PagamentiContanti(Pagamento):

    def __init__(self) -> None:
        super().__init__()

    def dettagliPagamento(self):
        return f"Importo del pagamento, in contanti: ${round(self.get_importo(), 2)}; in pezzi da: {self.inPezziDa()}"
    
    def inPezziDa(self):
        importo: float = self.get_importo()
        banconote: dict[int, int] = {500: 0,
                                     200: 0,
                                     100: 0,
                                     50: 0,
                                     20: 0,
                                     10: 0,
                                     5: 0
                                     }
        monete: dict[float, int] = {2.00: 0,
                                    1.00: 0,
                                    0.50: 0,
                                    0.20: 0,
                                    0.10: 0,
                                    0.05: 0,
                                    0.01: 0
                                    } 
        while importo >= 5.00:
            for key, value in banconote.items():
                if key <= importo:
                    importo = round((importo - key), 2)
                    banconote[key] += 1
                    break
        while importo < 5.00 and importo > 0.00:
            for key, value in monete.items():
                if key <= importo:
                    importo = round((importo - key), 2)
                    monete[key] += 1
                    break
        usate: dict[float, int] = {}
        for key, value in banconote.items():
            if value != 0:
                usate.update({key: value})
        for key, value in monete.items():
            if value != 0:
                usate.update({key: value})
        return usate
    
class PagamentoCartaDiCredito(Pagamento):

    def __init__(self, nome: str, data_scadenza: str, numero: int) -> None:
        super().__init__()
        self.nome = nome
        self.data_scadenza = data_scadenza
        self.numero = numero

    def dettagliPagamento(self):
        return f"Dati della Carta di credito: {self.nome}, {self.data_scadenza}, {self.numero}; importo del pagamento: ${round(self.get_importo(), 2)}"
    

contanti1: PagamentiContanti = PagamentiContanti()
contanti2: PagamentiContanti = PagamentiContanti()
carta1: PagamentoCartaDiCredito = PagamentoCartaDiCredito("Giovanni", "31/12/2026", 12340)
carta2: PagamentoCartaDiCredito = PagamentoCartaDiCredito("Gigi", "31/08/2028", 98210)
contanti1.set_importo(324.99)
contanti2.set_importo(700.65)
carta1.set_importo(324.99)
carta2.set_importo(700.65)
print(contanti1.dettagliPagamento())
print(contanti2.dettagliPagamento())
print(carta1.dettagliPagamento())
print(carta2.dettagliPagamento())
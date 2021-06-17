from models.cliente import Cliente
from models.conta import Conta

jeferson: Cliente = Cliente('Jeferson Geovani', 'jeffolivera01@gmail.com', '123.456.789-01', '15/08/1993')
michelen: Cliente = Cliente('Michelen Voigt', 'chelyvoigtoliveira@gmail.com', '123.456.789-02', '09/01/1994')

#print(jeferson)
#print(michelen)

contaf: Conta = Conta(jeferson)
contaa: Conta = Conta(michelen)

#print(contaf)
#print(contaa)
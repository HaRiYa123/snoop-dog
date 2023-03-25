print('Hello Good Morning Shoppers')
A = input('If you want to browse our hundred of bakery products Press (Yes) (Any other Inputs are autumatically declined by the system) : ')
if A != 'Yes':
    print('Thank You , Have A Nice Day')
    exit()
if A == 'Yes':
  print('Hello..!!! Welcome to our Bakery')
  print('which products are do want to buy')
B = input('Bakery items or Beverages : ')
C = 'Bakery items'
D = 'Beverages'
if B == C :
    print('This is Our All Bakery Items')
    print('Kibula Bunnis')
    print('Jam Bunnis')
    print('Cream Bunnis')
    print('Fish Bun')
    print('Egg Bun')
    print('Sausage Bun')
    print('Tea Bun')
    print('Rolls')
if B == D :
    print('This is Our All Beverages')
    print('Orange Juice')
    print('Milo')
    print('Tea')
    print('Coffee')
print('If you want to any of these products type the name of it correctly, (One product at one time)')

E = 'Kibula Bunnis'
F = 'Jam Bunnis'
G = 'Cream Bunnis'
H = 'Fish Bun'
I = 'Egg Bun'
J = 'Sausage Bun'
K = 'Tea Bun'
L = 'Rolls'
N = 'Orange Juice'
O = 'Milo'
P = 'Tea'
Q = 'Coffee'

AA = '30'
BB = '35'
CC = '40'
DD = '45'
EE = '50'
FF = '55'
GG = '60'
HH = '80'
II = '100'
JJ = '120'

M = input('Select the Product Name : ')
if M == E :
     print('Your Cost Is Rs.' + CC)
if M == F :
     print('Your Cost Is Rs.' + str(AA))
if M == G :
     print('Your Cost Is Rs.' + str(CC))
if M == H :
     print('Your Cost Is Rs.' + str(EE))
if M == I :
     print('Your Cost Is Rs.' + str(BB))
if M == J :
    print('Your Cost Is Rs.' + str(DD))
if M == K :
    print('Your Cost Is Rs.' + str(AA))
if M == L :
    print('Your Cost Is Rs.' + str(II))

if M == N :
    print('Your Cost Is Rs.' + str(JJ))
if M == O :
    print('Your Cost Is Rs.' + str(HH))
if M == P :
    print('Your Cost Is Rs.' + str(FF))
if M == Q :
    print('Your Cost Is Rs.' + str(GG))

if M == E :
     T1 = int(CC)
if M == F :
     T1 = int(AA)
if M == G :
     T1 = int(CC)
if M == H :
     T1 = int(EE)
if M == I :
     T1 = int(BB)
if M == J :
    T1 = int(DD)
if M == K :
    T1 = int(AA)
if M == L :
    T1 = int(II)
if M == N :
    T1 = int(JJ)
if M == O :
    T1 = int(HH)
if M == P :
    T1 = int(FF)
if M == Q :
    T1 = int(GG)

R = input('Would you add another products, (Yes or No) : ')
X = 'Yes'
Y = 'No'
if R == X:
    S = input('Select The Product Name : ')
if R == Y :
    print('Order Completed Here is Your Bill Pay for the Cashier Thank You..!')
    print('your Bill is Rs. ' + str(T1))
    exit()

if S == E :
     T2 = int(CC)
if S == F :
     T2 = int(AA)
if S == G :
     T2 = int(CC)
if S == H :
     T2 = int(EE)
if S == I :
     T2 = int(BB)
if S == J :
    T2 = int(DD)
if S == K :
    T2 = int(AA)
if S == L :
    T2 = int(II)
if S == N :
    T2 = int(JJ)
if S == O :
    T2 = int(HH)
if S == P :
    T2 = int(FF)
if S == Q :
    T2 = int(GG)

if S == E :
     print('Your Cost Is Rs.' + str(CC))
if S == F :
     print('Your Cost Is Rs.' + str(AA))
if S == G :
     print('Your Cost Is Rs.' + str(CC))
if S == H :
     print('Your Cost Is Rs.' + str(EE))
if S == I :
     print('Your Cost Is Rs.' + str(BB))
if S == J :
    print('Your Cost Is Rs.' + str(DD))
if S == K :
    print('Your Cost Is Rs.' + str(AA))
if S == L :
    print('Your Cost Is Rs.' + str(II))

if S == N :
    print('Your Cost Is Rs.' + str(JJ))
if S == O :
    print('Your Cost Is Rs.' + str(HH))
if S == P :
    print('Your Cost Is Rs.' + str(FF))
if S == Q :
    print('Your Cost Is Rs.' + str(GG))

print('You have reached the maximum number of orders')
print('Your total is Rs.' + str(T1 + T2) )
print('Pay at the Counter.Thank You')
exit()









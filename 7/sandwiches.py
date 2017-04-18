sandwich_orders = ['tuna', 'pastrami', 'chicken', 'bekon', 'pastrami', 'cheese', 'pastrami']
finished_sandwiches = []

print('Pastrami sandwich is out!')
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

while sandwich_orders:
    sandwich_order = sandwich_orders.pop()
    print("I made your " + sandwich_order + ' sandwich')
    finished_sandwiches.append(sandwich_order)

for finished_sandwiche in finished_sandwiches:
    print(finished_sandwiche.title() + " sandwich")

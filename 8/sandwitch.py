def order_sandwitch(*items):
    print("\nMake a sandwitch with this items: ")
    for item in items:
        print("- " + item)


order_sandwitch('bekon')
order_sandwitch('cheese', 'ketchup', 'cucumber')
order_sandwitch('beaf', 'cheese')

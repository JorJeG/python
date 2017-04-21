def print_models(unprinting_designs, completed_models):
    while unprinting_designs:
        current_design = unprinting_designs.pop()
        print("Printing model: " + current_design)
        completed_models.append(current_design)


def show_completed_models(completed_models):
    print("\nThe following models have been printed:")
    for completed_model in completed_models:
        print(completed_model)

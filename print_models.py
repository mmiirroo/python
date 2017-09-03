def print_models(unprinted_models, completed_models):
    while unprinted_models:
        current_design = unprinted_models.pop()
        print("Printing model:" + current_design)
        completed_models.append(current_design)

def show_completed_models(completed_models):
    print("\nThe following models have been printed:")
    for completed_model in completed_models:
        print(completed_model)

unprinted_models = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []

print_models(unprinted_models, completed_models)
show_completed_models(completed_models)

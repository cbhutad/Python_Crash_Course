def design_models(undesigned_models, completed_models):
    
    while len(undesigned_models) != 0:
        model = undesigned_models.pop()
        print(f"Designing model : {model}")
        completed_models.append(model)

def print_models(completed_models):
    print("\nCompleted Models are : ")
    for model in completed_models:
        print(model.title())
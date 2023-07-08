# using functions to complete the design the print them

# def design_models(undesigned_models, completed_models):
    
#     while len(undesigned_models) != 0:
#         model = undesigned_models.pop()
#         print(f"Designing model : {model}")
#         completed_models.append(model)

# def print_models(completed_models):
#     print("\nCompleted Models are : ")
#     for model in completed_models:
#         print(model.title())

# undesigned_models = ["model1", "model2", "model3"]
# completed_models = []

# design_models(undesigned_models,completed_models)
# print_models(completed_models)

# Same working as above but preserving the original list of undesigned models by providing copy instead of the original list object

def design_models(undesigned_models, completed_models):
    
    while len(undesigned_models) != 0:
        model = undesigned_models.pop()
        print(f"Designing model : {model}")
        completed_models.append(model)

def print_models(completed_models):
    print("\nCompleted Models are : ")
    for model in completed_models:
        print(model.title())

undesigned_models = ["model1", "model2", "model3"]
completed_models = []

design_models(undesigned_models[:],completed_models)
print_models(completed_models)
print(undesigned_models)
def all_thing_is_obj(object : any) -> type :
    # besoin d utiliser mla fonction type native 
    type_obj = type(object)


    if type_obj == float:
        print(f"nan : {type_obj}")
    elif type_obj == str:
        print(f"Empty: {type_obj}")
    elif type_obj == int:
        print(f"Zero : {type_obj}")
    elif type_obj == bool:
        print(f"Fake : {type_obj}")
    else:
        print(f"Type not found : {type_obj}")

    return type_obj

def NULL_not_found(object: any) -> int:
    t = type(object)
    
    # On vérifie si c'est un des cas "NULL" acceptés
    if object is None:
        print(f"Nothing: {object} {t}")
    elif isinstance(object, float) and object != object: # C'est le test pour NaN
        print(f"Cheese: nan {t}")
    elif t is int and object == 0:
        print(f"Zero: 0 {t}")
    elif t is str and object == "":
        print(f"Empty: {t}")
    elif t is bool and object is False:
        print(f"Fake: {object} {t}")
    else:
        # Si on arrive ici, ce n'est pas un "NULL" au sens de l'exo
        print("Type not Found")
        return 1
        
    return 0
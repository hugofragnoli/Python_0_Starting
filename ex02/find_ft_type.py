def all_thing_is_obj(object : any) -> int :
    # besoin d utiliser mla fonction type native 
    type_obj = type(object)

    if type_obj == list:
        print(f"List : {type_obj}")
    elif type_obj == tuple:
        print(f"Tuple : {type_obj}")
    elif type_obj == set:
        print(f"Set : {type_obj}")
    elif type_obj == dict:
        print(f"Dict : {type_obj}")
    elif type_obj == str:
        print(f"{object} is in the kitchen : {type_obj}")
    else:
        print("Type not found")

    return 42
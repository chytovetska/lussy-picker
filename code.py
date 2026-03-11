def touch(where : str, name = "Yehor"):
    print(f"{name}'s {where} was touched")

person, bodypart = map(str, input().split())
touch(bodypart, person)
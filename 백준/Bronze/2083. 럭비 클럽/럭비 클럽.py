while True:
    name, age, weight = map(str, input().split())
    if name == '#' and age == '0' and weight == '0': break
    else:
        if int(age) > 17 or int(weight) >= 80:
            print(f"{name} Senior")
        else:
            print(f"{name} Junior")

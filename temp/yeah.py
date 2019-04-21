with open("/home/simrat39/py/temp/lol.txt", "r") as file:
    for line in file:
        if 'shishu' in line:
            print("Kang found: ",line)
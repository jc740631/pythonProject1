COLOR_NAME_TO_COLOR_CODE = {
    "aliceblue": "#f0f8ff",
    "aqua": "#00ffff",
    "beaver": "#9f8170",
    "bittersweet": "#fe6f5e",
    "bleu de france": "#318ce7",
    "blond": "#faf0be",
    "bright lilac": "#d891ef",
    "byzantium": "#702963",
    "cadmium yellow": "#fff600",
    "celeste": "#b2ffff"
}

color_name = input("Enter color name(hit enter to quit): ").lower()
while color_name != "":
    if color_name in COLOR_NAME_TO_COLOR_CODE:  # find key
        print(f"{color_name} is {COLOR_NAME_TO_COLOR_CODE[color_name]}")
    else:
        print("Invalid color name")
    color_name = input("Enter color name(hit enter to quit):  ").lower()
    print("Bye.")

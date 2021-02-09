#x = str(input("enter: "))

month_conversion = {
    "jan": "january",
    "mar": "march",
    "dec": "december",
    "liam": "is a dingus",
}

print(month_conversion.get("dfa", "not something i entered"))


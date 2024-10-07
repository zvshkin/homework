cities = {
    "Москва": {
        "strana": "Россия",
        "ludey": 13200000,
        "fact": "Площадь = 2561 км(кв)."},
    "Абуджа": {
        "strana": "Нигер",
        "ludey": 1700000,
        "fact": "Площадь = 609 км(кв)."},
    "Дубай": {
        "strana": "ОАЭ",
        "ludey": 3600000,
        "fact": "Площадь = 3800 км(кв)."}}

for z, v in cities.items():
    print("Город:", z)
    print("Страна:", v['strana'])
    print("Население", v['ludey'])
    print("Факт:", v['fact'])
    print()
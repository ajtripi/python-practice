# firstname = "alec"
# lastname = "tripi"
# fullname = f"{firstname} {lastname}"
# print(fullname.title())

# motorcycles = ['honda', 'yamaha', 'suzuki']
# print(reversed(motorcycles))

# # practice 4
# menu_itms = ['pizza', 'pasta', 'chicken parm', 'salad']
# print(f"the first three items are: {menu_itms[:3]}")
# print("my favorite items are:")
# for item in menu_itms[-3:]:
#     print(item, end=" ")  # This prints items on the same line with spaces
# print()  # Add a newline at the end

# # Alternative: Join items with spaces and print once
# print("my favorite items are:", " ".join(menu_itms[-3:]))

cities = {
    'new york':{
        'state': 'ny',
        'population': '8.5 million',
        'nickname': 'the big apple'
        },
    'chicago':{
        'state': 'il',
        'population': '6.5 million',
        'nickname': 'the windy city'
        },
    'boston':{
        'state': 'ma',
        'population': '7.5 million',
        'nickname': 'the hub'
        },
    'austin':{
        'state': 'tx',
        'population': '5 million',
        'nickname': 'the live music capital of the world'
        },
    'philadelphia':{
        'state': 'pa',
        'population': '3.5 million',
        'nickname': 'the city of brotherly love'
        },
    }

for city, info in cities.items():
    state = info['state']
    population = info['population']
    nickname = info['nickname']
    
    print(f"{city.title()} is in {state.upper()}.")
    print(f"It has a population of {population}.")
    print(f"It's nickname is '{nickname.title()}'.\n")
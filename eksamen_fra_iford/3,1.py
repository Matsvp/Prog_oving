def meny():
    return{'Ribbe' : 145.90,
           'Pinnekjøtt' : 155.90,
           'Lutefisk' : 135.90,
           'Nøttestek' : 135.90,
           'Reinsdyrstek' : 155.90
     }

def display_meny_item(item_name):
    menu = meny()
    if item_name in menu:
        print(f'{item_name} - {menu[item_name]}')
    else:
        print(f'{item_name} finnes ikke i menyen')



display_meny_item('Ribbe')
display_meny_item('Pizza')


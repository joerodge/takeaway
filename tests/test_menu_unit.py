from lib.menu import Menu

def test_menu_is_created_properly():
    menu = Menu()
    assert len(menu.dishes) == 7
    assert menu.dishes[3].name == 'Mushroom Risotto' 

def test_list_all_dishes():
    menu = Menu()
    result = menu.list_dishes()
    assert result.startswith('Fish and Chips: £11.50\nSausage')
    assert result.endswith('£7.50\nHam and Cheese Baguette: £5.00')
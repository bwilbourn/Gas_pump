def inventory_to_string(inventory):
    '''Dict[String, Item] -> String

    Returns a string representation of the provided inventory.
    The string format of the inventory is the same as the one provided to `read_inventory`
    The items should be written out in alphabetical order according to their names.

    >>> inventory_to_string({
    ...   'Coke': {'name': 'Coke', 'paid': .4, 'charging': 1.0},
    ...   'Tab': {'name': 'Tab', 'paid': 0.54, 'charging': 1.49}})
    'Coke\\t0.4\\t1.0\\nTab\\t0.54\\t1.49'
    >>> inventory_to_string({
    ...   'Chips': {'name': 'Chips', 'paid': 0.5, 'charging': 1.25},
    ...   'Pizza': {'name': 'Pizza', 'paid': 3.0, 'charging': 5.0},
    ...   'Coke': {'name': 'Coke', 'paid': 0.4, 'charging': 1.0}})
    'Chips\\t0.5\\t1.25\\nCoke\\t0.4\\t1.0\\nPizza\\t3.0\\t5.0'
    '''
    new_l = []
    for item in inventory.values():
        new_l.append('{0}\t{1}\t{2}'.format(item['name'], item['paid'], item['charging']))
        sort = sorted(new_l)
    return '\n'.join(sort)
def select_dates(potential_dates):
    names = [i.get('name') for i in potential_dates if i.get('age') > 30 and i.get('city') == 'Berlin'
             and 'art' in i.get('hobbies')]
    return ", ".join(names)

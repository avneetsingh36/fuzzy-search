def ending(num):
    endings = {1: 'st', 2: 'nd', 3: 'rd'}
    if num % 100 in [11, 12, 13]:
        return 'th'
    else:
        return endings.get(num % 10, 'th')


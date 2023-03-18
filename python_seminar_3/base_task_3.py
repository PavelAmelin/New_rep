def person(**kwargs):
    for k, val in kwargs.items():
        print(f'{k}: {val}', end=', ')

person(name='Ivan', last_name='Ivanov', birth_d='1846', city='Moscow', email='jackie@gmail.com', tel='01005321456')
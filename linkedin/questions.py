# Q172
employees = {
    'alice': {
        'position': 'Lead Developer',
        'salary': 1000
    },
    'bob': {
        'position': 'Lead Artist',
        'salary': 2000
    },
    'charlie': {
        'position': 'cfo',
        'salary': 3000
    }
}

employees['alice']['salary'] = employees['charlie']['salary']

print(employees['alice'])

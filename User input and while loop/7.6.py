unconfirmed_cases = ['virat','dhawan','rohit']
confirmed_cases = []

while unconfirmed_cases:
    current_cases = unconfirmed_cases.pop()
    print('Verifying user: '+ current_cases.title())

    confirmed_cases.append(current_cases)

for confirmed_case in confirmed_cases:
    print(confirmed_case.title())
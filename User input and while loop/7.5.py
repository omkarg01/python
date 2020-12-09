ticket = '\nEnter your age here to know the price of ticket: '
ticket+="\nEnter 'quit' when uour finished."

while True:
    know = int(input(ticket))
    if know < 3:
        print(" No tickets needed, it's free for you.")
    elif 12 >= know >= 3:
        print('Your ticket cost is 10$')
    elif know > 12:
        print('Your ticket price is 15$ ')
    else:
        break

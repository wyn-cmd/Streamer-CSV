# Version 1.0




def find_cheapest_streamer(streamer_prices_list, customers):
    # Initialize a dictionary to store streamer prices
    streamer_prices_dict = {}

    # Fill the dictionary with streamer prices
    for row in streamer_prices_list:
        streamer = row[0]
        prices = list(map(float, row[1:]))  # Convert the price strings to floats
        streamer_prices_dict[streamer] = prices

    # Initialize the nested list for storing customer subscriptions
    subscriptions = []

    # Genre mapping
    genres = ['Sports', 'Sitcom', 'Drama', 'Reality', 'Film']

    # Process each customer
    for customer in customers:
        name = customer[0]
        genre1 = customer[1]
        genre2 = customer[2]

        # Get genre indices
        index1 = genres.index(genre1)
        index2 = genres.index(genre2)

        # Initialize variables to find the cheapest streamer
        min_cost = float('inf')
        best_streamer = ''

        # Check each streamer to find the cheapest one
        for streamer, prices in streamer_prices_dict.items():
            cost = prices[index1] + prices[index2]
            if cost < min_cost:
                min_cost = cost
                best_streamer = streamer

        # Append the result for the current customer
        subscriptions.append([name, best_streamer, min_cost])

    # Print the subscriptions list with a heading
    print("\nCustomer Subscriptions:")
    for subscription in subscriptions:
        print(subscription)

    return subscriptions

# Read data from the file
file_name = 'streamers.txt'
streamer_prices_list = []

# Open the file and read the data
with open(file_name, 'r') as file:
    # Read the header line and ignore it
    header = file.readline().strip().split(',')

    # Read the remaining lines for the streamer data
    for line in file:
        data = line.strip().split(',')
        streamer_prices_list.append(data)

# Print the streamer prices list with a heading
print('\nStreamer Prices List:')
for row in streamer_prices_list:
    print(row)

# Define the customer list
customers = [
        ['Angelica', 'Sports', 'Reality'],
        ['Eliza', 'Sitcom', 'Drama'],
        ['Alex', 'Drama', 'Sports'],
        ['Peggy', 'Sitcom', 'Reality'],
        ['George', 'Sports', 'Film'],
        ['Andy', 'Reality', 'Sports']
    ]

# Find the cheapest streamer for each customer
subscriptions = find_cheapest_streamer(streamer_prices_list, customers)

# Display customers and their subscriptions
print('\nName            Genre 1         Genre 2         Streamer        Cost')
num = 0
total = 0
metflicks = 0
duriantv = 0
risney = 0
composite = 0
provider_list = []
for person in subscriptions:
    print(f'{person[0]: <15} {customers[num][1]: <15} {customers[num][2]: <15} {person[1]: <15} {person[2]: <15.2f} ')
    if person[1] == 'Metflicks':
        metflicks += 1
        provider_list.append(['Metflicks', person[2]])
    elif person[1] == 'DurianTV+':
        duriantv += 1
        provider_list.append(['DurianTV+', person[2]])
    elif person[1] == 'Risney+':
        risney += 1
        provider_list.append(['Risney+', person[2]])
    elif person[1] == 'CompositeVideo':
        composite += 1
        provider_list.append(['CompositeVideo', person[2]])

# calculate average spent
total += person[2]
num += 1
average = total / num
print(f'\nAverage spent: ${average:.2f}')


if metflicks > duriantv:
    if metflicks > risney:
        if metflicks > composite:
            print('Most subscribed streamer: Metflicks')
            print(f'Number of subscribers: {metflicks}')
        else:
            print('Most subscribed streamer: Composite')
            print(f'Number of subscribers: {composite}')
    else:
        if risney > composite:
            print('Most subscribed streamer: Risney+')
            print(f'Number of subscribers: {risney}')
        else:
            print('Most subscribed streamer: CompositeVideo')
            print(f'Number of subscribers: {composite}')

else:
    if duriantv > risney:
        if duriantv > composite:
            print('Most subscribed streamer: DurianTV+')
            print(f'Number of subscribers: {duriantv}')
        else:
            print('Most subscribed streamer: CompositeVideo')
            print(f'Number of subscribers: {composite}')
    else:
        if risney > composite:
            print('Most subscribed streamer: Risney+')
            print(f'Number of subscribers: {risney}')
        else:
            print('Most subscribed streamer: CompositeVideo')
            print(f'Number of subscribers: {composite}')

# Version 1.2

from collections import Counter


def find_cheapest_streamer(streamer_prices_list, customers):
    streamer_prices_dict = {}
    for row in streamer_prices_list:
        streamer = row[0]
        prices = list(map(float, row[1:]))
        streamer_prices_dict[streamer] = prices

    subscriptions = []
    genres = ["Sports", "Sitcom", "Drama", "Reality", "Film"]

    for customer in customers:
        name, genre1, genre2 = customer[0], customer[1], customer[2]
        index1 = genres.index(genre1)
        index2 = genres.index(genre2)

        min_cost = float("inf")
        best_streamer = ""

        for streamer, prices in streamer_prices_dict.items():
            cost = prices[index1] + prices[index2]
            if cost < min_cost:
                min_cost = cost
                best_streamer = streamer

        subscriptions.append([name, best_streamer, min_cost])

    print("\nCustomer Subscriptions:")
    for subscription in subscriptions:
        print(subscription)

    return subscriptions


file_name = "streamers.txt"
streamer_prices_list = []

try:
    with open(file_name, "r") as file:
        header = file.readline().strip().split(",")
        for line in file:
            if line.strip():
                data = line.strip().split(",")
                streamer_prices_list.append(data)
except FileNotFoundError:
    print(f"Error: The file '{file_name}' was not found.")
    streamer_prices_list = []

print("\nStreamer Prices List:")
for row in streamer_prices_list:
    print(row)

customers = [
    ["Angelica", "Sports", "Reality"],
    ["Eliza", "Sitcom", "Drama"],
    ["Alex", "Drama", "Sports"],
    ["Peggy", "Sitcom", "Reality"],
    ["George", "Sports", "Film"],
    ["Andy", "Reality", "Sports"],
]

subscriptions = find_cheapest_streamer(streamer_prices_list, customers)

print("\nName            Genre 1         Genre 2         Streamer        Cost")
total = 0
# count by whatever streamer name the CSV holds, so the names in the file
# do not have to be listed a second time here as well
provider_counts = Counter()

for idx, person in enumerate(subscriptions):
    name, streamer, cost = person[0], person[1], person[2]
    cust_genre1 = customers[idx][1]
    cust_genre2 = customers[idx][2]

    print(f"{name: <15} {cust_genre1: <15} {cust_genre2: <15} {streamer: <15} {cost: <15.2f}")

    provider_counts[streamer] += 1
    total += cost

num_customers = len(subscriptions)
average = total / num_customers if num_customers > 0 else 0
print(f"\nAverage spent: ${average:.2f}")

if provider_counts:
    most_popular_streamer, subscribers = provider_counts.most_common(1)[0]
    print(f"Most subscribed streamer: {most_popular_streamer}")
    print(f"Number of subscribers: {subscribers}")
# Version 1.3
import sys
from collections import Counter

# Reads streamer prices from a CSV file and returns the genres and price mapping
def load_streamer_data(file_name):
    try:
        with open(file_name, "r") as file:
            lines = [line.strip() for line in file if line.strip()]
            if not lines:
                return [], {}

            # Use the header to determine the available genres
            header = lines[0].split(",")
            genres = header[1:]
            
            streamer_prices = {}
            for line in lines[1:]:
                parts = line.split(",")
                name = parts[0]
                prices = [float(p) for p in parts[1:]]
                streamer_prices[name] = prices
            
            return genres, streamer_prices
    except FileNotFoundError:
        print(f"Error: The file '{file_name}' was not found.")
        sys.exit(1)
    except (ValueError, IndexError) as e:
        print(f"Error parsing CSV data: {e}")
        sys.exit(1)

# Calculates the cheapest streamer for each customer based on their preferred genres
def get_best_subscriptions(streamer_prices, customers, genres):
    subscriptions = []

    for customer in customers:
        name, g1, g2 = customer
        
        # Find indices for the requested genres
        try:
            idx1 = genres.index(g1)
            idx2 = genres.index(g2)
        except ValueError as e:
            print(f"Error: Genre not found for customer {name}: {e}")
            continue

        min_cost = float("inf")
        best_streamer = None

        for streamer, prices in streamer_prices.items():
            cost = prices[idx1] + prices[idx2]
            if cost < min_cost:
                min_cost = cost
                best_streamer = streamer

        subscriptions.append({
            "name": name,
            "streamer": best_streamer,
            "cost": min_cost,
            "genres": (g1, g2)
        })

    return subscriptions

def main():
    file_name = "streamers.txt"
    customers = [
        ["Angelica", "Sports", "Reality"],
        ["Eliza", "Sitcom", "Drama"],
        ["Alex", "Drama", "Sports"],
        ["Peggy", "Sitcom", "Reality"],
        ["George", "Sports", "Film"],
        ["Andy", "Reality", "Sports"],
    ]

    genres, streamer_prices = load_streamer_data(file_name)

    print("\nStreamer Prices List:")
    for streamer, prices in streamer_prices.items():
        print(f"{streamer}: {prices}")

    subscriptions = get_best_subscriptions(streamer_prices, customers, genres)

    print("\nName            Genre 1         Genre 2         Streamer        Cost")
    total_spent = 0
    provider_counts = Counter()

    for sub in subscriptions:
        g1, g2 = sub["genres"]
        print(f"{sub['name']: <15} {g1: <15} {g2: <15} {sub['streamer']: <15} {sub['cost']: <15.2f}")
        
        provider_counts[sub['streamer']] += 1
        total_spent += sub['cost']

    if not subscriptions:
        print("No subscriptions were processed.")
        return

    avg_cost = total_spent / len(subscriptions)
    print(f"\nAverage spent: ${avg_cost:.2f}")

    if provider_counts:
        most_popular, count = provider_counts.most_common(1)[0]
        print(f"Most subscribed streamer: {most_popular}")
        print(f"Number of subscribers: {count}")

if __name__ == "__main__":
    main()
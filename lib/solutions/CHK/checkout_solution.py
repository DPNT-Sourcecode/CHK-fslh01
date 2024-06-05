# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    prices = {
        'A': 50, 'B': 30, 'C': 20, 'D': 15, 'E': 40, 'F': 10,
        'G': 20, 'H': 10, 'I': 35, 'J': 60, 'K': 80, 'L': 90,
        'M': 15, 'N': 40, 'O': 10, 'P': 50, 'Q': 30, 'R': 50,
        'S': 30, 'T': 20, 'U': 40, 'V': 50, 'W': 20, 'X': 90,
        'Y': 10, 'Z': 50
    }

    special_offers = {
        'A': [(5, 200), (3, 130)],
        'B': [(2, 45)],
        'H': [(10, 80), (5, 45)],
        'K': [(2, 150)],
        'P': [(5, 200)],
        'Q': [(3, 80)],
        'V': [(3, 130), (2, 90)]
    }

    free_offers = {
        'E': (2, 'B'),
        'F': (3, 'F'),
        'N': (3, 'M'),
        'R': (3, 'Q'),
        'U': (4, 'U')
    }

    if not all(item in prices for item in skus):
        return -1

    from collections import Counter
    item_counts = Counter(skus)

    sum = 0

    for item, (required_count, free_item) in free_offers.items():
        if item in item_counts:
            free_items_count = (item_counts[item] // required_count)
            if free_item == item:
                item_counts[item] -= free_items_count
            else:
                item_counts[free_item] = max(0, item_counts[free_item] - free_items_count)

    for item, count in item_counts.items():
        if item in special_offers:
            for offer_count, offer_price in sorted(special_offers[item], reverse=True):
                sum += (count // offer_count) * offer_price
                count %= offer_count
        sum += count * prices[item]

    return sum

    # in item_counts.items():
    # if item == 'E' and item_counts[item] >= 2:
    #     free_b_items = item_counts[item] // 2
    #     item_counts['B'] = max(0, item_counts['B'] - free_b_items)
    #
    # if item in special_offers:
    #     if isinstance(special_offers[item], list):
    #         for offer_count, offer_price in sorted(special_offers[item], reverse=True):
    #             sum += (count // offer_count) * offer_price
    #             count %= offer_count
    #
    #     elif isinstance(special_offers[item], tuple):
    #         offer_count, free_item = special_offers[item]
    #         sum += (count // offer_count) * offer_count * prices[item]
    #         count %= offer_count
    #
    # sum += count * prices[item]

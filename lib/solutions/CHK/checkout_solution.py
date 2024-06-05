# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    prices = {
        'A': 50, 'B': 30, 'C': 20, 'D': 15, 'E': 40, 'F': 10,
        'G': 20, 'H': 10, 'I': 35, 'J': 60, 'K': 70, 'L': 90,
        'M': 15, 'N': 40, 'O': 10, 'P': 50, 'Q': 30, 'R': 50,
        'S': 20, 'T': 20, 'U': 40, 'V': 50, 'W': 20, 'X': 17,
        'Y': 20, 'Z': 21
    }

    special_offers = {
        'A': [(5, 200), (3, 130)],
        'B': [(2, 45)],
        'H': [(10, 80), (5, 45)],
        'K': [(2, 120)],
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

    group_discount_items = {'S', 'T', 'X', 'Y', 'Z'}
    group_discount_price = 45

    if not all(item in prices for item in skus):
        return -1

    from collections import Counter
    item_counts = Counter(skus)

    total = 0

    for item, (required_count, free_item) in free_offers.items():
        if item in item_counts:
            free_items_count = (item_counts[item] // required_count)
            if free_item == item:
                item_counts[item] -= free_items_count
            else:
                item_counts[free_item] = max(0, item_counts[free_item] - free_items_count)

    group_discount_count = sum(item_counts[item] for item in group_discount_items)
    if group_discount_count >= 3:
        total += (group_discount_count // 3)*group_discount_price
        rem_group_items = group_discount_count % 3
        group_items_sorted = sorted(group_discount_items, key=lambda x: prices[x], reverse=True)
        for item in group_items_sorted:
            if rem_group_items <= 0:
                break
            if item_counts[item] > 0:
                count_to_add = min(item_counts[item], rem_group_items)
                total += count_to_add * prices[item]
                rem_group_items -= count_to_add
                item_counts[item] -= count_to_add

    for item, count in item_counts.items():
        if item in special_offers:
            for offer_count, offer_price in sorted(special_offers[item], reverse=True):
                total += (count // offer_count) * offer_price
                count %= offer_count
        total += count * prices[item]

    return total




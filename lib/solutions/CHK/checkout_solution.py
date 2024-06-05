

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):

    prices = {'A': 50, 'B':30, 'C':20, 'D': 15, 'E': 40}
    special_offers = {
        'A': [(5, 200), (3, 130)],
        'B': [(2, 45)],
        'E': (2, 'B')
    }

    if not all(item in prices for item in skus):
        return -1

    from collections import Counter
    item_counts = Counter(skus)

    sum = 0

    for item, count in item_counts.items():
        if item == 'E' and item_counts[item] >= 2:
            free_B_items = item_counts[item] //2
            item_counts['B'] = max(0, item_counts['B'] - free_B_items)


        if item in special_offers:
            if isinstance(special_offers[item], list):
                for offer_count, offer_price in sorted(special_offers[item,reversed]):
                    sum += (count//offer_count)*offer_price
                    count %=offer_count

            elif isinstance(special_offers[item], tuple):
                offer_count, free_item = special_offers[item]
                sum += (count // offer_count)*offer_count*prices[item]
                count %= offer_count

        sum += count * prices[item]

    return sum


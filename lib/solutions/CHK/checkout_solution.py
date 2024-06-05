

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):

    prices = {'A': 50, 'B':30, 'C':20, 'D': 15}
    special_offers = {'A': (3, 130), 'B': (2, 45)}

    if not all(item in prices for item in skus):
        return -1

    from collections import Counter
    item_counts = Counter(skus)

    sum = 0

    for item, count in item_counts.items():
        if item in special_offers:
            offer_count, offer_price = special_offers[item]
            sum += (count // offer_count)*offer_price
            count %= offer_count

        sum += count * prices[item]

    return sum


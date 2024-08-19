# quick demo of lambda vs functions
pairs = [(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four')]
sorted_pairs = sorted(pairs, key=lambda x: x[1])

def get_second_item(pair):
    return pair[1]

sorted_pairs = sorted(pairs, key=get_second_item)
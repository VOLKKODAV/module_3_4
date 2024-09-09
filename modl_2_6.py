
def single_root_words(root_word, *other_words):
    same_words = []
    for item in other_words:
        if root_word.lower() in item.lower() or item.lower() in root_word.lower():
            same_words.append(item)
    return same_words


result1 = single_root_words('rich',  'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement',  'Able', 'Mable', 'Disable', 'Bagel')
print('\n'.join(result1))
print()                   #'\n'.join -- переход на другую строку    # join -- соединяющий метод
print('\n'.join(result2))

#     for item in other_words:
#         if root_word.lower() in item.lower():
#             same_words.append(item)
#         item.lower() in root_word.lower():
#             same_words.append(item)
#     return same_words
def count_words(text):
    words = text.split()
    return len(words)

def count_chars(text):
    
    char_count = {}

    for char in text:

        char = char.lower()

        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count





def sort_chars(char_count):
    char_list =[]
    for char, count in char_count.items():
        char_dic = {"char": char, "num": count}
        char_list.append(char_dic)

    def sort_on(item):
        return item["num"]

    char_list.sort(reverse=True, key=sort_on)

    return char_list
def num_of_words(text):
    words = text.split() 
   
    return len(words)

def char_count(text):
    res = {}
    l_text = text.lower()
    words = l_text.split()
    for word in words:
        for char in word:
            if char in res:
                res[char] += 1
            else: 
                res[char] = 1
    
    return res

def sort_on(item):
    return item["num"]

def sort_characters(char_dict):
    char_list = []
    for ch in char_dict:
        char_list.append({"char": ch, "num": char_dict[ch]})
    char_list.sort(reverse=True, key=sort_on)
    return char_list


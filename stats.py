def get_words_count(text):
    if text is None or text == '':
        return 0

    return len(text.split())

def get_character_dict(text):
    if text is None or text == '':
        return 0

    characters_dict = {}
    for word in text.split():
        for character in word:
            char = character.lower()
            if char.isalpha():
                if char in characters_dict:
                    characters_dict[char] += 1
                else:
                    characters_dict[char] = 1

    return characters_dict

def sort_on_dict(dictionary):
    sorted_dict_list = []
    _dict = {}
    for key, value in dictionary.items():
        _dict["char"] = key
        _dict["num"] = value
        sorted_dict_list.append(_dict)
        _dict = {}

    sorted_dict_list.sort(reverse=True, key=sort_on)
    return sorted_dict_list

def sort_on(items):
    return items["num"]
def get_count(text): 
   return len(text.split())


def get_character_count(book): 
    count_dictionary = {} 
    for char in book:
        if char.lower() in count_dictionary: 
            count_dictionary[char.lower()] += 1 
        else:
            count_dictionary[char.lower()] = 1 
    return count_dictionary



def sort_dictionary(dictionary): 
    new_list = []
    for key,value in dictionary.items(): 
        if key.isalpha(): 
            new_list.append({key:value}) 

    new_list.sort(key=sortItem, reverse=True)
    return new_list

def sortItem(item):
    for key in item:
        return item[key]

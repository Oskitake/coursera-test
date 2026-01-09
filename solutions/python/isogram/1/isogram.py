def is_isogram(string):

    sentence_list = []

    for char in string:        
        if char.lower() in sentence_list and char.isalpha():
            return False
        sentence_list.append(char.lower())

    return True

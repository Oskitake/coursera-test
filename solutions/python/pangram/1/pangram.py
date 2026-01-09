def is_pangram(sentence):

    sentence_list = []
    
    for char in sentence.strip():
        if char.lower() not in sentence_list and char.isalpha():
            sentence_list.append(char)
    
    if len(sentence_list) == 26: 
        return True
    return False
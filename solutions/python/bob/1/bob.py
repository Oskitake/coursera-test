def response(hey_bob):

    if hey_bob[:-1] == hey_bob[:-1].upper() and any(c.isalpha() for c in hey_bob):
        if hey_bob[-1] == "?":
            return "Calm down, I know what I'm doing!"
        return "Whoa, chill out!"
    elif len(hey_bob) > 0 and len(hey_bob.strip()) > 0 and hey_bob.strip()[-1] == "?": 
        return "Sure."
    elif len(hey_bob.strip()) == 0:
        return "Fine. Be that way!"
    return "Whatever."
            
        
        

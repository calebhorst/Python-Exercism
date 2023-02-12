def response(hey_bob=""):
    hey_bob = hey_bob.strip()
    #He says 'Fine. Be that way!' if you address him without actually saying anything.
    if hey_bob.strip() == "":
        return "Fine. Be that way!"
    elif hey_bob[-1] == "?":
        #He answers 'Calm down, I know what I'm doing!' if you yell a question at him.
        if hey_bob.isupper():
            return "Calm down, I know what I'm doing!"
        #Bob answers 'Sure.' if you ask him a question, such as "How are you?".
        else:
            return "Sure."
    #He answers 'Whoa, chill out!' if you YELL AT HIM (in all capitals).
    elif hey_bob.isupper():
        return "Whoa, chill out!"
    #He answers 'Whatever.' to anything else.
    else:
        return "Whatever."

** start of main.py **

def is_valid_message(message, validation):
    if len(message.split()) != len(validation):
        return False
    for idx, word in enumerate(message.split()):
        print(idx,word.lower(),validation.lower()[idx])
        if word.lower().startswith(validation.lower()[idx]):
            pass
        else:
            return False
    return True


** end of main.py **


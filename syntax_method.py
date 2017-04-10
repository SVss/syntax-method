def analyze(items_list, grammar):
    done = False
    error = False
    for rule in grammar:
        applied = False
        i = 0
        while not applied and i < len(items_list)-1:
            applied = rule.apply(items_list[i:i+2])
            if applied:
                items_list[i] = applied
                del items_list[i+1]
            i += 1
        error = not applied
    return not error

def synthesize():
    pass

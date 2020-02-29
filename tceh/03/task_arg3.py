def glue(*words, glue=':'):
    glued = []
    for item in words:
        if len(item) == 3:
            glued.append(item)
    
    return glue.join(glued)

print(glue('max', 'bobby', 'tom', 'foobar'))
def pal_checker(num):
    count = 0
    text = str(num)
    rev_text = text[::-1]

    while text != rev_text:
        new_num = int(text) + int(rev_text)
        count += 1
        text = str(new_num)
        rev_text = text[::-1]
        
    return count
    
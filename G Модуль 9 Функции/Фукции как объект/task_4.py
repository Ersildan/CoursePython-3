def remove_marks(text, mark):
    remove_marks.count += 1
    for i in mark:
        text = text.replace(i ,"")
    return text

remove_marks.count = 0
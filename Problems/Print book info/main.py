def print_book_info(title, author=None, year=None):
    #  Write your code here
    string = f'"{title}" was written by {author} in {year}'
    if author is None and year is None:
        string = f'"{title}"'
    elif author is None:
        string = f'"{title}" was written in {year}'
    elif year is None:
        string = f'"{title}" was written by {author}'
    print(string)
    return string

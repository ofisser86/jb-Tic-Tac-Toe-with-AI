def heading(st, h_sign=1):
    return f"{'#' + ' ' + st if h_sign < 1 else '#' * h_sign + ' ' + st if h_sign < 7 else '#' * 6 + ' ' + st}"

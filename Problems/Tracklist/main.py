def tracklist(**kwargs):
    for k, v in kwargs.items():
        print(k)
        for k_, v_ in v.items():
            print(f'ALBUM: {k_} TRACK: {v_}')

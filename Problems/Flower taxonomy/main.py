iris = {}


def add_iris(*args, **kwargs):
    id_n, species, petal_length, petal_width = args
    iris.update({
        id_n:
            {'species': species,
             'petal_length': petal_length,
             'petal_width': petal_width,
             **kwargs}})

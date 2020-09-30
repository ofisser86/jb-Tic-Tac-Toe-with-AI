def add_viewer(name, fun_list=None):
    if fun_list is None:
        fun_list = []
    fun_list.append(name)
    return fun_list

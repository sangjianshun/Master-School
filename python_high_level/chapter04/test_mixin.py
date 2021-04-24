class SimpleItemContainer(object):
    def __init__(self, id, item_containers):
        self.id = id
        self.data = {}
        for item in item_containers:
            self.data[item.id] = item

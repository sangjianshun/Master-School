import numbers

class Field():
    pass
class IntField(Field):
    # 以下方法只实现一个方法就是属性描述符
    def __init__(self, db_column, min_value = None, max_value = None):
        self._value = None
        self.min_value = min_value
        self.max_value = max_value
        self.db_column = db_column
        if min_value is not None:
            if not isinstance(min_value, numbers.Integral):
                raise ValueError("min_value must be int")
            elif min_value < 0:
                raise ValueError("min_value must be positive int")
        if max_value is not None:
            if not isinstance(max_value, numbers.Integral):
                raise ValueError("max_value must be int")
            elif max_value < 0:
                raise ValueError("max_value must be positive int")
        if min_value > max_value:
            raise ValueError("min_value must be smaller than max_value")

    def __get__(self, instance, owner):
        return self._value
    def __set__(self, instance, value):
        if not isinstance(value, numbers.Integral):
            raise ValueError("int value need")
        if value < self.min_value or value > self.max_value:
            raise ValueError("value must between min_value and max_value")
        self._value = value

class CharField(Field):
    def __init__(self, db_column, max_length = None):
        self._value = None
        self.db_column = db_column
        self.max_length = max_length
        if max_length is None:
            raise ValueError("you must specify max_length for charfield")

    def __get__(self, instance, owner):
        return self._value
    def __set__(self, instance, value):
        if not isinstance(value, str):
            raise ValueError("int value need")
        if len(value)  > self.max_length:
            raise ValueError("value len excess len of max_length")
        self._value = value


class ModelMetaClass(type):
    def __new__(cls, name,bases,attrs, **kwargs):
        if name == "BaseModel":
            return super().__new__(cls, name,bases,attrs, **kwargs)
        fields = {}
        for key,value in attrs.items():
            if isinstance(value, Field):
                fields[key] = value
        attrs_meta = attrs.get("Meta", None)
        _meta = {}
        db_table = name.lower()
        if attrs_meta is not None:
            table = getattr(attrs_meta, "db_table", None)
            if table is not None:
                db_table = table
        _meta["db_table"] = db_table
        attrs["_meta"] = _meta
        attrs["fields"] = fields
        del attrs["Meta"]
        return super().__new__(cls, name,bases,attrs, **kwargs)

class BaseModel(metaclass=ModelMetaClass):
    def __init__(self, *args, **kwargs):
        for key,value in kwargs.items():
            setattr(self, key, value)
        return super().__init__()
    def save(self):
        pass

class User(BaseModel):
    name = CharField(db_column = "", max_length=10)
    age = IntField(db_column = "", min_value = 0, max_value = 100)

    class Meta:
        db_table = ""


if __name__ == '__main__':
    user = User(name = "test", age = "age")
    # user.name = "test"
    # user.age = 20
    user.save()
# -*- coding: utf-8 -*-
#  lxf_orm.py


'A simple ORM test using metaclass'


class Field(object):
    def __init__(self, name, column_type):
        self.name = name
        self.column_type = column_type

    def __str__(self):
        return '<%s:%s>' % (self.__class__.__name__, self.name)


class StringField(Field):
    def __init__(self, name):
        super(StringField, self).__init__(name, 'varchar(100)')


class IntegerField(Field):
    def __init__(self, name):
        super(IntegerField, self).__init__(name, 'bigint')


class ModelMetaclass(type):
    def __new__(cls, name, bases, attrs):
        if __name__ == 'Model':
            return type.__new__(cls, name, bases, attrs)
        print('Found model: %s' % name)
        print('attrs: %s' % str(attrs))
        print('cls: %s' % str(cls))
        print('bases: %s' % str(bases))
        mappings = dict()
        for k, v in attrs.items():
            if isinstance(v, Field):
                print('Found mapping: %s ==> %s' % (k, v))    # v是一个Field类
                mappings[k] = v
        for k in mappings.keys():
            attrs.pop(k)
        attrs['__mappings__'] = mappings    # 保存属性和列的映射关系
        attrs['__table__'] = name    # 假设表名和类名一致
        return type.__new__(cls, name, bases, attrs)


class Model(dict, metaclass=ModelMetaclass):
    def __init__(self, **kw):
        super(Model, self).__init__(**kw)

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r"'Model' object has no attribute '%s'" % key)

    def __setattr__(self, key, value):
        self[key] = value

    def save(self):
        fields = []
        params = []
        args = []
        for k, v in self.__mappings__.items():
            fields.append(v.name)    # v.name是字段名称
            # fields.append(k)    # k是属性名称
            params.append('?')
            args.append(getattr(self, k, None))
        sql = 'insert into %s (%s) values (%s)' % (
            self.__table__, ','.join(fields), ','.join(params)
        print('SQL: %s' % sql)
        print('ARGS: %s' % str(args))

    def delete(self):
        pass

    def select(self):
        pass

    def update(self):
        pass


# testing code:


class User(Model):
    id = IntegerField('id')
    name = StringField('username')
    email = StringField('email')
    password = StringField('password')


def main():
    u = User(id=12345, name='Charlie', email='test@orm.org', password='my-pwd')
    u.save()

if __name__ == '__main__':
    main()

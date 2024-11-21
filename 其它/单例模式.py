class Single(object):
    # 定义一个类属性，初始值为None，用来记录对象的引用
    record = None

    # 重写__new__()方法
    def __new__(cls, *args, **kwargs):
        print("这是new方法")
        # 进行判断，如果类属性是None,把__new__()返回的对象引用保存进去
        if cls.record is None:
            cls.record = super().__new__(cls)
        # 返回类属性中记录的对象引用1
        return cls.record

    def __init__(self):
        print("我是init")


s1 = Single()
print(f"s1:{s1}")
s2 = Single()
print(f"s2:{s2}")
# s1和s2完全相同
# 每一次实例化所创建的对象都是同一个，内存地址都一样
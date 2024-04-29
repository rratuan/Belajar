# Static Method dan Class Method

class MyClass:
    class_attribute = "Hello"

    def __init__(self, instance_attribute):
        self.instance_attribute = instance_attribute

    @classmethod
    def class_method(cls):
        print("Class attribute:", cls.class_attribute)
        new_instance = cls("World")  # Membuat instance objek dari kelas itu sendiri
        new_instance.instance_method()

    def instance_method(self):
        print("Instance attribute:", self.instance_attribute)

    @staticmethod
    def static_method():
        print("This is a static method")

# Membuat instance objek dari kelas
my_object = MyClass("OpenAI")

# Panggil instance method
my_object.instance_method()

# Panggil class method
MyClass.class_method()

# Panggil static method
MyClass.static_method()

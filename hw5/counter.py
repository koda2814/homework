"""
Написать декоратор instances_counter, который применяется к любому классу
и добавляет ему 2 метода:
get_created_instances - возвращает количество созданых экземпляров класса
reset_instances_counter - сбросить счетчик экземпляров,
возвращает значение до сброса
Имя декоратора и методов не менять

Ниже пример использования
"""


def instances_counter(cls):
    '''
    создает новый класс NewClass, который наследуется от переданного класса cls. 
    '''
    class NewClass(cls):
        created_instances = 0 #количество созданных экземпляров класса

        def __new__(cls, *args, **kwargs): 
            instance = super().__new__(cls) #переопределяем метод __new__, 
                                            #который будет вызываться при создании нового экземпляра класса
            NewClass.created_instances += 1
            return instance

        @classmethod
        def get_created_instances(cls):
            return cls.created_instances

        @classmethod
        def reset_instances_counter(cls):
            count = cls.created_instances
            cls.created_instances = 0
            return count

    return NewClass


@instances_counter
class User:
    pass


if __name__ == '__main__':

    User.get_created_instances()  # 0
    user, _, _ = User(), User(), User()
    user.get_created_instances()  # 3
    user.reset_instances_counter()  # 3

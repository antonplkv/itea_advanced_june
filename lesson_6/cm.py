class MyContextManager:

    def __init__(self, *args):
        self.args = args
        self.status = 1
        self.errors_texts_list = []

    def __enter__(self):
        print('Entered CM')
        if self.status == 1:
            return self
        raise ValueError('Object cannot be used')

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type == TypeError:
            self.errors_texts_list.append(exc_val)
            print('U did something wrong with types')
        print('CM exited')
        self.status = 0


# with MyContextManager(1, 2, 3, 4, 5, 100) as cm_obj:
#     print(cm_obj.status)
#     cm_obj.args[0] = 1

# print(cm_obj.status)


with open('text.txt', 'w') as file:
    file.write({1: 2})

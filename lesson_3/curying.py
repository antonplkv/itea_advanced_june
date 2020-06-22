def a(arg1):
    print(arg1)

    def b(arg2):
        print(arg2)

        def c(arg3):
            print(arg3)

            def d(arg4):
                print(arg1, arg2, arg3, arg4)

            return d
        return c
    return b


a(123)(321)(432)(900)
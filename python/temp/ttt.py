def main():
    def aa():
        def ab():
            def ac():
                def ad():
                    return 'return value 0'
                return ad()
            return ac()
        return ab()
    return aa()


print(main())


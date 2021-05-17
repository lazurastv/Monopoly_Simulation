def force_type_input(target_type):
    while True:
        try:
            return target_type(input())
        except ValueError:
            print("Incorrect type! Must be", target_type.__name__)

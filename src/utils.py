def get_float_input(prompt):
    try:
        return float(input(prompt))
    except ValueError:
        print("Invalid input.")
        return None
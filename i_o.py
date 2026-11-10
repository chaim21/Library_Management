def get_input(msg,valition,*kwargs):
    valid_input = False
    while not valid_input:
        choose = input(msg)
        user_input,msg_error = valition(choose,*kwargs)
        if not user_input:
            print(f"{msg_error}\n")
        else:
            return user_input
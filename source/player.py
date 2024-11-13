def pon():
    while True:
        user_input = int(input("1.グー\n2.チョキ\n3.パー\nあなたの手を選択してください。 >"))
        if user_input == 1 or 2 or 3:
            if user_input == 1:
                return "グー"
            elif user_input == 2:
                return "チョキ"
            else:
                return "パー"
        else:
            print("1, 2, 3のいずれかを入力してください。")
def judge(player_hand, computer_hand):
    if player_hand == computer_hand:
        return "引き分け"
    elif player_hand == "グー" and computer_hand == "チョキ" or player_hand == "チョキ" and computer_hand == "パー" or player_hand == "パー" and computer_hand == "グー":
        return "勝ち"
    else:
        return "負け"
import player
import computer
import janken_judge
def janken_main():
    player_wins = 0
    computer_wins = 0
    number_of_rounds = 1
    while player_wins + computer_wins < 3:
        print(f"-----ラウンド{number_of_rounds}-----")
        player_hand = player.pon()
        computer_hand = computer.pon()
        
        print(f"あなたの手: {player_hand}")
        print(f"コンピューターの手: {computer_hand}")
        
        result = janken_judge.judge(player_hand, computer_hand)
        
        if result == "勝ち":
            print("あなたの勝ちです!")
            player_wins += 1
        elif result == "負け":
            print("コンピューターの勝ちです!")
            computer_wins += 1
        number_of_rounds += 1
    print("【最終結果】")
    print(f"あなた{player_wins}勝")
    print(f"コンピューター{computer_wins}勝")
    
    if player_wins > computer_wins:
        print("あなたの総合勝利です！")
    else:
        print("コンピュータの総合勝利です！")

if __name__ == "__main__":
    janken_main()
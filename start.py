from dice import Dice
dice1 = Dice()
dice2 = Dice()
p1_wins_count = 0
p2_wins_count = 0
draw_count = 0
intro = """
Добро пожаловать!
...............................
Введите p чтобы играть
Чтобы закончить игру введите q
...............................
"""
print(intro)

while True:
    cmd = input("> ").lower()
    if cmd == 'p':
        player1 = dice1.roll()
        player2 = dice2.roll()
        print(f"Ваш бросок: {player1}")
        print(f"Бросок компьютера: {player2}")
        if (sum(player1) > sum(player2)):
            p1_wins_count += 1
            print("Вы выиграли!")
        elif (sum(player1) == sum(player2)):
            draw_count += 1
            print("Ничья!")
        else:
            p2_wins_count += 1
            print("Вы проиграли!")
    elif cmd == 'q':
        break
    else:
        print("Некорректная команда")
total = p1_wins_count + p2_wins_count + draw_count
statistics = f"""
Количество ваших побед: {p1_wins_count}
Количество побед компьютера: {p2_wins_count}
Количество ничьих: {draw_count}
Количество сыгранных партий: {total}
"""
print(statistics)

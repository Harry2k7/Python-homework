# Задача FOOTBALL необязательная. Напишите программу, которая принимает на стандартный вход список игр футбольных команд с результатом матча и выводит на стандартный вывод сводную таблицу результатов всех матчей. За победу команде начисляется 3 очка, за поражение — 0, за ничью — 1.
# Формат ввода следующий:
# В первой строке указано целое число nn — количество завершенных игр. После этого идет nn строк, в которых записаны результаты игры в следующем формате:
# Первая команда; Забитопервойкомандой; Втораякоманда; Забитовторойкомандой

# Вывод программы необходимо оформить следующим образом:
# Команда: Всего игр Побед Ничьих Поражений Всего очков
# Конкретный пример ввода-вывода приведён ниже.
# Порядок вывода команд произвольный.
# Пример входа:
# 3
# Спартак;9;Зенит;10
# Локомотив;12;Зенит;3
# Спартак;8;Локомотив;15

# Выход будет:
# Спартак: 2 0 0 2 0
# Зенит: 2 1 0 1 3
# Локомотив: 2 2 0 0 6


def calculate_points(results: list[str]) -> dict[str, dict[str, int]]:
    team_points: dict[str, dict[str, int]] = {}

    for match in results:
        team1, score1, team2, score2 = match.split(";")

        if team1 not in team_points:
            team_points[team1] = {"games": 0, "wins": 0, "draws": 0, "losses": 0, "points": 0}
        if team2 not in team_points:
            team_points[team2] = {"games": 0, "wins": 0, "draws": 0, "losses": 0, "points": 0}

        team_points[team1]["games"] += 1
        team_points[team2]["games"] += 1

        if score1 > score2:
            team_points[team2]["wins"] += 1
            team_points[team2]["points"] += 3
            team_points[team1]["losses"] += 1
        elif score1 < score2:
            team_points[team1]["wins"] += 1
            team_points[team1]["points"] += 3
            team_points[team2]["losses"] += 1
        else:
            team_points[team1]["draws"] += 1
            team_points[team1]["points"] += 1
            team_points[team2]["draws"] += 1
            team_points[team2]["points"] += 1

    return team_points


def display_table(team_points: dict[str, dict[str, int]]) -> None:
    print()
    print("Команда:    Всего игр Побед Ничьих Поражений Всего очков")

    for team, points in team_points.items():
        games = points["games"]
        wins = points["wins"]
        draws = points["draws"]
        losses = points["losses"]
        total_points = points["points"]

        print("{:<16s}{:<8d}{:<6d}{:<9d}{:<12d}{:<12d}".format(team, games, wins, draws, losses, total_points))


# Чтение ввода данных
n = int(input("Введите кол-во игр: "))
results = []
for _ in range(n):
    results.append(input())

# Вычисление результатов и вывод таблицы
team_points = calculate_points(results)
display_table(team_points)
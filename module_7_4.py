team1 = '"Мастера кода"' # команда 1
team2 = '"Волшебники данных"' # команда 2
team1_num = 5  # количество участников в команде 1
team2_num = 6  # количество участников в команде 2
score_1 = 40   # количество задач, решенных командой 1
score_2 = 42   # количество задач, решенных командой 2
team1_time = 1552.512
team2_time = 2153.31451
challenge_result = ''
tasks_total = score_1 + score_2
time_avg = round(((team1_time/score_1 + team2_time/score_2)/2), 2)

if score_1 > score_2 or score_1 == score_2 and team1_time > team2_time:
    challenge_result = f'победа команды {team1}'
elif score_1 < score_2 or score_1 == score_2 and team1_time < team2_time:
    challenge_result = f'победа команды {team2}'
else:
    challenge_result = 'Ничья!'

# Использование %
print('"В команде %(team1)s участников: %(team1_num)s!"' % {'team1': '"Мастера кода"', 'team1_num': team1_num})
print('"Итого сегодня в командах участников: %d и %d!"' % (team1_num, team2_num))

# Использование format()
print('"Команда "Волшебники данных" решила задач: {}!"'.format(score_2))
print('"{team2} решили задачи за {team1_time} c!"'.format(team2=team2, team1_time=team1_time))

# Использование f-строк
print(f'"Команды решили {score_1} и {score_2} задач."')
print(f'"Результат битвы: {challenge_result}!"')
print(f'"Сегодня было решено {tasks_total} задача, в среднем по {time_avg} секунды на задачу!"')

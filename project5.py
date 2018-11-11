# В файле input.txt указана температура в Новосибирске в первую неделю ноября (за каждый день.)
# Нужно найти среднюю температуру и вывести ее в output.txt, используя исключения.
# Пользователю предлагается ввести номер дня, а программа будет считать среднюю температуру с понедельника до
# этого дня.
with open("input.txt") as f_in:
    with open("output.txt", 'w') as f_out:
        text = ''
        for line in f_in:
            text += line
        Mo, Tu, We, Th, Fr, Sa, Su = text.split()
        while True:
            day = (input('Enter the number of days: '))
            try:
                day = int(day)
                break
            except ValueError:
                print('Value {} is not integer.'.format(day), file=f_out)
                continue
        day = day
        if day == 0:
            try:
                int(Mo) / day
            except ZeroDivisionError:
                print('division by 0', file=f_out)

        if day == 1:
            print('Average temperature for the first day: ', day, file=f_out)

        if day == 2:
            print('Average temperature for two days: ', (int(Mo) + int(Tu)) / day, file=f_out)

        if day == 3:
            print('Average temperature for two days: ', (int(Mo) + int(Tu) + int(We)) / day, file=f_out)

        if day == 4:
            print('Average temerature for two days: ', (int(Mo) + int(Tu) + int(We) + int(Th)) / day, file=f_out)

        if day == 5:
            print('Average temperature for two days: ', (int(Mo) + int(Tu) + int(We) + int(Th) + int(Fr)) / day,
                  file=f_out)

        if day == 6:
            print('Average temperature for two days: ', (int(Mo) + int(Tu) + int(We) + int(Th) + int(Fr) + int(Sa)) /
                  day, file=f_out)

        if day == 7:
            d = (int(Mo) + int(Tu) + int(We) + int(Th) + int(Fr) + int(Sa) + int(Su) / day)
            print('Average temperature for two days: ', d, file=f_out)



# Формирование строки со статусом ОК с выравниванием по правому краю в логе


def end_current_OK(message_text):
    total_string_OK_length = 100
    result = ''
    for i in range(1, total_string_OK_length - len(message_text)-2):
        result += '.'
    result += 'OK'
    return result

# Добавить запись в лог


def logwrite(logfile, arg, message_text=''):
    cur_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    if arg == 'step_begin' or arg == 'exception':
        print(message_text, end='')
        logfile.write(cur_time + ' ' + message_text)
    if arg == 'step_OK':
        print(end_current_OK(message_text))
        logfile.write(end_current_OK(message_text) + '\n')
    if arg == 'dop_info':
        print(message_text)
        logfile.write(cur_time + ' ' + message_text + '\n')
    if arg == 'empty':
        logfile.write('\n')

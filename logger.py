from datetime import datetime, date


class Logger:
    today = date.today()
    logger_path = f'./log_{today.month:02d}.{today.day:02d}.' + f'{today.year}'[2:] + '.txt'

    def __init__(self):
        try:
            with open(self.logger_path, 'x', encoding='UTF-8') as f:
                f.write('')
        except:
            with open(self.logger_path, 'a', encoding='UTF-8') as f:
                f.write('')

    @property
    def date(self):
        print(self.today)

    def write_log(self, event):
        now = f'[{datetime.now().hour}-{datetime.now().minute}-{datetime.now().second:02d}] '
        with open(self.logger_path, 'a', encoding='UTF-8') as f:
            f.write(now + event + '\n')

    def clear_log(self):
        with open(self.logger_path, 'w') as f:
            f.write('')

    def get_logs(self):
        with open(self.logger_path, 'r') as f:
            result = f.readlines()
        print(result)

    def get_last_event(self):
        with open(self.logger_path, 'r', encoding='UTF-8') as f:
            event = f.readlines()[-1]
        return event

    def get_all_logs(self):
        with open(self.logger_path, 'r', encoding='UTF-8') as f:
            events = f.readlines()
        return events

# l = Logger()
# from time import sleep
# logs = ['event 1', 'event 2', 'event 3']
# for log in logs:
#     l.write_log(log)
#     sleep(2)

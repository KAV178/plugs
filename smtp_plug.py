import asyncore
import os
from smtpd import SMTPServer


class EmlServer(SMTPServer):
    def process_message(self, peer, mailfrom, rcpttos, data):
        f = open(os.devnull, 'w')
        f.write(data)
        f.close
        print "data moved to devnull"


def run():
    foo = EmlServer(('localhost', 25), None)
    try:
        asyncore.loop()
    except KeyboardInterrupt:
        pass

if __name__ == '__main__':
    run()

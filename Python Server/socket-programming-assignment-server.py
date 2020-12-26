#!/usr/bin/env python


"""
Server file for Python training day 3 homework
"""

import random

from twisted.internet import protocol, reactor
from twisted.protocols import basic, policies


class ChallengeProtocol(basic.LineReceiver, policies.TimeoutMixin):
    """
    Protocol class for the challenge
    """

    # pylint: disable=invalid-name,too-many-instance-attributes

    def __init__(self):
        self.challenge_message = "Start: %c, end: %c, period: %d" + self.delimiter
        self.challenge_wrong = "Wrong! Got %s, expected %s" + self.delimiter
        self.curr_trial = 1
        self.domain = [('A', 'Z'), ('a', 'z')]
        self.done = "Yaay! All trials done! Nice job" + self.delimiter
        self.exp_ans = None
        self.max_trials = 50
        self.timeout = 3
        self.too_slow = "Boo! You're too slow! Bye!" + self.delimiter
        self.welcome = "Welcome to challenge. Timeout: %ds, total trials: %d" % \
                       (self.timeout, self.max_trials) + self.delimiter

    def connectionMade(self):
        self.setTimeout(self.timeout)
        self.transport.write(self.welcome)
        self.sendChallenge()
        return

    def lineReceived(self, line):
        answer = line.strip()
        if answer == self.exp_ans:
            if self.curr_trial == self.max_trials:
                self.transport.write(self.done)
                self.transport.loseConnection()
            else:
                self.curr_trial = self.curr_trial + 1
                self.sendChallenge()
        else:
            self.transport.write(self.challenge_wrong % (answer, self.exp_ans))
            self.transport.loseConnection()


    def sendChallenge(self):
        """
        Send next challenge to user
        """

        dom_start, dom_end = random.choice(self.domain)
        start = chr(random.choice(xrange(ord(dom_start), ord(dom_end))))
        end = chr(random.choice(xrange(ord(start) + 1, ord(dom_end) + 1)))
        period = random.choice(xrange(1, ord(end) - ord(start) + 1))
        self.exp_ans = ' '.join([chr(n) for n in xrange(ord(start), ord(end) + 1, period)])
        self.transport.write(self.challenge_message % (start, end, period))
        return

    def timeoutConnection(self):
        self.transport.write(self.too_slow)
        self.transport.loseConnection()


class ChallengeServerFactory(protocol.ServerFactory):
    """
    Factory class for the challenge
    """

    protocol = ChallengeProtocol

    def __init__(self, log_file):
        pass


if __name__ == "__main__":
    # pylint: disable=no-member
    reactor.listenTCP(7171, ChallengeServerFactory("logs"))
    reactor.run()

#!/usr/bin/env python


"""
Server file for Python training day 3 homework
"""

# "Standard library imports"
import os
import random
import struct

# "Imports from third party packages"
from twisted.internet import protocol, reactor
from twisted.protocols import basic, policies


class ChallengeProtocol(basic.LineReceiver, policies.TimeoutMixin):
    """
    Protocol class for the challenge
    """

    # pylint: disable=invalid-name,too-many-instance-attributes

    def __init__(self):
        self.byte_orders = {}
        self.challenge_message = "Byte order: %s; type(s): %s; input: %s" + self.delimiter
        self.challenge_wrong = "Wrong! Got %s, expected %s" + self.delimiter
        self.curr_trial = 1
        self.done = "Yaay! All trials done! Nice job" + self.delimiter
        self.exp_ans = None
        self.max_elem_count = 5
        self.min_elem_count = 1
        self.max_trials = 50
        self.timeout = 3
        self.too_slow = "Boo! You're too slow! Bye!" + self.delimiter
        self.types = {}
        self.welcome = "Welcome to challenge. Timeout: %ds, total trials: %d" % \
                       (self.timeout, self.max_trials) + self.delimiter

        self.populateByteOrder()
        self.populateTypes()

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

    def populateByteOrder(self):
        """
        Create byte order name to character code mapping
        """

        self.byte_orders['little-endian'] = '<'
        self.byte_orders['big-endian'] = '>'
        self.byte_orders['network'] = '!'
        return

    def populateTypes(self):
        """
        Create type to character code mapping
        """

        self.types["char"] = ('c', 1)
        self.types["signed char"] = ('b', 1)
        self.types["unsigned char"] = ('B', 1)
        self.types["bool"] = ('?', 1)
        self.types["short"] = ('h', 2)
        self.types["unsigned short"] = ('H', 2)
        self.types["int"] = ('i', 4)
        self.types["unsigned int"] = ('I', 4)
        self.types["long"] = ('l', 4)
        self.types["unsigned long"] = ('L', 4)
        self.types["long long"] = ('q', 8)
        self.types["unsigned long long"] = ('Q', 8)
        self.types["float"] = ('f', 4)
        self.types["double"] = ('d', 8)
        return

    def sendChallenge(self):
        """
        Send next challenge to user
        """

        byte_order = random.choice(self.byte_orders.keys())
        elem_count = random.randint(self.min_elem_count, self.max_elem_count)
        encoding = [random.choice(self.types.keys()) for _ in xrange(elem_count)]
        packing_format_str = ''.join([self.types[elem][0] for elem in encoding])
        packing_format_str = self.byte_orders[byte_order] + packing_format_str
        chal_bytes_len = sum([self.types[elem][1] for elem in encoding])
        chal_bytes = os.urandom(chal_bytes_len)
        self.exp_ans = str(struct.unpack(packing_format_str, chal_bytes))
        values = (byte_order, ', '.join(encoding), chal_bytes)
        self.transport.write(self.challenge_message % values)
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

# Generated from src/zorg/grammar/zorg_query/ZorgQuery.g4 by ANTLR 4.13.1
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


def serializedATN():
    return [
        4,0,17,78,6,-1,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,
        6,7,6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,
        7,13,2,14,7,14,2,15,7,15,2,16,7,16,1,0,1,0,1,1,1,1,1,2,1,2,1,3,1,
        3,1,4,1,4,1,4,1,4,1,4,1,5,1,5,1,5,1,5,1,5,1,6,3,6,55,8,6,1,6,1,6,
        1,7,1,7,1,8,1,8,1,9,1,9,1,10,1,10,1,11,1,11,1,12,1,12,1,13,1,13,
        1,14,1,14,1,15,1,15,1,16,1,16,0,0,17,1,1,3,2,5,3,7,4,9,5,11,6,13,
        7,15,8,17,9,19,10,21,11,23,12,25,13,27,14,29,15,31,16,33,17,1,0,
        0,78,0,1,1,0,0,0,0,3,1,0,0,0,0,5,1,0,0,0,0,7,1,0,0,0,0,9,1,0,0,0,
        0,11,1,0,0,0,0,13,1,0,0,0,0,15,1,0,0,0,0,17,1,0,0,0,0,19,1,0,0,0,
        0,21,1,0,0,0,0,23,1,0,0,0,0,25,1,0,0,0,0,27,1,0,0,0,0,29,1,0,0,0,
        0,31,1,0,0,0,0,33,1,0,0,0,1,35,1,0,0,0,3,37,1,0,0,0,5,39,1,0,0,0,
        7,41,1,0,0,0,9,43,1,0,0,0,11,48,1,0,0,0,13,54,1,0,0,0,15,58,1,0,
        0,0,17,60,1,0,0,0,19,62,1,0,0,0,21,64,1,0,0,0,23,66,1,0,0,0,25,68,
        1,0,0,0,27,70,1,0,0,0,29,72,1,0,0,0,31,74,1,0,0,0,33,76,1,0,0,0,
        35,36,5,83,0,0,36,2,1,0,0,0,37,38,5,87,0,0,38,4,1,0,0,0,39,40,5,
        79,0,0,40,6,1,0,0,0,41,42,5,71,0,0,42,8,1,0,0,0,43,44,5,102,0,0,
        44,45,5,105,0,0,45,46,5,108,0,0,46,47,5,101,0,0,47,10,1,0,0,0,48,
        49,5,110,0,0,49,50,5,111,0,0,50,51,5,116,0,0,51,52,5,101,0,0,52,
        12,1,0,0,0,53,55,5,13,0,0,54,53,1,0,0,0,54,55,1,0,0,0,55,56,1,0,
        0,0,56,57,5,10,0,0,57,14,1,0,0,0,58,59,5,32,0,0,59,16,1,0,0,0,60,
        61,5,43,0,0,61,18,1,0,0,0,62,63,5,64,0,0,63,20,1,0,0,0,64,65,5,37,
        0,0,65,22,1,0,0,0,66,67,5,35,0,0,67,24,1,0,0,0,68,69,5,45,0,0,69,
        26,1,0,0,0,70,71,5,111,0,0,71,28,1,0,0,0,72,73,5,120,0,0,73,30,1,
        0,0,0,74,75,5,60,0,0,75,32,1,0,0,0,76,77,5,62,0,0,77,34,1,0,0,0,
        2,0,54,0
    ]

class ZorgQueryLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    T__2 = 3
    T__3 = 4
    T__4 = 5
    T__5 = 6
    NL = 7
    SPACE = 8
    PLUS = 9
    AT_SIGN = 10
    PERCENT = 11
    HASH = 12
    DASH = 13
    LOWER_O = 14
    LOWER_X = 15
    LANGLE = 16
    RANGLE = 17

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'S'", "'W'", "'O'", "'G'", "'file'", "'note'", "' '", "'+'", 
            "'@'", "'%'", "'#'", "'-'", "'o'", "'x'", "'<'", "'>'" ]

    symbolicNames = [ "<INVALID>",
            "NL", "SPACE", "PLUS", "AT_SIGN", "PERCENT", "HASH", "DASH", 
            "LOWER_O", "LOWER_X", "LANGLE", "RANGLE" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "T__4", "T__5", "NL", 
                  "SPACE", "PLUS", "AT_SIGN", "PERCENT", "HASH", "DASH", 
                  "LOWER_O", "LOWER_X", "LANGLE", "RANGLE" ]

    grammarFileName = "ZorgQuery.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None



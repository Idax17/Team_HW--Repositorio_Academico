# Generated from DockerNetworks.g4 by ANTLR 4.13.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,11,47,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,1,0,1,0,1,0,4,
        0,14,8,0,11,0,12,0,15,1,0,1,0,1,1,1,1,1,1,4,1,23,8,1,11,1,12,1,24,
        1,2,1,2,1,2,1,2,1,2,1,2,3,2,33,8,2,1,3,1,3,1,3,4,3,38,8,3,11,3,12,
        3,39,1,4,1,4,1,4,1,4,1,4,1,4,0,0,5,0,2,4,6,8,0,0,45,0,10,1,0,0,0,
        2,19,1,0,0,0,4,32,1,0,0,0,6,34,1,0,0,0,8,41,1,0,0,0,10,11,5,1,0,
        0,11,13,5,6,0,0,12,14,3,2,1,0,13,12,1,0,0,0,14,15,1,0,0,0,15,13,
        1,0,0,0,15,16,1,0,0,0,16,17,1,0,0,0,17,18,5,0,0,1,18,1,1,0,0,0,19,
        20,5,8,0,0,20,22,5,6,0,0,21,23,3,4,2,0,22,21,1,0,0,0,23,24,1,0,0,
        0,24,22,1,0,0,0,24,25,1,0,0,0,25,3,1,0,0,0,26,27,5,2,0,0,27,28,5,
        6,0,0,28,33,5,9,0,0,29,30,5,3,0,0,30,31,5,6,0,0,31,33,3,6,3,0,32,
        26,1,0,0,0,32,29,1,0,0,0,33,5,1,0,0,0,34,35,5,4,0,0,35,37,5,6,0,
        0,36,38,3,8,4,0,37,36,1,0,0,0,38,39,1,0,0,0,39,37,1,0,0,0,39,40,
        1,0,0,0,40,7,1,0,0,0,41,42,5,7,0,0,42,43,5,5,0,0,43,44,5,6,0,0,44,
        45,5,10,0,0,45,9,1,0,0,0,4,15,24,32,39
    ]

class DockerNetworksParser ( Parser ):

    grammarFileName = "DockerNetworks.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'networks'", "'driver'", "'ipam'", "'config'", 
                     "'subnet'", "':'", "'-'" ]

    symbolicNames = [ "<INVALID>", "NETWORKS_KEY", "DRIVER_KEY", "IPAM_KEY", 
                      "CONFIG_KEY", "SUBNET_KEY", "COLON", "DASH", "ID", 
                      "STRING", "IP_CIDR", "WS" ]

    RULE_composeFile = 0
    RULE_networkDef = 1
    RULE_property = 2
    RULE_ipamDef = 3
    RULE_dashConfig = 4

    ruleNames =  [ "composeFile", "networkDef", "property", "ipamDef", "dashConfig" ]

    EOF = Token.EOF
    NETWORKS_KEY=1
    DRIVER_KEY=2
    IPAM_KEY=3
    CONFIG_KEY=4
    SUBNET_KEY=5
    COLON=6
    DASH=7
    ID=8
    STRING=9
    IP_CIDR=10
    WS=11

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ComposeFileContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NETWORKS_KEY(self):
            return self.getToken(DockerNetworksParser.NETWORKS_KEY, 0)

        def COLON(self):
            return self.getToken(DockerNetworksParser.COLON, 0)

        def EOF(self):
            return self.getToken(DockerNetworksParser.EOF, 0)

        def networkDef(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(DockerNetworksParser.NetworkDefContext)
            else:
                return self.getTypedRuleContext(DockerNetworksParser.NetworkDefContext,i)


        def getRuleIndex(self):
            return DockerNetworksParser.RULE_composeFile

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterComposeFile" ):
                listener.enterComposeFile(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitComposeFile" ):
                listener.exitComposeFile(self)




    def composeFile(self):

        localctx = DockerNetworksParser.ComposeFileContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_composeFile)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 10
            self.match(DockerNetworksParser.NETWORKS_KEY)
            self.state = 11
            self.match(DockerNetworksParser.COLON)
            self.state = 13 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 12
                self.networkDef()
                self.state = 15 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==8):
                    break

            self.state = 17
            self.match(DockerNetworksParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class NetworkDefContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(DockerNetworksParser.ID, 0)

        def COLON(self):
            return self.getToken(DockerNetworksParser.COLON, 0)

        def property_(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(DockerNetworksParser.PropertyContext)
            else:
                return self.getTypedRuleContext(DockerNetworksParser.PropertyContext,i)


        def getRuleIndex(self):
            return DockerNetworksParser.RULE_networkDef

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNetworkDef" ):
                listener.enterNetworkDef(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNetworkDef" ):
                listener.exitNetworkDef(self)




    def networkDef(self):

        localctx = DockerNetworksParser.NetworkDefContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_networkDef)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 19
            self.match(DockerNetworksParser.ID)
            self.state = 20
            self.match(DockerNetworksParser.COLON)
            self.state = 22 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 21
                self.property_()
                self.state = 24 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==2 or _la==3):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PropertyContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DRIVER_KEY(self):
            return self.getToken(DockerNetworksParser.DRIVER_KEY, 0)

        def COLON(self):
            return self.getToken(DockerNetworksParser.COLON, 0)

        def STRING(self):
            return self.getToken(DockerNetworksParser.STRING, 0)

        def IPAM_KEY(self):
            return self.getToken(DockerNetworksParser.IPAM_KEY, 0)

        def ipamDef(self):
            return self.getTypedRuleContext(DockerNetworksParser.IpamDefContext,0)


        def getRuleIndex(self):
            return DockerNetworksParser.RULE_property

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProperty" ):
                listener.enterProperty(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProperty" ):
                listener.exitProperty(self)




    def property_(self):

        localctx = DockerNetworksParser.PropertyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_property)
        try:
            self.state = 32
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [2]:
                self.enterOuterAlt(localctx, 1)
                self.state = 26
                self.match(DockerNetworksParser.DRIVER_KEY)
                self.state = 27
                self.match(DockerNetworksParser.COLON)
                self.state = 28
                self.match(DockerNetworksParser.STRING)
                pass
            elif token in [3]:
                self.enterOuterAlt(localctx, 2)
                self.state = 29
                self.match(DockerNetworksParser.IPAM_KEY)
                self.state = 30
                self.match(DockerNetworksParser.COLON)
                self.state = 31
                self.ipamDef()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IpamDefContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CONFIG_KEY(self):
            return self.getToken(DockerNetworksParser.CONFIG_KEY, 0)

        def COLON(self):
            return self.getToken(DockerNetworksParser.COLON, 0)

        def dashConfig(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(DockerNetworksParser.DashConfigContext)
            else:
                return self.getTypedRuleContext(DockerNetworksParser.DashConfigContext,i)


        def getRuleIndex(self):
            return DockerNetworksParser.RULE_ipamDef

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIpamDef" ):
                listener.enterIpamDef(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIpamDef" ):
                listener.exitIpamDef(self)




    def ipamDef(self):

        localctx = DockerNetworksParser.IpamDefContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_ipamDef)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 34
            self.match(DockerNetworksParser.CONFIG_KEY)
            self.state = 35
            self.match(DockerNetworksParser.COLON)
            self.state = 37 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 36
                self.dashConfig()
                self.state = 39 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==7):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DashConfigContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DASH(self):
            return self.getToken(DockerNetworksParser.DASH, 0)

        def SUBNET_KEY(self):
            return self.getToken(DockerNetworksParser.SUBNET_KEY, 0)

        def COLON(self):
            return self.getToken(DockerNetworksParser.COLON, 0)

        def IP_CIDR(self):
            return self.getToken(DockerNetworksParser.IP_CIDR, 0)

        def getRuleIndex(self):
            return DockerNetworksParser.RULE_dashConfig

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDashConfig" ):
                listener.enterDashConfig(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDashConfig" ):
                listener.exitDashConfig(self)




    def dashConfig(self):

        localctx = DockerNetworksParser.DashConfigContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_dashConfig)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 41
            self.match(DockerNetworksParser.DASH)
            self.state = 42
            self.match(DockerNetworksParser.SUBNET_KEY)
            self.state = 43
            self.match(DockerNetworksParser.COLON)
            self.state = 44
            self.match(DockerNetworksParser.IP_CIDR)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx






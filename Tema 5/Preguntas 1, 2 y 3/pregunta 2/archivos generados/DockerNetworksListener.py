# Generated from DockerNetworks.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .DockerNetworksParser import DockerNetworksParser
else:
    from DockerNetworksParser import DockerNetworksParser

# This class defines a complete listener for a parse tree produced by DockerNetworksParser.
class DockerNetworksListener(ParseTreeListener):

    # Enter a parse tree produced by DockerNetworksParser#composeFile.
    def enterComposeFile(self, ctx:DockerNetworksParser.ComposeFileContext):
        pass

    # Exit a parse tree produced by DockerNetworksParser#composeFile.
    def exitComposeFile(self, ctx:DockerNetworksParser.ComposeFileContext):
        pass


    # Enter a parse tree produced by DockerNetworksParser#networkDef.
    def enterNetworkDef(self, ctx:DockerNetworksParser.NetworkDefContext):
        pass

    # Exit a parse tree produced by DockerNetworksParser#networkDef.
    def exitNetworkDef(self, ctx:DockerNetworksParser.NetworkDefContext):
        pass


    # Enter a parse tree produced by DockerNetworksParser#property.
    def enterProperty(self, ctx:DockerNetworksParser.PropertyContext):
        pass

    # Exit a parse tree produced by DockerNetworksParser#property.
    def exitProperty(self, ctx:DockerNetworksParser.PropertyContext):
        pass


    # Enter a parse tree produced by DockerNetworksParser#ipamDef.
    def enterIpamDef(self, ctx:DockerNetworksParser.IpamDefContext):
        pass

    # Exit a parse tree produced by DockerNetworksParser#ipamDef.
    def exitIpamDef(self, ctx:DockerNetworksParser.IpamDefContext):
        pass


    # Enter a parse tree produced by DockerNetworksParser#dashConfig.
    def enterDashConfig(self, ctx:DockerNetworksParser.DashConfigContext):
        pass

    # Exit a parse tree produced by DockerNetworksParser#dashConfig.
    def exitDashConfig(self, ctx:DockerNetworksParser.DashConfigContext):
        pass



del DockerNetworksParser
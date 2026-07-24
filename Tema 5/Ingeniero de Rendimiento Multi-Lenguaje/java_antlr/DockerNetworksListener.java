// Generated from DockerNetworks.g4 by ANTLR 4.13.1
import org.antlr.v4.runtime.tree.ParseTreeListener;

/**
 * This interface defines a complete listener for a parse tree produced by
 * {@link DockerNetworksParser}.
 */
public interface DockerNetworksListener extends ParseTreeListener {
	/**
	 * Enter a parse tree produced by {@link DockerNetworksParser#composeFile}.
	 * @param ctx the parse tree
	 */
	void enterComposeFile(DockerNetworksParser.ComposeFileContext ctx);
	/**
	 * Exit a parse tree produced by {@link DockerNetworksParser#composeFile}.
	 * @param ctx the parse tree
	 */
	void exitComposeFile(DockerNetworksParser.ComposeFileContext ctx);
	/**
	 * Enter a parse tree produced by {@link DockerNetworksParser#networkDef}.
	 * @param ctx the parse tree
	 */
	void enterNetworkDef(DockerNetworksParser.NetworkDefContext ctx);
	/**
	 * Exit a parse tree produced by {@link DockerNetworksParser#networkDef}.
	 * @param ctx the parse tree
	 */
	void exitNetworkDef(DockerNetworksParser.NetworkDefContext ctx);
	/**
	 * Enter a parse tree produced by {@link DockerNetworksParser#property}.
	 * @param ctx the parse tree
	 */
	void enterProperty(DockerNetworksParser.PropertyContext ctx);
	/**
	 * Exit a parse tree produced by {@link DockerNetworksParser#property}.
	 * @param ctx the parse tree
	 */
	void exitProperty(DockerNetworksParser.PropertyContext ctx);
	/**
	 * Enter a parse tree produced by {@link DockerNetworksParser#ipamDef}.
	 * @param ctx the parse tree
	 */
	void enterIpamDef(DockerNetworksParser.IpamDefContext ctx);
	/**
	 * Exit a parse tree produced by {@link DockerNetworksParser#ipamDef}.
	 * @param ctx the parse tree
	 */
	void exitIpamDef(DockerNetworksParser.IpamDefContext ctx);
	/**
	 * Enter a parse tree produced by {@link DockerNetworksParser#dashConfig}.
	 * @param ctx the parse tree
	 */
	void enterDashConfig(DockerNetworksParser.DashConfigContext ctx);
	/**
	 * Exit a parse tree produced by {@link DockerNetworksParser#dashConfig}.
	 * @param ctx the parse tree
	 */
	void exitDashConfig(DockerNetworksParser.DashConfigContext ctx);
}
// Generated from DockerNetworks.g4 by ANTLR 4.13.1
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.misc.*;
import org.antlr.v4.runtime.tree.*;
import java.util.List;
import java.util.Iterator;
import java.util.ArrayList;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast", "CheckReturnValue"})
public class DockerNetworksParser extends Parser {
	static { RuntimeMetaData.checkVersion("4.13.1", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		NETWORKS_KEY=1, DRIVER_KEY=2, IPAM_KEY=3, CONFIG_KEY=4, SUBNET_KEY=5, 
		COLON=6, DASH=7, ID=8, STRING=9, IP_CIDR=10, WS=11;
	public static final int
		RULE_composeFile = 0, RULE_networkDef = 1, RULE_property = 2, RULE_ipamDef = 3, 
		RULE_dashConfig = 4;
	private static String[] makeRuleNames() {
		return new String[] {
			"composeFile", "networkDef", "property", "ipamDef", "dashConfig"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, "'networks'", "'driver'", "'ipam'", "'config'", "'subnet'", "':'", 
			"'-'"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, "NETWORKS_KEY", "DRIVER_KEY", "IPAM_KEY", "CONFIG_KEY", "SUBNET_KEY", 
			"COLON", "DASH", "ID", "STRING", "IP_CIDR", "WS"
		};
	}
	private static final String[] _SYMBOLIC_NAMES = makeSymbolicNames();
	public static final Vocabulary VOCABULARY = new VocabularyImpl(_LITERAL_NAMES, _SYMBOLIC_NAMES);

	/**
	 * @deprecated Use {@link #VOCABULARY} instead.
	 */
	@Deprecated
	public static final String[] tokenNames;
	static {
		tokenNames = new String[_SYMBOLIC_NAMES.length];
		for (int i = 0; i < tokenNames.length; i++) {
			tokenNames[i] = VOCABULARY.getLiteralName(i);
			if (tokenNames[i] == null) {
				tokenNames[i] = VOCABULARY.getSymbolicName(i);
			}

			if (tokenNames[i] == null) {
				tokenNames[i] = "<INVALID>";
			}
		}
	}

	@Override
	@Deprecated
	public String[] getTokenNames() {
		return tokenNames;
	}

	@Override

	public Vocabulary getVocabulary() {
		return VOCABULARY;
	}

	@Override
	public String getGrammarFileName() { return "DockerNetworks.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public ATN getATN() { return _ATN; }

	public DockerNetworksParser(TokenStream input) {
		super(input);
		_interp = new ParserATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ComposeFileContext extends ParserRuleContext {
		public TerminalNode NETWORKS_KEY() { return getToken(DockerNetworksParser.NETWORKS_KEY, 0); }
		public TerminalNode COLON() { return getToken(DockerNetworksParser.COLON, 0); }
		public TerminalNode EOF() { return getToken(DockerNetworksParser.EOF, 0); }
		public List<NetworkDefContext> networkDef() {
			return getRuleContexts(NetworkDefContext.class);
		}
		public NetworkDefContext networkDef(int i) {
			return getRuleContext(NetworkDefContext.class,i);
		}
		public ComposeFileContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_composeFile; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof DockerNetworksListener ) ((DockerNetworksListener)listener).enterComposeFile(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof DockerNetworksListener ) ((DockerNetworksListener)listener).exitComposeFile(this);
		}
	}

	public final ComposeFileContext composeFile() throws RecognitionException {
		ComposeFileContext _localctx = new ComposeFileContext(_ctx, getState());
		enterRule(_localctx, 0, RULE_composeFile);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(10);
			match(NETWORKS_KEY);
			setState(11);
			match(COLON);
			setState(13); 
			_errHandler.sync(this);
			_la = _input.LA(1);
			do {
				{
				{
				setState(12);
				networkDef();
				}
				}
				setState(15); 
				_errHandler.sync(this);
				_la = _input.LA(1);
			} while ( _la==ID );
			setState(17);
			match(EOF);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class NetworkDefContext extends ParserRuleContext {
		public TerminalNode ID() { return getToken(DockerNetworksParser.ID, 0); }
		public TerminalNode COLON() { return getToken(DockerNetworksParser.COLON, 0); }
		public List<PropertyContext> property() {
			return getRuleContexts(PropertyContext.class);
		}
		public PropertyContext property(int i) {
			return getRuleContext(PropertyContext.class,i);
		}
		public NetworkDefContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_networkDef; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof DockerNetworksListener ) ((DockerNetworksListener)listener).enterNetworkDef(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof DockerNetworksListener ) ((DockerNetworksListener)listener).exitNetworkDef(this);
		}
	}

	public final NetworkDefContext networkDef() throws RecognitionException {
		NetworkDefContext _localctx = new NetworkDefContext(_ctx, getState());
		enterRule(_localctx, 2, RULE_networkDef);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(19);
			match(ID);
			setState(20);
			match(COLON);
			setState(22); 
			_errHandler.sync(this);
			_la = _input.LA(1);
			do {
				{
				{
				setState(21);
				property();
				}
				}
				setState(24); 
				_errHandler.sync(this);
				_la = _input.LA(1);
			} while ( _la==DRIVER_KEY || _la==IPAM_KEY );
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class PropertyContext extends ParserRuleContext {
		public TerminalNode DRIVER_KEY() { return getToken(DockerNetworksParser.DRIVER_KEY, 0); }
		public TerminalNode COLON() { return getToken(DockerNetworksParser.COLON, 0); }
		public TerminalNode STRING() { return getToken(DockerNetworksParser.STRING, 0); }
		public TerminalNode IPAM_KEY() { return getToken(DockerNetworksParser.IPAM_KEY, 0); }
		public IpamDefContext ipamDef() {
			return getRuleContext(IpamDefContext.class,0);
		}
		public PropertyContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_property; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof DockerNetworksListener ) ((DockerNetworksListener)listener).enterProperty(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof DockerNetworksListener ) ((DockerNetworksListener)listener).exitProperty(this);
		}
	}

	public final PropertyContext property() throws RecognitionException {
		PropertyContext _localctx = new PropertyContext(_ctx, getState());
		enterRule(_localctx, 4, RULE_property);
		try {
			setState(32);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case DRIVER_KEY:
				enterOuterAlt(_localctx, 1);
				{
				setState(26);
				match(DRIVER_KEY);
				setState(27);
				match(COLON);
				setState(28);
				match(STRING);
				}
				break;
			case IPAM_KEY:
				enterOuterAlt(_localctx, 2);
				{
				setState(29);
				match(IPAM_KEY);
				setState(30);
				match(COLON);
				setState(31);
				ipamDef();
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class IpamDefContext extends ParserRuleContext {
		public TerminalNode CONFIG_KEY() { return getToken(DockerNetworksParser.CONFIG_KEY, 0); }
		public TerminalNode COLON() { return getToken(DockerNetworksParser.COLON, 0); }
		public List<DashConfigContext> dashConfig() {
			return getRuleContexts(DashConfigContext.class);
		}
		public DashConfigContext dashConfig(int i) {
			return getRuleContext(DashConfigContext.class,i);
		}
		public IpamDefContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_ipamDef; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof DockerNetworksListener ) ((DockerNetworksListener)listener).enterIpamDef(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof DockerNetworksListener ) ((DockerNetworksListener)listener).exitIpamDef(this);
		}
	}

	public final IpamDefContext ipamDef() throws RecognitionException {
		IpamDefContext _localctx = new IpamDefContext(_ctx, getState());
		enterRule(_localctx, 6, RULE_ipamDef);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(34);
			match(CONFIG_KEY);
			setState(35);
			match(COLON);
			setState(37); 
			_errHandler.sync(this);
			_la = _input.LA(1);
			do {
				{
				{
				setState(36);
				dashConfig();
				}
				}
				setState(39); 
				_errHandler.sync(this);
				_la = _input.LA(1);
			} while ( _la==DASH );
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class DashConfigContext extends ParserRuleContext {
		public TerminalNode DASH() { return getToken(DockerNetworksParser.DASH, 0); }
		public TerminalNode SUBNET_KEY() { return getToken(DockerNetworksParser.SUBNET_KEY, 0); }
		public TerminalNode COLON() { return getToken(DockerNetworksParser.COLON, 0); }
		public TerminalNode IP_CIDR() { return getToken(DockerNetworksParser.IP_CIDR, 0); }
		public DashConfigContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_dashConfig; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof DockerNetworksListener ) ((DockerNetworksListener)listener).enterDashConfig(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof DockerNetworksListener ) ((DockerNetworksListener)listener).exitDashConfig(this);
		}
	}

	public final DashConfigContext dashConfig() throws RecognitionException {
		DashConfigContext _localctx = new DashConfigContext(_ctx, getState());
		enterRule(_localctx, 8, RULE_dashConfig);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(41);
			match(DASH);
			setState(42);
			match(SUBNET_KEY);
			setState(43);
			match(COLON);
			setState(44);
			match(IP_CIDR);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static final String _serializedATN =
		"\u0004\u0001\u000b/\u0002\u0000\u0007\u0000\u0002\u0001\u0007\u0001\u0002"+
		"\u0002\u0007\u0002\u0002\u0003\u0007\u0003\u0002\u0004\u0007\u0004\u0001"+
		"\u0000\u0001\u0000\u0001\u0000\u0004\u0000\u000e\b\u0000\u000b\u0000\f"+
		"\u0000\u000f\u0001\u0000\u0001\u0000\u0001\u0001\u0001\u0001\u0001\u0001"+
		"\u0004\u0001\u0017\b\u0001\u000b\u0001\f\u0001\u0018\u0001\u0002\u0001"+
		"\u0002\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0002\u0003\u0002!\b"+
		"\u0002\u0001\u0003\u0001\u0003\u0001\u0003\u0004\u0003&\b\u0003\u000b"+
		"\u0003\f\u0003\'\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0004\u0001"+
		"\u0004\u0001\u0004\u0000\u0000\u0005\u0000\u0002\u0004\u0006\b\u0000\u0000"+
		"-\u0000\n\u0001\u0000\u0000\u0000\u0002\u0013\u0001\u0000\u0000\u0000"+
		"\u0004 \u0001\u0000\u0000\u0000\u0006\"\u0001\u0000\u0000\u0000\b)\u0001"+
		"\u0000\u0000\u0000\n\u000b\u0005\u0001\u0000\u0000\u000b\r\u0005\u0006"+
		"\u0000\u0000\f\u000e\u0003\u0002\u0001\u0000\r\f\u0001\u0000\u0000\u0000"+
		"\u000e\u000f\u0001\u0000\u0000\u0000\u000f\r\u0001\u0000\u0000\u0000\u000f"+
		"\u0010\u0001\u0000\u0000\u0000\u0010\u0011\u0001\u0000\u0000\u0000\u0011"+
		"\u0012\u0005\u0000\u0000\u0001\u0012\u0001\u0001\u0000\u0000\u0000\u0013"+
		"\u0014\u0005\b\u0000\u0000\u0014\u0016\u0005\u0006\u0000\u0000\u0015\u0017"+
		"\u0003\u0004\u0002\u0000\u0016\u0015\u0001\u0000\u0000\u0000\u0017\u0018"+
		"\u0001\u0000\u0000\u0000\u0018\u0016\u0001\u0000\u0000\u0000\u0018\u0019"+
		"\u0001\u0000\u0000\u0000\u0019\u0003\u0001\u0000\u0000\u0000\u001a\u001b"+
		"\u0005\u0002\u0000\u0000\u001b\u001c\u0005\u0006\u0000\u0000\u001c!\u0005"+
		"\t\u0000\u0000\u001d\u001e\u0005\u0003\u0000\u0000\u001e\u001f\u0005\u0006"+
		"\u0000\u0000\u001f!\u0003\u0006\u0003\u0000 \u001a\u0001\u0000\u0000\u0000"+
		" \u001d\u0001\u0000\u0000\u0000!\u0005\u0001\u0000\u0000\u0000\"#\u0005"+
		"\u0004\u0000\u0000#%\u0005\u0006\u0000\u0000$&\u0003\b\u0004\u0000%$\u0001"+
		"\u0000\u0000\u0000&\'\u0001\u0000\u0000\u0000\'%\u0001\u0000\u0000\u0000"+
		"\'(\u0001\u0000\u0000\u0000(\u0007\u0001\u0000\u0000\u0000)*\u0005\u0007"+
		"\u0000\u0000*+\u0005\u0005\u0000\u0000+,\u0005\u0006\u0000\u0000,-\u0005"+
		"\n\u0000\u0000-\t\u0001\u0000\u0000\u0000\u0004\u000f\u0018 \'";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}
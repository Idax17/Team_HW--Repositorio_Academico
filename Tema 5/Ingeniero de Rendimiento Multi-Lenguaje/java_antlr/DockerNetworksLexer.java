// Generated from DockerNetworks.g4 by ANTLR 4.13.1
import org.antlr.v4.runtime.Lexer;
import org.antlr.v4.runtime.CharStream;
import org.antlr.v4.runtime.Token;
import org.antlr.v4.runtime.TokenStream;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.misc.*;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast", "CheckReturnValue", "this-escape"})
public class DockerNetworksLexer extends Lexer {
	static { RuntimeMetaData.checkVersion("4.13.1", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		NETWORKS_KEY=1, DRIVER_KEY=2, IPAM_KEY=3, CONFIG_KEY=4, SUBNET_KEY=5, 
		COLON=6, DASH=7, ID=8, STRING=9, IP_CIDR=10, WS=11;
	public static String[] channelNames = {
		"DEFAULT_TOKEN_CHANNEL", "HIDDEN"
	};

	public static String[] modeNames = {
		"DEFAULT_MODE"
	};

	private static String[] makeRuleNames() {
		return new String[] {
			"NETWORKS_KEY", "DRIVER_KEY", "IPAM_KEY", "CONFIG_KEY", "SUBNET_KEY", 
			"COLON", "DASH", "ID", "STRING", "IP_CIDR", "WS"
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


	public DockerNetworksLexer(CharStream input) {
		super(input);
		_interp = new LexerATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	@Override
	public String getGrammarFileName() { return "DockerNetworks.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public String[] getChannelNames() { return channelNames; }

	@Override
	public String[] getModeNames() { return modeNames; }

	@Override
	public ATN getATN() { return _ATN; }

	public static final String _serializedATN =
		"\u0004\u0000\u000bn\u0006\uffff\uffff\u0002\u0000\u0007\u0000\u0002\u0001"+
		"\u0007\u0001\u0002\u0002\u0007\u0002\u0002\u0003\u0007\u0003\u0002\u0004"+
		"\u0007\u0004\u0002\u0005\u0007\u0005\u0002\u0006\u0007\u0006\u0002\u0007"+
		"\u0007\u0007\u0002\b\u0007\b\u0002\t\u0007\t\u0002\n\u0007\n\u0001\u0000"+
		"\u0001\u0000\u0001\u0000\u0001\u0000\u0001\u0000\u0001\u0000\u0001\u0000"+
		"\u0001\u0000\u0001\u0000\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001"+
		"\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0002\u0001\u0002\u0001\u0002"+
		"\u0001\u0002\u0001\u0002\u0001\u0003\u0001\u0003\u0001\u0003\u0001\u0003"+
		"\u0001\u0003\u0001\u0003\u0001\u0003\u0001\u0004\u0001\u0004\u0001\u0004"+
		"\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0005\u0001\u0005"+
		"\u0001\u0006\u0001\u0006\u0001\u0007\u0001\u0007\u0005\u0007A\b\u0007"+
		"\n\u0007\f\u0007D\t\u0007\u0001\b\u0004\bG\b\b\u000b\b\f\bH\u0001\t\u0004"+
		"\tL\b\t\u000b\t\f\tM\u0001\t\u0001\t\u0004\tR\b\t\u000b\t\f\tS\u0001\t"+
		"\u0001\t\u0004\tX\b\t\u000b\t\f\tY\u0001\t\u0001\t\u0004\t^\b\t\u000b"+
		"\t\f\t_\u0001\t\u0001\t\u0004\td\b\t\u000b\t\f\te\u0001\n\u0004\ni\b\n"+
		"\u000b\n\f\nj\u0001\n\u0001\n\u0000\u0000\u000b\u0001\u0001\u0003\u0002"+
		"\u0005\u0003\u0007\u0004\t\u0005\u000b\u0006\r\u0007\u000f\b\u0011\t\u0013"+
		"\n\u0015\u000b\u0001\u0000\u0005\u0003\u0000AZ__az\u0005\u0000--09AZ_"+
		"_az\u0004\u000009AZ__az\u0001\u000009\u0003\u0000\t\n\r\r  u\u0000\u0001"+
		"\u0001\u0000\u0000\u0000\u0000\u0003\u0001\u0000\u0000\u0000\u0000\u0005"+
		"\u0001\u0000\u0000\u0000\u0000\u0007\u0001\u0000\u0000\u0000\u0000\t\u0001"+
		"\u0000\u0000\u0000\u0000\u000b\u0001\u0000\u0000\u0000\u0000\r\u0001\u0000"+
		"\u0000\u0000\u0000\u000f\u0001\u0000\u0000\u0000\u0000\u0011\u0001\u0000"+
		"\u0000\u0000\u0000\u0013\u0001\u0000\u0000\u0000\u0000\u0015\u0001\u0000"+
		"\u0000\u0000\u0001\u0017\u0001\u0000\u0000\u0000\u0003 \u0001\u0000\u0000"+
		"\u0000\u0005\'\u0001\u0000\u0000\u0000\u0007,\u0001\u0000\u0000\u0000"+
		"\t3\u0001\u0000\u0000\u0000\u000b:\u0001\u0000\u0000\u0000\r<\u0001\u0000"+
		"\u0000\u0000\u000f>\u0001\u0000\u0000\u0000\u0011F\u0001\u0000\u0000\u0000"+
		"\u0013K\u0001\u0000\u0000\u0000\u0015h\u0001\u0000\u0000\u0000\u0017\u0018"+
		"\u0005n\u0000\u0000\u0018\u0019\u0005e\u0000\u0000\u0019\u001a\u0005t"+
		"\u0000\u0000\u001a\u001b\u0005w\u0000\u0000\u001b\u001c\u0005o\u0000\u0000"+
		"\u001c\u001d\u0005r\u0000\u0000\u001d\u001e\u0005k\u0000\u0000\u001e\u001f"+
		"\u0005s\u0000\u0000\u001f\u0002\u0001\u0000\u0000\u0000 !\u0005d\u0000"+
		"\u0000!\"\u0005r\u0000\u0000\"#\u0005i\u0000\u0000#$\u0005v\u0000\u0000"+
		"$%\u0005e\u0000\u0000%&\u0005r\u0000\u0000&\u0004\u0001\u0000\u0000\u0000"+
		"\'(\u0005i\u0000\u0000()\u0005p\u0000\u0000)*\u0005a\u0000\u0000*+\u0005"+
		"m\u0000\u0000+\u0006\u0001\u0000\u0000\u0000,-\u0005c\u0000\u0000-.\u0005"+
		"o\u0000\u0000./\u0005n\u0000\u0000/0\u0005f\u0000\u000001\u0005i\u0000"+
		"\u000012\u0005g\u0000\u00002\b\u0001\u0000\u0000\u000034\u0005s\u0000"+
		"\u000045\u0005u\u0000\u000056\u0005b\u0000\u000067\u0005n\u0000\u0000"+
		"78\u0005e\u0000\u000089\u0005t\u0000\u00009\n\u0001\u0000\u0000\u0000"+
		":;\u0005:\u0000\u0000;\f\u0001\u0000\u0000\u0000<=\u0005-\u0000\u0000"+
		"=\u000e\u0001\u0000\u0000\u0000>B\u0007\u0000\u0000\u0000?A\u0007\u0001"+
		"\u0000\u0000@?\u0001\u0000\u0000\u0000AD\u0001\u0000\u0000\u0000B@\u0001"+
		"\u0000\u0000\u0000BC\u0001\u0000\u0000\u0000C\u0010\u0001\u0000\u0000"+
		"\u0000DB\u0001\u0000\u0000\u0000EG\u0007\u0002\u0000\u0000FE\u0001\u0000"+
		"\u0000\u0000GH\u0001\u0000\u0000\u0000HF\u0001\u0000\u0000\u0000HI\u0001"+
		"\u0000\u0000\u0000I\u0012\u0001\u0000\u0000\u0000JL\u0007\u0003\u0000"+
		"\u0000KJ\u0001\u0000\u0000\u0000LM\u0001\u0000\u0000\u0000MK\u0001\u0000"+
		"\u0000\u0000MN\u0001\u0000\u0000\u0000NO\u0001\u0000\u0000\u0000OQ\u0005"+
		".\u0000\u0000PR\u0007\u0003\u0000\u0000QP\u0001\u0000\u0000\u0000RS\u0001"+
		"\u0000\u0000\u0000SQ\u0001\u0000\u0000\u0000ST\u0001\u0000\u0000\u0000"+
		"TU\u0001\u0000\u0000\u0000UW\u0005.\u0000\u0000VX\u0007\u0003\u0000\u0000"+
		"WV\u0001\u0000\u0000\u0000XY\u0001\u0000\u0000\u0000YW\u0001\u0000\u0000"+
		"\u0000YZ\u0001\u0000\u0000\u0000Z[\u0001\u0000\u0000\u0000[]\u0005.\u0000"+
		"\u0000\\^\u0007\u0003\u0000\u0000]\\\u0001\u0000\u0000\u0000^_\u0001\u0000"+
		"\u0000\u0000_]\u0001\u0000\u0000\u0000_`\u0001\u0000\u0000\u0000`a\u0001"+
		"\u0000\u0000\u0000ac\u0005/\u0000\u0000bd\u0007\u0003\u0000\u0000cb\u0001"+
		"\u0000\u0000\u0000de\u0001\u0000\u0000\u0000ec\u0001\u0000\u0000\u0000"+
		"ef\u0001\u0000\u0000\u0000f\u0014\u0001\u0000\u0000\u0000gi\u0007\u0004"+
		"\u0000\u0000hg\u0001\u0000\u0000\u0000ij\u0001\u0000\u0000\u0000jh\u0001"+
		"\u0000\u0000\u0000jk\u0001\u0000\u0000\u0000kl\u0001\u0000\u0000\u0000"+
		"lm\u0006\n\u0000\u0000m\u0016\u0001\u0000\u0000\u0000\t\u0000BHMSY_ej"+
		"\u0001\u0006\u0000\u0000";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}
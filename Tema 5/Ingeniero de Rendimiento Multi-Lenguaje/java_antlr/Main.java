import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.tree.*;
import java.io.File;
import java.nio.file.Files;
import java.util.*;

public class Main {
    public static void main(String[] args) throws Exception {
        String datasetDir = args[0];
        int repeats = args.length > 1 ? Integer.parseInt(args[1]) : 50;

        File[] files = new File(datasetDir).listFiles((d, name) -> name.endsWith(".yml"));
        Arrays.sort(files, Comparator.comparing(File::getName));

        System.out.println("file,lang,run,time_ms,ok");

        for (File f : files) {
            String content = new String(Files.readAllBytes(f.toPath()));
            for (int r = 0; r < repeats; r++) {
                long start = System.nanoTime();
                boolean ok = true;
                try {
                    CharStream input = CharStreams.fromString(content);
                    DockerNetworksLexer lexer = new DockerNetworksLexer(input);
                    CommonTokenStream tokens = new CommonTokenStream(lexer);
                    DockerNetworksParser parser = new DockerNetworksParser(tokens);
                    parser.removeErrorListeners();
                    parser.addErrorListener(new BaseErrorListener() {
                        @Override
                        public void syntaxError(Recognizer<?, ?> recognizer, Object offendingSymbol,
                                                 int line, int charPositionInLine, String msg, RecognitionException e) {
                            throw new RuntimeException("Syntax error: " + msg);
                        }
                    });
                    ParseTree tree = parser.composeFile();
                } catch (Exception e) {
                    ok = false;
                }
                long end = System.nanoTime();
                double ms = (end - start) / 1_000_000.0;
                System.out.println(f.getName() + ",java_antlr," + r + "," + ms + "," + ok);
            }
        }
    }
}

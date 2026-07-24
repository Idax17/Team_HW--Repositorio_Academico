import sys
import os
import time

sys.path.insert(0, os.path.dirname(__file__))
from antlr4 import InputStream, CommonTokenStream
from antlr4.error.ErrorListener import ErrorListener
from DockerNetworksLexer import DockerNetworksLexer
from DockerNetworksParser import DockerNetworksParser


class RaisingErrorListener(ErrorListener):
    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        raise RuntimeError(msg)


def parse_once(content):
    ok = True
    try:
        input_stream = InputStream(content)
        lexer = DockerNetworksLexer(input_stream)
        stream = CommonTokenStream(lexer)
        parser = DockerNetworksParser(stream)
        parser.removeErrorListeners()
        parser.addErrorListener(RaisingErrorListener())
        parser.composeFile()
    except Exception:
        ok = False
    return ok


def main():
    dataset_dir = sys.argv[1]
    repeats = int(sys.argv[2]) if len(sys.argv) > 2 else 50

    files = sorted(f for f in os.listdir(dataset_dir) if f.endswith(".yml"))

    print("file,lang,run,time_ms,ok")
    for fname in files:
        with open(os.path.join(dataset_dir, fname)) as fh:
            content = fh.read()
        for r in range(repeats):
            start = time.perf_counter()
            ok = parse_once(content)
            end = time.perf_counter()
            ms = (end - start) * 1000.0
            print(f"{fname},python_antlr,{r},{ms},{ok}")


if __name__ == "__main__":
    main()

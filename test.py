import os
import pytest
from src.type_checker.node_visitor import TypeChecker
from src.interpreter.interpreter import Interpreter
from pathlib import Path


def check_parser(parser, scanner, text):
    try:
        ast = parser.parse(text, lexer=scanner.lexer)
        # ast.print_tree()

        type_checker = TypeChecker()
        type_checker.visit(ast)

        if type_checker.correct:
            interpreter = Interpreter()
            interpreter.visit(ast)

    except SyntaxError as error:
        print(error.msg)


def test_parser(files):
    from src.parser import parser as parser_module
    from src.scanner import scanner

    parser = parser_module.parser
    work_dir = str(Path(__file__).parent)
    if len(files) == 0:
        work_dir += "\\examples"
        files = os.listdir(work_dir)

    for filename in files:
        print(filename)
        filename = os.path.join(work_dir, filename)

        file = open(filename, "r")
        text = file.read()

        if "error" in filename:
            with pytest.raises(AssertionError):
                check_parser(parser, scanner, text)
                raise AssertionError
        else:
            check_parser(parser, scanner, text)

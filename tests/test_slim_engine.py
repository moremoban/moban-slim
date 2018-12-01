import os

from nose.tools import eq_
from moban.plugins import ENGINES, BaseEngine
from moban_slim.engine import EngineSlim


def test_slim_engine_type():
    engine = ENGINES.get_engine("slim", [], "")
    assert engine.engine_cls == EngineSlim
    pass


def test_slim_file_tests():
    output = "test.txt"
    path = os.path.join("tests", "fixtures", "slim_tests")
    engine = BaseEngine([path], path, EngineSlim)
    engine.render_to_file("file_tests.slim", "file_tests.json", output)
    with open(output, "r") as output_file:
        expected_path = os.path.join("tests", "fixtures", "slim_tests",
            "expected_output.txt")
        with open(expected_path) as expected_file:
            expected = expected_file.read()
            content = output_file.read()
            eq_(content, expected)
    os.unlink(output)
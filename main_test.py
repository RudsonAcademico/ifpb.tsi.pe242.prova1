import mock
import builtins
import main


def test_q01(capfd):
    input_outputexpected = {
        '121':'True\n',
        '-121':'False\n',
        '10':'False\n',
        '010101010':'True\n',
        '01':'False\n',
        '1':'True\n',
        '-1':'False\n',
    }
    for _input, _outputexpected in input_outputexpected.items():
        with mock.patch.object(builtins, 'input', lambda _: _input):
            main.q1()
            output, _ = capfd.readouterr()
            assert output == _outputexpected

def test_q02a(capfd):
    input_outputexpected = {
        'III':'3\n',
        'LVIII':'58\n',
        'DCXXI': '621\n',
        'MMM': '3000\n',
        'LXX': '70\n',
        'XVI': '16\n',
    }
    for _input, _outputexpected in input_outputexpected.items():
        with mock.patch.object(builtins, 'input', lambda _: _input):
            main.q2()
            output, _ = capfd.readouterr()
            assert output == _outputexpected

def test_q02b(capfd):
    input_outputexpected = {
        'MCMXCIV':'1994\n',
        'XCIX':'99\n',
        'XIX':'19\n',
        'XLIV': '44\n',
    }
    for _input, _outputexpected in input_outputexpected.items():
        with mock.patch.object(builtins, 'input', lambda _: _input):
            main.q2()
            output, _ = capfd.readouterr()
            assert output == _outputexpected

def test_q03(capfd):
    input_output = {
        '7': 'O número não possui divisores multiplos de 3\n',
        '3': 'Quantidade de divisores divisiveis por 3: 1\n',
        '555':'Quantidade de divisores divisiveis por 3: 4\n',
        '3144':'Quantidade de divisores divisiveis por 3: 8\n',
        '17640':'Quantidade de divisores divisiveis por 3: 48\n'
    }
    for k, v in input_output.items():
        with mock.patch.object(builtins, 'input', lambda _: k):
            main.q3()
            out, err = capfd.readouterr()
            assert out == v

def make_multiple_inputs(inputs):
    """ provides a function to call for every input requested. """
    def next_input(_):
        """ provides the first item in the list. """
        return inputs.pop()
    return next_input

def test_q04(capfd, monkeypatch):
    input_output = {
        '1,3': '6\n',
        '-2,2': '3\n',
        '10,-10': '55\n',
    }
    for k,v in input_output.items():
        monkeypatch.setitem(__builtins__, 'input', make_multiple_inputs(k.split(',')))
        main.q4()
        out, _ = capfd.readouterr()
        assert out == v
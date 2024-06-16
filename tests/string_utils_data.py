char_and_ascii_number_pairs_data = [
    ('test', [('t', 116), ('e', 101), ('s', 115), ('t', 116)]),
    ('', []),
    (' ', [(' ', 32)]),
    ('1', [('1', 49)]),
    ('1.0', [('1', 49), ('.', 46), ('0', 48)]),
    ('1.0 ', [('1', 49), ('.', 46), ('0', 48), (' ', 32)]),
    ('1.0 \na', [('1', 49), ('.', 46), ('0', 48), (' ', 32), ('\n', 10), ('a', 97)]),
    ('1.0 d\n', [('1', 49), ('.', 46), ('0', 48), (' ', 32), ('d', 100), ('\n', 10)])
]


emails_data = [
    ('test e1@test.com test ffff ssss e1@test.com test232323\n'
     'test@test.com e2@test.com\te3@test.com\n\n',
     ['e1@test.com', 'test@test.com', 'e2@test.com', 'e3@test.com'])
]

urls_data = [
    ('http://www.test.com wwwwwwwww ffffffffff\n\n\n'
     ' https://www.test.com http://test.com http://test.com https://test.com\n'
     'http://www.test.com/test http://test.com/test https://test.com/test\n\n',
     [
        'http://www.test.com',
        'https://www.test.com',
        'http://test.com',
        'https://test.com',
        'http://www.test.com/test',
        'http://test.com/test',
        'https://test.com/test'
     ])
]

json_data = [
    ('{"test": "test"}', True),
    ('{"test": "test"', False),
    ('{"test": "test"} ', True),
    ('{}', True),
    ('', False),
    ('{', False),
    ('}', False),
    ('{test}', False),
    ('{test:}', False),
    ('{test: "test"}', False)
]

sub_string_data = [
    ('(test)', '(', ')', 'test'),
    ('(test)', '(', None, 'test)'),
    ('(test', '(', ')', ''),
    ('test)', '(', ')', ''),
    ('test', '(', ')', ''),
    ('(test) test', '(', ')', 'test'),
    ('(test) test (test)', '(', ')', 'test'),
    ('(test) test (test', '(', ')', 'test'),
    ('(test) test test)', ' ', ')', 'test test'),
    ('(test) test test', ') ', ')', '')
]

sub_string_list_data = [
    ('(test)', '(', ')', ['test']),
    ('(test', '(', ')', []),
    ('test)', '(', ')', []),
    ('test', '(', ')', []),
    ('(test) test', '(', ')', ['test']),
    ('(test) test (test)', '(', ')', ['test', 'test']),
    ('(test) test (test', '(', ')', ['test'])
]

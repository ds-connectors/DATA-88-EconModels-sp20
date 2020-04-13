test = {   'name': 'q1_6',
    'points': 1,
    'suites': [   {   'cases': [   {   'code': '>>> results = run_tournament(make_array(Defector(), Cooperator()));\n'
                                               '>>> assert results.num_rows == 1;\n'
                                               '>>> assert results.num_columns == 4;\n'
                                               '>>> assert results.column("p1")[0] == Defector();\n'
                                               '>>> assert results.column("p2")[0] == Cooperator();\n'
                                               '>>> assert results.column("p1_mean")[0] == 0;\n'
                                               '>>> assert results.column("p2_mean")[0] == 5\n',
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}

test = {   'name': 'q2_5',
    'points': 1,
    'suites': [   {   'cases': [   {   'code': '>>> t = Table().with_columns("Estimate", np.arange(5), "TrueHeight", np.arange(5, 10));\n'
                                               '>>> t = add_error_ratio(t);\n'
                                               '>>> np.allclose(t["ErrorRatio"], np.array([-1., -0.83333333, -0.71428571, -0.625, -0.55555556]))\n'
                                               'True',
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}

test = {   'name': 'q1_7',
    'points': 1,
    'suites': [   {   'cases': [   {'code': '>>> tournmanet_results.num_rows == 45\nTrue', 'hidden': False, 'locked': False},
                                   {'code': '>>> tournmanet_results.num_columns == 4\nTrue', 'hidden': False, 'locked': False},
                                   {   'code': '>>> players = make_array(Alternator(), Backstabber(), Bully(), Desperate(), FoolMeOnce(), Forgiver(), \n'
                                               '...                      OnceBitten(), TitForTat(), WorseAndWorse(), ForgivingTitForTat());\n'
                                               '>>> for player in players:\n'
                                               '...     assert player in tournmanet_results.column("p1") or player in tournmanet_results.column("p2")\n',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': '>>> t = tournmanet_results.where("p1", Alternator()).where("p2", Bully());\n'
                                               '>>> assert np.isclose(t["p1_mean"][0], 3.015);\n'
                                               '>>> assert np.isclose(t["p2_mean"][0], 2.99)\n',
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}

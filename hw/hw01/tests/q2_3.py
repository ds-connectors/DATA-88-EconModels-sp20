test = {
	"name": "q2_3",
	"points": 0,
	"suites": [ 
		{
			"cases": [ 
				{
					"code": r"""
					>>> len(coeffs) == 2
					True
					""",
					"hidden": False,
					"locked": False,
				}, 
				{
					"code": r"""
					>>> 100 <= coeffs[1] <= 1000
					True
					""",
					"hidden": False,
					"locked": False,
				}, 
				{
					"code": r"""
					>>> -1 <= coeffs[0] <= 1
					True
					""",
					"hidden": False,
					"locked": False,
				}, 
			],
			"scored": False,
			"setup": "",
			"teardown": "",
			"type": "doctest"
		}, 
	]
}
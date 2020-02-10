test = {
	"name": "q1_10",
	"points": 0,
	"hidden": False,
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
					>>> -2 <= coeffs[0] <= 0
					True
					""",
					"hidden": False,
					"locked": False,
				}, 
				{
					"code": r"""
					>>> 0 <= coeffs[1] <= 0.2
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
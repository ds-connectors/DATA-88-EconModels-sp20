test = {
	"name": "q3_5",
	"points": 0,
	"suites": [ 
		{
			"cases": [ 
				{
					"code": r"""
					>>> -1 <= lowprice_coeffs[0] <= 1
					True
					""",
					"hidden": False,
					"locked": False,
				}, 
				{
					"code": r"""
					>>> len(lowprice_coeffs) == 2
					True
					""",
					"hidden": False,
					"locked": False,
				}, 
				{
					"code": r"""
					>>> 100 <= lowprice_coeffs[1] <= 200
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
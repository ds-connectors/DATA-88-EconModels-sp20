test = {
	"name": "q2_1",
	"points": 1,
	"suites": [ 
		{
			"cases": [ 
				{
					"code": r"""
					>>> "Average Weekly Passengers" in nondelta.labels
					False
					""",
					"hidden": False,
					"locked": False,
				}, 
				{
					"code": r"""
					>>> "Average Price" in nondelta.labels
					False
					""",
					"hidden": False,
					"locked": False,
				}, 
				{
					"code": r"""
					>>> "Quantity" in nondelta.labels
					True
					""",
					"hidden": False,
					"locked": False,
				}, 
				{
					"code": r"""
					>>> "Price" in nondelta.labels
					True
					""",
					"hidden": False,
					"locked": False,
				}, 
				{
					"code": r"""
					>>> len(nondelta.labels)
					11
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
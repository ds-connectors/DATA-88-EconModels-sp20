test = {
	"name": "q3_1",
	"points": 1,
	"suites": [ 
		{
			"cases": [ 
				{
					"code": r"""
					>>> lowprice.num_columns == 4
					True
					""",
					"hidden": False,
					"locked": False,
				}, 
				{
					"code": r"""
					>>> for l in ["Average Weekly Passengers", "Low Price Airline", "Market Share Low Price", "Low Price Airline Ticket Cost"]:
					... 	assert l in lowprice.labels, ""
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
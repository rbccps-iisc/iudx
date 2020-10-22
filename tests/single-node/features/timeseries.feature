Feature: Vermillion is able to handle timeseries data


    	Scenario: Geo-spactial query with wrong id
		Given Vermillion is running
		When The payload is empty
		Then Return the status as Bad request 400
			
	Scenario: Geo-spatial query
		Given Vermillion is running
		When A geo-spatial query is initiated
		Then All matching records are returned

	Scenario: Timeseries query
		Given Vermillion is running
		When A timeseries query is initiated
		Then All matching records are returned

	Scenario: Attribute term query
		Given Vermillion is running
		When An attribute term query is initiated
		Then All matching records are returned

	Scenario: Attribute value query
		Given Vermillion is running
		When An attribute value query is initiated
		Then All matching records are returned

	Scenario: Complex query
		Given Vermillion is running
		When A complex query is initiated
		Then All matching records are returned

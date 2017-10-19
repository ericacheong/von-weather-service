

# Get current temperatuure of <city> in celsius

    * URL: /api/v1.0/<city>/temp  
    * HTTP method: GET

## Example Response

    {
        "city": "paris",
        "temperature": 15,
    }


# Get current humidity of <city> in percentage

    * URL: /api/v1.0/<city>/humidity
    * HTTP method: GET

## Example Response

    {
        "city": "paris",
        "humidity": 82
    }


# Get current wind speed of <city> in kmh

    * URL: /api/v1.0/<city>/wind
    * HTTP method: GET

## Example Response

    {
        "city": paris,
        "wind": 10
    }


# Get current weather "status" of <city>

    * URL: /api/v1.0/<city>/status
    * HTTP method: GET

## Example Response

    {
        "city": "paris",
        "status": "Partly cloudy"
    }


# Get current atmospheric pressure of <city> in mb

    * URL: /api/v1.0/<city>/atmospres
    * HTTP method: GET

## Example Response

    {
        "city": "paris",
        "atmospheric pressure": 1009
    }

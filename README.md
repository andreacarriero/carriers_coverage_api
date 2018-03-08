# Operators Connectivity Coverage API
Get per-operator mobile connectivity details at city-level.

The connectivity types (2G, 3G, 4G) will result as "present" if them are present at least in one location in the same city.

### How to populate carriers table
- `python manage.py shell`
- `from data_processing import populate_carriers`
- `populate_carriers.parse_and_populate()`

### How to populate carriers connectivity table
- `python manage.py shell`
- `from data_processing import populate_carriers_connectivity`
- `populate_carriers_connectivity.parse_and_populate()`

### How to run the application
- Create a configuration file or rename the example one `mv data/example_configuration.json configuration.json`
- Populate carriers table (see above)
- Populate carriers connectivity table (see above)
- Run the dev server `python manage.py runserver`

### Examples
Get connectivity at city-level for main operators.

To change the "main operators" list edit `data/configuration.json`.
```
"carriersToShow": [
    "Orange",
    "SFR"
]
```

```
http GET "http://localhost:5000/?q=quai lamartine rennes"
HTTP/1.0 200 OK
Content-Length: 461
Content-Type: application/json
Date: Wed, 07 Mar 2018 23:05:28 GMT
Server: Werkzeug/0.14.1 Python/3.6.0b3

{
    "Orange": {
        "2G": true,
        "3G": true,
        "4G": true
    },
    "SFR": {
        "2G": true,
        "3G": true,
        "4G": true
    },
    "meta": {
        "location": {
            "city": "Rennes",
            "context": "35, Ille-et-Vilaine, Bretagne",
            "coordinates": {
                "x": -1.678835,
                "y": 48.110144
            },
            "label": "Quai Lamartine 35000 Rennes"
        }
    }
}
```


Get connectivity at city-level for all operators
```
http GET "http://localhost:5000/?q=quai lamartine rennes&all=1"
HTTP/1.0 200 OK
Content-Length: 2815
Content-Type: application/json
Date: Wed, 07 Mar 2018 23:08:10 GMT
Server: Werkzeug/0.14.1 Python/3.6.0b3

{
    "Air France": {
        "2G": false,
        "3G": false,
        "4G": false
    },
    "Altitude": {
        "2G": false,
        "3G": false,
        "4G": false
    },
    "Association Images & Réseaux": {
        "2G": false,
        "3G": false,
        "4G": false
    },
    "Association Plate-forme Telecom[9]": {
        "2G": false,
        "3G": false,
        "4G": false
    },
    "Astrium SAS": {
        "2G": false,
        "3G": false,
        "4G": false
    },
    "Axione[11]": {
        "2G": false,
        "3G": false,
        "4G": false
    },
    "Bouygues": {
        "2G": false,
        "3G": false,
        "4G": false
    },
    "Bouygues Telecom": {
        "2G": true,
        "3G": true,
        "4G": true
    },
    "Completel": {
        "2G": false,
        "3G": false,
        "4G": false
    },
    "Coriolis": {
        "2G": false,
        "3G": false,
        "4G": false
    },
    "Free": {
        "2G": false,
        "3G": true,
        "4G": true
    },
    "Globalstar": {
        "2G": false,
        "3G": false,
        "4G": false
    },
    "Halys[10]": {
        "2G": false,
        "3G": false,
        "4G": false
    },
    "IMC": {
        "2G": false,
        "3G": false,
        "4G": false
    },
    "Legos": {
        "2G": false,
        "3G": false,
        "4G": false
    },
    "Lycamobile": {
        "2G": false,
        "3G": false,
        "4G": false
    },
    "MobiquiThings": {
        "2G": false,
        "3G": false,
        "4G": false
    },
    "NRJ Mobile": {
        "2G": false,
        "3G": false,
        "4G": false
    },
    "Orange": {
        "2G": true,
        "3G": true,
        "4G": true
    },
    "RFF": {
        "2G": false,
        "3G": false,
        "4G": false
    },
    "SFR": {
        "2G": true,
        "3G": true,
        "4G": true
    },
    "Sisteer": {
        "2G": false,
        "3G": false,
        "4G": false
    },
    "Syma Mobile": {
        "2G": false,
        "3G": false,
        "4G": false
    },
    "Thales": {
        "2G": false,
        "3G": false,
        "4G": false
    },
    "Transatel Mobile": {
        "2G": false,
        "3G": false,
        "4G": false
    },
    "Vectone / Delight Mobile (MVNO)": {
        "2G": false,
        "3G": false,
        "4G": false
    },
    "Virgin Mobile": {
        "2G": false,
        "3G": false,
        "4G": false
    },
    "Voxbone": {
        "2G": false,
        "3G": false,
        "4G": false
    },
    "meta": {
        "location": {
            "city": "Rennes",
            "context": "35, Ille-et-Vilaine, Bretagne",
            "coordinates": {
                "x": -1.678835,
                "y": 48.110144
            },
            "label": "Quai Lamartine 35000 Rennes"
        }
    }
}
```

# Operators Connectivity Coverage API

### How to populate carriers table
`python manage.py shell`
`from data_processing import populate_carriers`
`populate_carriers.parse_and_populate()`


### How to populate carriers connectivity table
`python manage.py shell`
`from data_processing import populate_carriers_connectivity`
`populate_carriers_connectivity.parse_and_populate()`

### How to run the application
- Create a configuration file or rename the example one `mv data/example_configuration.json configuration.json`
- Populate carriers table (see above)
- Populate carriers connectivity table (see above)
- Run the dev server `python manage.py runserver`

### Examples
Get connectivity at city-level for main operators
```
http GET "http://localhost:5000/?q=tour eiffel"
HTTP/1.0 200 OK
Content-Length: 488
Content-Type: application/json
Date: Wed, 07 Mar 2018 22:59:51 GMT
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
            "city": "Paris",
            "context": "75, Paris, Île-de-France",
            "coordinates": {
                "x": 2.289644,
                "y": 48.856888
            },
            "label": "Port de Suffren, CHAMP DE MARS - TOUR EIFFEL 75015 Paris"
        }
    }
}
```


Get connectivity at city-level for all operators
```
http GET "http://localhost:5000/?q=tour eiffel&all=1"
HTTP/1.0 200 OK
Content-Length: 2842
Content-Type: application/json
Date: Wed, 07 Mar 2018 23:02:00 GMT
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
            "city": "Paris",
            "context": "75, Paris, Île-de-France",
            "coordinates": {
                "x": 2.289644,
                "y": 48.856888
            },
            "label": "Port de Suffren, CHAMP DE MARS - TOUR EIFFEL 75015 Paris"
        }
    }
}
```
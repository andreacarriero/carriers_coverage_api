### How to populate carriers table
`python manage.py shell`
`from data_processing import populate_carriers`
`populate_carriers.parse_and_populate()`


### How to populate carriers connectivity table
`python manage.py shell`
`from data_processing import populate_carriers_connectivity`
`populate_carriers_connectivity.parse_and_populate()`
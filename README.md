### How to populate carriers table
`python manage.py shell`
`from data_processing import populate_carriers`
`populate_carriers.parse_and_populate()`
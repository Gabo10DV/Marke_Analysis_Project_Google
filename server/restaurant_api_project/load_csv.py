from .models import Place # Asegúrate de ajustar la ruta al modelo Place
import csv

# Ruta al archivo CSV
csv_file_path_1 = '/home/mkm/programin/Marke_Analysis_Project_Google/Data/Data_process/restaurants.csv'
csv_file_path_2 = '/home/mkm/programin/Marke_Analysis_Project_Google/Data/Data_process/reviews.csv'
csv_file_path_3 = '/home/mkm/programin/Marke_Analysis_Project_Google/Data/Data_process/users.csv'

Data/Data_process/restaurants.csv
Data/Data_process/reviews.csv
Data/Data_process/users.csv

BATCH_SIZE = 100

with open(csv_file_path, 'r') as file:
    csv_reader = csv.DictReader(file)
    places_to_create = []

    for row in csv_reader:
        # Verifica si ya existe un lugar con el mismo nombre en la base de datos
        existing_place = Place.objects.filter(name=row['name']).first()

        if not existing_place:
            place = Place(
                name=row['name'],
                latitude=row['latitude'],
                longitude=row['longitude'],
                category=row['category'],
                avg_rating=row['avg_rating'],
                num_of_reviews=row['num_of_reviews']
            )
            places_to_create.append(place)

            if len(places_to_create) == BATCH_SIZE:
                Place.objects.bulk_create(places_to_create)
                places_to_create = []

    # Inserta cualquier remanente que quede en el último lote
    if places_to_create:
        Place.objects.bulk_create(places_to_create)
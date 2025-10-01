'''
keys: model,make,colour,year,fuel_type 

list_of_cars = [
{
model: 'civic',
make: 'honda',
colour: 'blue',
year: 2012,
fuel_type: 'petrol'
}, 
{
model: 'corolla',
make: 'toyota',
colour: 'white',
year: 2020,
fuel_type: 'petrol'
}
]
'''

with open('data/cars.csv') as file:
    records = file.readlines()

    
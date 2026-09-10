from vehicle import Vehicle

def test_vehicle_stores_year():
    vehicle = Vehicle(1967, 'Ford','Mustang', 'CLASSICVIN67',  'CLASSIC67')
    assert vehicle.year == 1967
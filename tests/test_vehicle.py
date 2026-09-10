from vehicle import Vehicle

def test_vehicle_stores_year():
    vehicle = Vehicle(1967, 'Ford','Mustang', 'CLASSICVIN67',  'CLASSIC67')
    assert vehicle.year == 1967

def test_vehicle_displays_summary(capsys):
    vehicle = Vehicle(2027, 'Lamborghini', 'Urus', 'HUMBLEURUS27', 'URUS27')
    vehicle.display_summary()
    captured = capsys.readouterr()

    assert 'Year: 2027' in captured.out

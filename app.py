from core import Guitar, GuitarType

electric_guitar = GuitarType(name="Electric")
ibanez = Guitar(name="Ibanez RG", guitar_type=electric_guitar, number_of_strings=6)

if not ibanez.is_deleted:
    print(ibanez)
    print(ibanez.created_at)
    print(ibanez.updated_at)
    print(ibanez.guitar_type.name)

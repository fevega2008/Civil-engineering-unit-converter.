"""A simple unit converter for common engineering length measurements."""

UNITS_TO_METERS = {
    "mm": 0.001,
    "cm": 0.01,
    "m": 1.0,
    "km": 1000.0,
    "in": 0.0254,
    "ft": 0.3048,
    "yd": 0.9144,
    "mi": 1609.344,
}

UNIT_ALIASES = {
    "millimeter": "mm",
    "millimeters": "mm",
    "centimeter": "cm",
    "centimeters": "cm",
    "meter": "m",
    "meters": "m",
    "kilometer": "km",
    "kilometers": "km",
    "inch": "in",
    "inches": "in",
    "foot": "ft",
    "feet": "ft",
    "yard": "yd",
    "yards": "yd",
    "mile": "mi",
    "miles": "mi",
}


def normalize_unit(unit):
    """Convert a unit name or abbreviation to its standard abbreviation."""
    unit = unit.strip().lower()
    return UNIT_ALIASES.get(unit, unit)


def convert_length(value, from_unit, to_unit):
    """Convert a length measurement between supported units."""
    from_unit = normalize_unit(from_unit)
    to_unit = normalize_unit(to_unit)

    if from_unit not in UNITS_TO_METERS:
        raise ValueError(f"Unsupported starting unit: {from_unit}")

    if to_unit not in UNITS_TO_METERS:
        raise ValueError(f"Unsupported target unit: {to_unit}")

    # Convert the original value to meters, then to the target unit.
    value_in_meters = value * UNITS_TO_METERS[from_unit]
    return value_in_meters / UNITS_TO_METERS[to_unit]


def main():
    print("Civil Engineering Length Unit Converter")
    print("Supported units: mm, cm, m, km, in, ft, yd, mi")

    try:
        value = float(input("Enter the measurement: "))
        from_unit = input("Convert from: ")
        to_unit = input("Convert to: ")

        result = convert_length(value, from_unit, to_unit)

        print(f"\nResult: {value:g} {normalize_unit(from_unit)} "
              f"= {result:.6g} {normalize_unit(to_unit)}")

    except ValueError as error:
        print(f"\nError: {error}")
        print("Please enter a valid number and supported units.")


if __name__ == "__main__":
    main()

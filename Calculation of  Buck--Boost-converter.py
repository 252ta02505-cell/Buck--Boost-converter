# buck_boost_converter.py

Vin = float(input("Enter input voltage (V): "))
D = float(input("Enter duty cycle (0 to 1): "))

if not 0 < D < 1:
    print("Duty cycle must be between 0 and 1.")
else:
    # Ideal inverting buck-boost converter
    Vout = -(D / (1 - D)) * Vin

    print(f"Input Voltage  : {Vin:.2f} V")
    print(f"Duty Cycle     : {D:.2f}")
    print(f"Output Voltage : {Vout:.2f} V")

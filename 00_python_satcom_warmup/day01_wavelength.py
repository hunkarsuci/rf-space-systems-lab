# Day 1 - Wavelength Calculation for SatCom Bands

speed_of_light_m_per_s = 299_792_458

frequencies_hz = {
    "S-band": 2.2e9,
    "X-band": 8.4e9,
    "Ku-band": 12.0e9,
    "Ka-band": 26.5e9,
}

print("SatCom Band Wavelengths")
print("-----------------------")

for band_name, frequency_hz in frequencies_hz.items():
    wavelength_m = speed_of_light_m_per_s / frequency_hz
    wavelength_cm = wavelength_m * 100

    print(f"{band_name}:")
    print(f"  Frequency: {frequency_hz / 1e9:.2f} GHz")
    print(f"  Wavelength: {wavelength_m:.4f} m")
    print(f"  Wavelength: {wavelength_cm:.2f} cm")
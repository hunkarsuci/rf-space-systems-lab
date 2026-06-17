# Day 2 - Free Space Path Loss
# Satellite Communication Systems Software Lab

import math

speed_of_light_m_per_s = 299_792_458

def calculate_wavelength(frequency_hz):
    wavelength_m = speed_of_light_m_per_s / frequency_hz
    return wavelength_m

def calculate_fspl(range_m, frequency_hz):
    wavelength_m = calculate_wavelength(frequency_hz)
    fspl_db = 20 * math.log10((4 * math.pi * range_m) / wavelength_m)
    return fspl_db

# Example values 
frequency_hz = 2.2e9 # 2.2 GHz, S-band
range_m = 1_000_000 # 1000km
range_km = [500, 1000, 2000, 35786] # list 

wavelength_m = calculate_wavelength(frequency_hz)
fspl_db = calculate_fspl(range_m, frequency_hz)

print('Free-Space path Loss Calculator')
print('-------------------------------')

for range in range_km:
    fspl_db = calculate_fspl(range, frequency_hz)
    print(f'Range: {range:8.0f} km | FSPL: {fspl_db:8.2f} dB')
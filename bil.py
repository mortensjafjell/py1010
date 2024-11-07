"""
Tall brukt i programmet:
Forsikring: Elbil: 5000 kr/år. Bensinbil: 7500 kr/år.
Trafikkforsikringsavgift: 8,38 kr/dag for både elbil og bensinbil.
Drivstoffbruk: Elbil: 0,2 kWh/km. Strømpris (antar kun hjemmelading): 2.00 kr/kWh. Bensinbil: 1,0 kr/km.
Bomavgift: Elbil: 0,1 kr/km. Bensinbil: 0,3 kr/km.
"""

km = 10000  # Antall årlige kilometer, felles for begge biltyper
trafikk_avg = 8.38*365 # Trafikkavgift, felles for begge biltyper

# Kostnader for Elbil
elbil_forsikring = 5000
elbil_drivstoff = (km*0.2) * 2 # Elbil bruker 0,2KWh/km, med en kostnad på 2.00 kr/kWh
elbil_bomavgift = 0.1*km # Bomavgift for elbil koster 0,1 kr/km

total_elbil = elbil_forsikring + trafikk_avg + elbil_drivstoff + elbil_bomavgift

# Kostnader for bensinbil
bensin_forsikring = 7500
bensin_drivstoff = 1*km # Drivstoff til bensinbil koster 1,0 kr/km
bensin_bomavgift = 0.3*km # Bomavgift for bensinbil koster 0,3 kr/km

total_bensinbil = bensin_forsikring + trafikk_avg + bensin_drivstoff + bensin_bomavgift

# Beregning av differansen for ålige kostnader mellom bensin- og elbil.
diff = total_bensinbil - total_elbil

print("Årlige kostnader for elbil er", total_elbil, "kroner, mens det for bensinbil er", total_bensinbil, "kroner. Det koster", diff, "kroner mer i året med bensinbil sammenlignet med elbil." )
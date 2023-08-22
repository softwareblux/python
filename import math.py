from math import sqrt

# Konstanter
m = 60  # massen av hver elev, kg
gamma = 6.67 * 10 ** (-11)  # gravitasjonskonstanten, Nm^2/kg^2
R_planet = 6371000  # radiusen til planeten, m

# Variable krefter, utregning av kraftsum og akselerasjon
def a(r):
    G = gamma * m ** 2 / r ** 2  # gravitasjonskraft for hver elev, N
    sum_F = G  # kraftsum for hver elev, N
    aks = sum_F / m
    return aks

# Startverdier for bevegelsen
r1 = 2 * R_planet  # Nora starter i en høyde 2R over planetoverflaten
v1 = 0  # Nora starter i ro
r2 = R_planet  # Planetens overflate
v2 = 0  # Planeten er i ro
r = r1 - r2  # avstanden mellom Nora og planetoverflaten
t = 0  # starttid
collision_time = None  # tiden det tar å treffe planetens overflate

# Simulering av bevegelsen
dt = 0.01  # tidssteg i simuleringen, s
while r > 0:  # stopper simuleringen når Nora treffer planetens overflate
    v1 = v1 - a(r) * dt  # regner ut neste fart for Nora
    v2 = v2 + a(r) * dt  # regner ut neste fart for planeten
    r1 = r1 + v1 * dt  # regner ut neste posisjon for Nora
    r2 = r2 + v2 * dt  # regner ut neste posisjon for planeten
    r = r1 - r2  # ny avstand mellom Nora og planetoverflaten
    t = t + dt  # går til neste tidspunkt

    if r <= 0 and collision_time is None:
        collision_time = t  # Lagrer tiden det tar å treffe planetens overflate

print("Tid før kollisjon:", collision_time / 3600, "timer")

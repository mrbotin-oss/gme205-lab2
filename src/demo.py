from spatial import Point

p = Point ("A", 121.0, 14.6)
print(p.id, p.lon, p.lat)
print(p.to_tuple())

distance = Point (121, 14.6, 90, 15)
print(distance)  # m

a = Point ("B", 122.0, 13.6)
print(p.distance_to(a))


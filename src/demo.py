##from spatial import Point

##p = Point ("A", 121.0, 14.6)
##print(p.id, p.lon, p.lat)
##print(p.to_tuple())

##distance = Point (121, 14.6, 90, 15)
##print(distance)  # m

##a = Point ("B", 122.0, 13.6)
##print(p.distance_to(a))

### Part C. Designing a Spatial Collection: PointSet (The Challenge) 

from spatial import PointSet

def main():
    points = PointSet.from_csv("data/points.csv")

    print("Point count:", points.count())
    print("Bounding box:", points.bbox())

    tagged_points = points.filter_by_tag("poi")
    print("poi points:", tagged_points.count())

if __name__ == "__main__":
    main()
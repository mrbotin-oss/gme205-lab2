# Project Title
# How to set up the virtual environment
# How to run Python scripts

### Reflections

# Object vs Geometry
- The difference between modelling points when you treat them as rows and columns in a table is that these are all just data from the table, you fast forward into thinking that these rows and columns can be data manipulated, we jump into spatial analysis. 
- But if you model the point as object then you think in terms of its geometeric meaning, like what can a point do? Should this behavior happen in this point? In a way, we treat these points as object that makes you think about modeling reality.

# Responsibility
- The behavior belonged in a Point if we're talking about per point (either only one point or one point interacting with another single point)
    Example,
    distance = Point (121, 14.6, 90, 15)
    print(distance)  # m
- While PointSet is the collection of points, this is a class or a group. A class manages our collection of points. The name of our colletion of points is PointSet and the name of our data is points. 
    Example,
    tagged_points = points.filter_by_tag("poi")
    print("poi points:", tagged_points.count())

# Modelling Insight
- It is important to know the diffrenece beatween geometry, meaning, and behavior. Geometry is the raw data like a point or collection of points. Meaning is what represent those object like a coordinates of a point. Behavior defined what actions those point or collection of points could perform. 
- Separating these three before combining them helps us understand object modeling better because it forces us to think clearly about what something is, what it represents, and what it should be responsible for doing. Instead of immediately writing code that mixes coordinates, formulas, and program flow, we slow down and take a moment to plan first.
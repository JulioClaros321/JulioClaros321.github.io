from HW6 import Robot, CompoundRobot

# build some Robot objects
r1 = Robot(name="Robot 1")
r2 = Robot(name="Robot 2")
r3 = Robot()
r4 = Robot()

# test the Robot objects
assert r1.name == "Robot 1", \
    "the value of r1's name attribute is wrong (should be 'Robot 1')"
assert r3.name is None, \
    "the value of r3's name attribute is wrong (should be None)"
assert r1.energy == 20, \
    "the value of r1's energy attribute is wrong (should be 20)"
assert r3.energy == 20, \
    "the value of r3's energy attribute is wrong (should be 20)"
assert r1.compound is None, \
    "the value of r1's compound attribute is wrong (should be None)"
assert r3.compound is None, \
    "the value of r3's compound attribute is wrong (should be None)"

# build a CompoundRobot object
cr1 = r1 + r2

# test the CompoundRobot object and its components
assert cr1.energy == 40, \
    "the value of cr1's energy attribute is wrong (should be 40)"
assert r1 in cr1.components, \
    "cr1's components attribute does not include r1"
assert r2 in cr1.components, \
    "cr1's components attribute does not include r2"
assert r1.compound == cr1, \
    "the value of r1's compound attribute is wrong after addition" \
    " (should refer to cr1)"
assert r2.compound == cr1, \
    "the value of r2's compound attribute is wrong after addition" \
    " (should refer to cr1)"

# add another robot to the CompoundRobot
cr1 += r3

# test the CompoundRobot object again, as well as its components
assert cr1.energy == 60, \
    "the value of cr1's energy attribute is wrong (should be 60)"
assert r1 in cr1.components, \
    "cr1's components attribute does not include r1 after in-place" \
    " addition"
assert r2 in cr1.components, \
    "cr1's components attribute does not include r2 after in-place" \
    " addition"
assert r3 in cr1.components, \
    "cr1's components attribute does not include r3 after in-place" \
    " addition"
assert r3.compound == cr1, \
    "the value of r3's compound attribute is wrong after in-place" \
    " addition (should refer to cr1)"

# add a CompoundRobot and a regular Robot
cr2 = r4 + cr1

# test the new CompoundRobot object
assert cr2.energy == 80, \
    "the value of cr2's energy attribute is wrong (should be 80)"
assert r4 in cr2.components, \
    "cr2's components attribute does not include r4"
assert cr1 in cr2.components, \
    "cr2's components attribute does not include cr1"
assert r4.compound == cr2, \
    "the value of r4's compound attribute is wrong after addition" \
    " (should refer to cr2)"
assert cr1.compound == cr2, \
    "the value of cr1's compound attribute is wrong after addition" \
    " (should refer to cr2)"

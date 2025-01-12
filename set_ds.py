"""student_id={34,46,64,34,85,25,64}
print (student_id)
print (type(student_id))

student_id.add(78)
print (student_id)
names=["kate","oliver","harry","loki"]
student_id.update(names)
print (student_id)
student_id.discard("kate")
print (student_id)

print (len (student_id))
"""

set_1={1,2,3,4,5,6}
set_2={4,5,6,7,8,9}

print(set_1.union(set_2))
print(set_1|set_2)

print(set_1.intersection(set_2))
print(set_1&set_2)

print(set_1.difference(set_2))

print(set_1.symmetric_difference(set_2))
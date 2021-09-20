# create two sets and find the difference, one set will hold all rooms while the other holds duplicates found
k = int(input())
rooms = map(int, input().split())
all_rooms = set()
duplicate_rooms = set()
for i in rooms:
  if i in all_rooms:
    duplicate_rooms.add(i)
  if i not in all_rooms:
    all_rooms.add(i)
cap_room = next(iter(all_rooms.difference(duplicate_rooms)))
print(cap_room)

# one test case fails -> new room comes after captains room is found
# k = int(input())
# rooms = map(int, input().split())
# set_rooms = set()
# cap_room = 0
# for i in rooms:
#     if i not in set_rooms:
#         cap_room = i
#         set_rooms.add(i)
# print(cap_room)
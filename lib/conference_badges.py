def badge_maker(name):
    return f"Hello, my name is {name}."

def batch_badge_creator(names):
    return [f"Hello, my name is {name}." for name in names]

def assign_rooms(names):
    rooms = range(1,9)
    new_list =[]
    for room in rooms:
        new_list.append(f"Hello, {names[room - 1]}! You'll be assigned to room {room}!")
    return new_list

def printer(names):
    for batch in batch_badge_creator(names):
        print(batch)
    for assignment in assign_rooms(names):
        print(assignment)
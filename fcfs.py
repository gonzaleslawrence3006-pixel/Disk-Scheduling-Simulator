def simulate_fcfs(head, queue): 
    current = head #track the current head position
    total_movement = 0 #track total head movement
    sequence = [head] #initialize sequence with the initial head position(head and queue)
    steps = [] #store the steps of head movement

    for req in queue:
        distance = abs(req - current) #abs is absolute so every answer is positive
        steps.append((current, req, distance)) 
        total_movement += distance #count total head movement
        current = req #update ulo
        sequence.append(current) #add the new head position to the sequence

    return sequence, steps, total_movement

def print_schedule_table(algo_name, head, queue, steps, total_movement): 
    print("\nDISK SCHEDULING ALGORITHM")
    print(f"Current Head Position: {head}")
    print(f"Requests: {', '.join(map(str, queue))}\n") #join the queue in one string with commas and spaces

    print(algo_name.upper())
    print(f"{'STEP':<8} {'HEAD MOVEMENT':<20} {'DISTANCE':<10}")

    for step_num, (src, dst, dist) in enumerate(steps, start=1):
        movement_str = f"{src} - {dst}"
        print(f"{step_num:<8} {movement_str:<20} {dist:<10}")

    print(f"{'':<8} {'TOTAL DISTANCE':<20} {total_movement:<10}")

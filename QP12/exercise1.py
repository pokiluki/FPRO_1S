
def do_not_intersect(rect1, rect2):

    if rect1['x2'] < rect2['x1'] or rect2['x2'] < rect1['x1']:
        return True


    if rect1['y2'] < rect2['y1'] or rect2['y2'] < rect1['y1']:
        return True

    return False


def number_of_collisions(objects):
    num_collisions = 0

    for i in range(len(objects)):
        for j in range(i + 1, len(objects)):
            if do_not_intersect(objects[i], objects[j]):
                continue

            num_collisions += 1

    return num_collisions



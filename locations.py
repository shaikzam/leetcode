def count_suitable_locations(centers, d):
    suitable_locations = 0

    for i in range(-10,10):
        total_distance = 0

        for j in centers:
            distance = abs(j - i)
            if distance > d:
                total_distance = float('inf')  # Skip the current potential location
                break
            total_distance += distance

        if total_distance <= d:
            suitable_locations += 1

    return suitable_locations

def main():
    centers = [-1, 2, 4]
    d = 6
    result = count_suitable_locations(centers, d)
    print("Number of suitable locations:", result)

if __name__ == "__main__":
    main()





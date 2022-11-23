with open(file='data.txt') as file:
    data = file.read().split("\n")
    big_caves = set()
    small_caves = set()
    graph = {}

    # PARSING...
    for entry in data:
        v1, v2 = entry.split("-")

        if v1.isupper():
            big_caves.add(v1)
        else:
            if v1 not in ['start', 'end']:
                small_caves.add(v1)
        if v2.isupper():
            big_caves.add(v2)
        else:
            if v2 not in ['start', 'end']:
                small_caves.add(v2)

        if v1 not in graph:
            graph[v1] = [v2]
        else:
            graph[v1].append(v2)
        if v2 not in graph:
            graph[v2] = [v1]
        else:
            graph[v2].append(v1)


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def part_one(graph, curr_vertex, visited):
    visited.append(curr_vertex)
    if visited[0] == 'start':
        for vertex in graph[curr_vertex]:
            if vertex in big_caves:
                part_one(graph, vertex, visited.copy())
            elif vertex not in visited:
                part_one(graph, vertex, visited.copy())

        if visited[-1] == 'end':
            distinct_paths.append(visited)


def part_two(graph, curr_vertex, visited, cave_visited_twice):
    visited.append(curr_vertex)
    if visited[0] == 'start':
        if curr_vertex in small_caves and visited.count(curr_vertex) == 2:
            cave_visited_twice = True

        for vertex in graph[curr_vertex]:
            if vertex in big_caves:
                part_two(graph, vertex, visited.copy(), cave_visited_twice)
            elif cave_visited_twice and vertex not in visited:
                part_two(graph, vertex, visited.copy(), cave_visited_twice)
            elif not cave_visited_twice and vertex in small_caves:
                part_two(graph, vertex, visited.copy(), cave_visited_twice)
            elif vertex not in visited:
                part_two(graph, vertex, visited.copy(), cave_visited_twice)

        if visited[-1] == 'end':
            distinct_paths.append(visited)


# part one:
distinct_paths = []
for vertex in graph:
    part_one(graph, vertex, [])

print(len(distinct_paths))

# part two:
distinct_paths = []
for vertex in graph:
    part_two(graph, vertex, [], False)

print(len(distinct_paths))

from trains.models import Train


def dfs_paths(graph, start, goal):
    stack = [(start, [start])]
    while stack:
        (vertex, path) = stack.pop()
        if vertex in graph.keys():
            for next in graph[vertex] - set(path):
                if (next == goal):
                    yield path + [next]
                else:
                    stack.append((next, path + [next]))


def get_graph(qs):
    graph = {}
    for q in qs:
        graph.setdefault(q.from_city_id, set())
        graph[q.from_city_id].add(q.to_city_id)
    return graph


def check_ways(all_ways, cities):
    if not all_ways:
        raise ValueError("Данного маршута не существует")
    if cities:
        cities_id = [city.id for city in cities]
        right_ways = []
        for way in all_ways:
            if all(city in way for city in cities_id):
                right_ways.append(way)
        if not right_ways:
            raise ValueError("Маршут через эти города невозможен")
    else:
        right_ways = all_ways
    return right_ways


def get_travel_time(qs, right_ways, travelling_time):
    routes = []
    all_trains = {}
    for q in qs:
        all_trains.setdefault((q.from_city_id, q.to_city_id), [])
        all_trains[(q.from_city_id, q.to_city_id)].append(q)
    for route in right_ways:
        tmp = {}
        tmp['trains'] = []
        total_time = 0
        for i in range(len(route) - 1):
            qs = all_trains[(route[i], route[i + 1])]
            q = qs[0]
            total_time += q.travel_time
            tmp['trains'].append(q)
        tmp['total_time'] = total_time
        if total_time <= travelling_time:
            routes.append(tmp)
    if not routes:
        raise ValueError('Время в пути больше заданного')
    return routes


def sort_routes(routes):
    sorted_routes = []
    if len(routes) == 1:
        sorted_routes = routes
    else:
        times = list(set(r['total_time'] for r in routes))
        times = sorted(times)
        for time in times:
            for route in routes:
                if time == route['total_time']:
                    sorted_routes.append(route)
    return sorted_routes


def get_routes(request, form) -> dict:
    qs = Train.objects.all().select_related('from_city', 'to_city')
    context = {'form': form}
    graph = get_graph(qs)
    data = form.cleaned_data
    from_city = data['from_city']
    cities = data['cities']
    to_city = data['to_city']
    travelling_time = data['travelling_time']
    all_ways = list(dfs_paths(graph, from_city.id, to_city.id))
    right_ways = check_ways(all_ways, cities)
    routes = get_travel_time(qs, right_ways, travelling_time)
    context['routes'] = sort_routes(routes)
    print(context['routes'])
    context['cities'] = {'from_city': from_city, 'to_city': to_city}
    print(right_ways)
    return context

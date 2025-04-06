from collections import deque


def person_is_seller(*args, **kwargs):
    args = args
    kwargs = kwargs
    ...


def search(name):
    graph = []
    search_queue = deque()
    search_queue += graph[name]
    searched = []

    while search_queue:
        person = search_queue.popleft()
        if not person in searched:
            if person_is_seller(person):
                print(f"{person} is a mongo seller")
                return True
            else:
                search_queue += graph[person]
                searched.append(person)

    return False


search('you')

def find_lowest_cost_node(args):
    ...


costs = 0
processed = []
node = find_lowest_cost_node(costs)
graph: list = []
while node is not None:
    cost = costs[node]
    neighbors = graph[node]
    for n in neighbors.keys():
        new_cost = cost + neighbors[n]
        if costs[n] > new_cost:
            costs[n] = new_cost
            parents[n] = node
    processed.append(node)
    node = find_lowest_cost_node(costs)


def ind_lowest_cost_node(costs):
    lowest_cost = float('inf')
    lowest_cost_node = None
    for node in costs:
        cost = costs[node]
        if cost < lowest_cost and node not in processed:
            lowest_cost = cost
            lowest_cost_node = node
    return lowest_cost_node

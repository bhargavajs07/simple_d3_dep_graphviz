import json

# Two clusters of dependencies forming separate islands
dependencies = {
    'Island1': {
        'Project1': {'deps': ['LibraryA1', 'ModuleA1'], 'metadata': {'category': 'Project', 'field1': 'valueP1-1', 'field2': 'valueP2-1'}},
        'LibraryA1': {'deps': ['ModuleA1'], 'metadata': {'category': 'Library', 'field1': 'valueL1-1', 'field3': 'valueL3-1'}},
        'ModuleA1': {'deps': [], 'metadata': {'category': 'Module', 'field5': 'valueM1-1'}}
    },
    'Island2': {
        'Project2': {'deps': ['LibraryB2', 'ModuleB2'], 'metadata': {'category': 'Project', 'field1': 'valueP1-2', 'field2': 'valueP2-2'}},
        'LibraryB2': {'deps': ['ModuleB2'], 'metadata': {'category': 'Library', 'field2': 'valueL2-2', 'field4': 'valueL4-2'}},
        'ModuleB2': {'deps': [], 'metadata': {'category': 'Module', 'field6': 'valueM2-2'}}
    }
}

nodes = []
links = []

for island_key, island_value in dependencies.items():
    for node, details in island_value.items():
        nodes.append({'id': node, 'group': details['metadata']['category'], **details['metadata']})
        for target in details['deps']:
            links.append({'source': node, 'target': target, 'value': 1})

graph = {'nodes': nodes, 'links': links}


# Save to JSON file
json_file_path = './dependencies_enhanced_metadata.json'
with open(json_file_path, 'w') as f:
    json.dump(graph, f, indent=4)

json_file_path


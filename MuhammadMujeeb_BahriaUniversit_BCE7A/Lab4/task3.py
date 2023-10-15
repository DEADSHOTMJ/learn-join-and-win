original_list = [
    {'id': '#FF0000', 'color': 'Red'},
    {'id': '#800000', 'color': 'Maroon'},
    {'id': '#FFFF00', 'color': 'Yellow'},
    {'id': '#808000', 'color': 'Olive'}
]

specified_id = '#FF0000'
filtered_list = [d for d in original_list if d['id'] != specified_id]

print("Remove id", specified_id, "from the list:", filtered_list)

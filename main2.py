
# Game items being replaced

inventory = [ 'iron dagger', 'bronze dagger', 'AGS']

chest = ['bronze platebody', 'steel platelegs', 'coif']

for item in chest:
    inventory.append(item)
    chest.pop(0)

print(inventory)
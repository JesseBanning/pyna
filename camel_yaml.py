import yaml

pets = {"dogs": ['mudge', 'spot', 'fido'], "cats": ['fullffy', 'nobassowuier', 'catsdf']}

print(yaml.dump(pets))

with open("camel.yaml", "r") as f:
    data = yaml.load(f)

print(data)

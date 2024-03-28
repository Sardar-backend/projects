import yaml
#readin yaml and indexing it
with open ("abc.yaml","r") as st:
    z=dict()
    d=yaml.safe_load_all(st)
    o=enumerate(d)
    for i, d in o:
        z[i] = d
    print(z)
#  reading yaml
with open ("abc.yaml","r") as st:
    for x in yaml.safe_load_all(st):
        print(x)

import ansible_runner

out=ansible_runner.run(
    private_data_dir='',
    playbook='add_static_route.yml',
    inventory='inventory.ini',
    json_mode=True,

)
print(out)
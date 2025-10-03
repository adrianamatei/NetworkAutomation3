import subprocess

with subprocess.Popen(
    args=['ansible-playbook', '-i', 'inv.ini', 'add_static_route.yaml', '--ask-vault-pass'],
    stdout=subprocess.PIPE,
    stderr=subprocess.PIPE,
    stdin=subprocess.PIPE,
) as p:
    p.communicate(input=b'pynet3')
    return_code = p.wait()
    if return_code == 0:
        print("Successfully deployed ansible playbook")

import os, shutil

# read the answer; never ask
VISIBILITY = "{{ cookiecutter.github_repo_visibility }}"

REMOVE_PATHS = [
    '{% if cookiecutter.command_line_interface == "None" %}src/{{ cookiecutter.import_name }}/cli.py{% endif %}',
    # ...
]
for p in REMOVE_PATHS:
    p = p.strip()
    if p and os.path.isdir(p): shutil.rmtree(p)
    elif p and os.path.exists(p): os.remove(p)

print("✓ Created. Next: cd {{ cookiecutter.package_name }} && just init-github")

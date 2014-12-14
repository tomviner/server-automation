vagrant destroy --force

# need this when re-making a vagrant box (per port)
# ssh-keygen -f "~/.ssh/known_hosts" -R [127.0.0.1]:${PORT}

vagrant up &&

ansible-playbook tasks/vagrant_setup.yml --extra-vars="cwd='$(pwd)'"

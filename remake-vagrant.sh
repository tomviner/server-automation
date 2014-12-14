vagrant destroy --force

# need this when re-making a vagrant box (per port)
# ssh-keygen -f "~/.ssh/known_hosts" -R [127.0.0.1]:${PORT}

vagrant up --no-provision &&
./fix_vagrant_inventory.sh &&
vagrant provison


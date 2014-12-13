# http://docs.ansible.com/guide_vagrant.html#running-ansible-manually

ansible all $@ -vv \
    --inventory-file .vagrant/provisioners/ansible/inventory/vagrant_ansible_inventory \
    --private-key ~/.vagrant.d/insecure_private_key \
    --user vagrant \
    --sudo

Vagrant.configure("2") do |config|
  config.vm.box = "trusty32"
  config.vm.box_url = "https://cloud-images.ubuntu.com/vagrant/trusty/current/trusty-server-cloudimg-i386-vagrant-disk1.box"

  config.vm.network "public_network"
  config.vm.network :private_network, ip:"10.0.0.100"

  config.vm.provision "ansible" do |ansible|
    ansible.playbook = "vagrant.yml"
    ansible.sudo = true
    ansible.extra_vars = {
      ansible_ssh_user: 'vagrant',
      domain: "10.0.0.100"
    }
  end
end

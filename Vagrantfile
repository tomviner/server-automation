VAGRANTFILE_API_VERSION = "2"

Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|
  config.vm.box = "utopic32"
  config.vm.box_url = "https://cloud-images.ubuntu.com/vagrant/utopic/current/utopic-server-cloudimg-i386-vagrant-disk1.box"

  config.vm.provider "virtualbox" do |vb|
        vb.memory = 2048
        vb.cpus = 2
        vb.customize ["modifyvm", :id, "--natdnshostresolver1", "on"]
    end

  config.vm.network "public_network", bridge: 'wlan0'
  config.vm.network :private_network, ip:"10.0.0.100"

  config.vm.synced_folder ".", "/vagrant", disabled: true
  config.vm.synced_folder "./website", "/home/projadm/www/10.0.0.100", disabled: true

  config.vm.provision "ansible" do |ansible|
    ansible.playbook = "site.yml"
    ansible.sudo = true
    ansible.extra_vars = {
      ansible_ssh_user: 'vagrant',
      domain: "10.0.0.100"
    }
  end
end

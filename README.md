# Infrastructure as Code

This an example [ansible](https://docs.ansible.com) project, deploying the 'awesome' [wordgame](https://github.com/wolfpaulus/wordgame) docker container.

I'm using the trusted Digital Ocean - <i>The simplest cloud that scales with you.</i> - as a hosting provider.

After manually creating an account there and reserving one IP address, everything else happens through code.

The three Python script to 
- Create a Droplet
- Assign a static IP to the droplet
- Destroy a Droplet

require three environment varibales:

- DIGITALOCEAN_TOKEN: Your DigitalOcean API token
- DROPLET_NAME: The name of the droplet to create
- SSH_KEY: The SSH key to use for the droplet 

1. Running `create_droplet.py` will create the cheapest droplet
2. Running `assign_ip.py` will assign the previously reserved IP address to the droplet
3. Running `ansible-playbook playbooks/all.yml` will run all 4 playbooks
4. The wordgame app will become avaialbe at http://reserved_IP_address/ or the domain name, should you have mapped it at your registrar.


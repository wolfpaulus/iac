""" 
    Assign a reserved floating IP to a droplet.
    Requires the following environment variables:
    - DIGITALOCEAN_TOKEN: Your DigitalOcean API token
    - RESERVED_IP: The reserved floating IP address
    - DROPLET_NAME: The name of the droplet to assign the IP to
    Author: Wolf Paulus - https://wolfpaulus.com
"""
import os
import digitalocean


token = os.environ['DIGITALOCEAN_TOKEN']
reserved_ip = os.environ['RESERVED_IP']
droplet_name = os.environ['DROPLET_NAME']

try:
    manager = digitalocean.Manager(token=token)
    my_droplets = manager.get_all_droplets()
    for d in my_droplets:
        if d.name == droplet_name:
            ip = manager.get_floating_ip(reserved_ip)
            ip.assign(d.id)
            print(f"Assigned {reserved_ip} to {d.name}")
            break
except OSError as e:
    print(f"Error: {e}")

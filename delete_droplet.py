""" 
    Deletes a droplet from Digital Ocean 
    Requires the following environment variables:
    - DIGITALOCEAN_TOKEN: Your DigitalOcean API token
    - DROPLET_NAME: The name of the droplet to delete
    Author: Wolf Paulus - https://wolfpaulus.com    
"""
import os
import digitalocean

token = os.environ['DIGITALOCEAN_TOKEN']
droplet_name = os.environ['DROPLET_NAME']

for droplet in digitalocean.Manager(token=token).get_all_droplets():
    if droplet.name == droplet_name:
        droplet.destroy()
        print("Droplet destroyed")
        break

#
# This repository is an Anvil app. Learn more at https://anvil.works/
# To run the server-side code on your own machine, run:
# pip install anvil-uplink
# python -m anvil.run_app_via_uplink YourAppPackageName

__path__ = [__path__[0] + "/server_code", __path__[0] + "/client_code"]

import anvil.server
import anvil.users
import anvil.tables as tables
from anvil.tables import app_tables

def show_landing_page():
    open_form('home')

# Make this the default startup form
anvil.server.call('anvil.private.set_default_form', 'home')

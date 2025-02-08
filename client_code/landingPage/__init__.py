from ._anvil_designer import landingPageTemplate
from anvil import *
import os

class landingPage(landingPageTemplate):
    def __init__(self, **properties):
        # Set Form properties and Data Bindings.
        self.init_components(**properties)

        # Load the external HTML file into the HTML component
        try:
            filepath = "_/theme/staticLanding.html"
            print(f"Attempting to open file: {filepath}")
            with open(filepath, 'r') as f:
                html_string = f.read()
            self.html = html_string
            print("HTML loaded successfully.")
        except FileNotFoundError:
            print(f"Error: File not found at {filepath}")
            self.html = "<p>Error: Landing page HTML file not found.</p>"
        except Exception as e:
            print(f"Error loading HTML: {e}")
            self.html = f"<p>Error loading landing page: {e}</p>"

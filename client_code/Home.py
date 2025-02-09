from ._anvil_designer import HomeTemplate
from anvil import *

class Home(HomeTemplate):
  def __init__(self, **properties):
    self.init_components(**properties)
    # Initialize the landing page
    self.content_panel.tag.html = """
      <div class="landing-content">
        <div class="header landing-header">
          <h1>Willow River Automation Services</h1>
          <h2>Streamlining Workflows, Automating Success.</h2>
        </div>
        <div class="nav">
          <a href="#">Home</a>
          <a href="#">About Us</a>
          <a href="#">Services</a>
          <a href="#">Contact</a>
          <button>Client Login</button>
        </div>
        <div class="hero">
          <h1>Optimize your business with cutting-edge automation solutions.</h1>
          <p>Discover Our Services!</p>
          <button>Get Started</button>
        </div>
        <div class="content">
          <h2>Why Choose Willow River Automation Services?</h2>
          <p>Brief paragraph explaining the benefits of automation, reducing manual work, and improving efficiency for small businesses.</p>
          <button>Learn More About Our Process</button>
        </div>
        <div class="content">
          <h2>Features & Services</h2>
          <div class="services">
            <!-- Dynamic section displaying multiple services -->
          </div>
        </div>
        <div class="content">
          <h2>See the Impact of Automation!</h2>
          <div class="metrics">
            <p>Total Automation Runs: 10,000+</p>
            <p>Time Saved: 500+ Hours Automated</p>
            <p>Revenue Impact: +15% Efficiency Gain</p>
          </div>
        </div>
        <div class="content">
          <h2>What Our Clients Say</h2>
          <div class="testimonials">
            <!-- Dynamically displays client feedback & case studies -->
          </div>
        </div>
        <div class="footer">
          <p>© 2025 Willow River Automation Services. All Rights Reserved.</p>
          <a href="#">Privacy Policy</a>
          <a href="#">Terms & Conditions</a>
          <div class="social-media">
            <!-- Social Media Icons -->
          </div>
        </div>
      </div>
    """

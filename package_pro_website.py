import zipfile

# Define the updated HTML, CSS, and JS content
html_content = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>PRO | Digital Marketing Portfolio</title>
  <link rel="stylesheet" href="styles.css">
</head>
<body>
  <a href="#main" class="skip-link">Skip to main content</a>
  <header>
    <div class="logo">PRO</div>
    <p class="tagline">Performance. Results. Optimization.</p>
    <button class="menu-toggle" aria-expanded="false" aria-controls="nav-menu" aria-label="Toggle navigation menu">
      <span class="icon open" aria-hidden="true">☰</span>
      <span class="icon close" aria-hidden="true" style="display:none;">✖</span>
    </button>
    <nav class="nav-links" id="nav-menu" role="navigation" aria-label="Main navigation">
      <a href="#about">About</a>
      <a href="#skills">Skills</a>
      <a href="#projects">Projects</a>
      <a href="#resume">Resume</a>
      <a href="#contact">Contact</a>
    </nav>
  </header>

  <main id="main">
    <section id="about" class="fade-in">
      <h2>About Me</h2>
      <p>I’m a digital marketer passionate about helping brands grow through data-driven strategies and creative storytelling.</p>
    </section>

    <section id="skills" class="fade-in">
      <h2>Skills</h2>
      <ul>
        <li>SEO & SEM</li>
        <li>Google Analytics & Tag Manager</li>
        <li>Content Marketing</li>
        <li>Email Campaigns</li>
        <li>Social Media Strategy</li>
      </ul>
    </section>

    <section id="projects" class="fade-in">
      <h2>Projects</h2>
      <div class="project">
        <h3>Campaign Optimization</h3>
        <p>Increased ROI by 35% through A/B testing and audience segmentation.</p>
      </div>
    </section>

    <section id="resume" class="fade-in">
      <h2>Resume</h2>
      <p><a href="Your_Resume.pdf" download>Download My Resume</a></p>
    </section>

    <section id="contact" class="fade-in">
      <h2>Contact</h2>
      <p>Email: <a href="mailto:your.email@example.com">your.email@example.com</a></p>
      <p>LinkedIn: <a href="https://linkedin.com/in/yourprofile" target="_blank" rel="noopener noreferrer">yourprofile</a></p>
    </section>
  </main>

  <footer>
    <p>© 2025 PRO. All rights reserved.</p>
  </footer>

  <script src="script.js"></script>
</body>
</html>
"""

css_content = """:root {
  --gold: #D4AF37;
  --deep-blue: #004466;
  --teal: #00B8A9;
  --coral: #FF6B6B;
  --light

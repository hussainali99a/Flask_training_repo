from flask import Flask


app = Flask(__name__)


@app.route('/')
def home():
    return '''

<h1 style = "color:red; text-align =  center;">Sagar institute of Science and Technology</h1>
            <img scr="data:image/jpeg;base64,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">
           <h1> Engineering</h1>
<p>The B.Tech. Engineering Program at Sagar Group of Institutions is developed from an industrial point of view, with a great focus on modern technologies employed in the industries. Engineers are the focal point in our economy to design, test, and develop the next generation of products and services for the betterment of society. In this regard, the pedagogy is designed based on industry-oriented training modules a level extra than the standard university curriculum. Similarly, the MTech Engineering Program is developed from a research point of view to inculcate the spirit of innovation and development in Science & Technology.</p>

<h2>B.Tech.</h2>
<ul>
<li>Civil Engineering</li>
<li>Computer Science & Engineering</li>
<li>Computer Science & Information Technology</li>
<li>CSE with Artificial Intelligence and Data Science</li>
<li>CSE with Artificial Intelligence and Machine Learning</li>
<li>CSE with Internet of Things</li>
<li>CSE with Cyber Security</li>
<li>Electrical & Electronics Engineering</li>
<li>Electrical Engineering</li>
<li>Electronics & Communication Engineering</li>
<li>Mechanical Engineering</li>
</ul>
<h2>M.Tech.</h2>
<li>Computer Science & Engineering</li>
<li>Construction Technology and Management</li>
<li>Digital Communication</li>
<li>Machine Design</li>
<li>Power System</li>
<li>Structural Engineering</li>
<li>Thermal Power & Engineering</li>
<li>Very Large Scale Integration (VLSI) Design</li>

'''
    
            

if __name__ == "__main__" :
    app.run(debug = True)
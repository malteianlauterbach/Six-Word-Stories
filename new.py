#in flask, select a random text from a list of texts and display it on the screen 
list = "He bottle-feeds his wife's killer.","`Goodbye, mission control. Thanks for trying.`"," ███ trust ███ ███ ██████ the government, ██ ██ █ ████ █████ everything ██████ ██ is █████ ███ ██████ █ ███ fine ███ ██████.","Goodbye, doctor. Thank you for trying.","Voyager still transmitted, but Earth didn't.","Trembling, they moved Lovecraft to nonfiction.","Brought roses home. Keys didn’t fit.","The smallest coffins are the heaviest.","Sticks. Spears. Swords. Guns. Nukes. Sticks.","The murderer still wears his badge","Scientists develop first atomic bomb. Again.","T.H.C., L.S.D., D.U.I., C.P.R., D.O.A., R.I.P","Paramedics finished her text, `....love you`.","One bullet is a lifetime supply.","Sorry soldier, shoes sold in pairs.","Birth certificate. Death certificate. One pen.","`Passengers, this isn't your captain speaking.`","Flags don't make very good fathers.","`Just married!` read the shattered windshield.","Wikipedia edit: changed `is` to `was`.","The riot gear hid his tears.","Please select your child's eye color.","The war is over! dozens celebrate.","`Love you`, he whispered, drinking alone.","Alzheimer’s took what the fire didn’t.","Everyone learned to ignore the cameras."



import flask
import random
#initialize the flask app
app = flask.Flask(__name__)
#define a route
@app.route('/')
def index():
    #choose random text from the list 
    text = random.choice(list)
    #display the text in a div  both vertically and horizontally in the middle of the page and set the font to monospace. at the end of the page, display "a"
    return flask.render_template_string('''
    <div style="font-size:36px; font-family: monospace; position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%);">{text}</div>
    <div style="font-size:18px; font-family: monospace; position: absolute; top: 80%; left: 50%; transform: translate(-50%, -50%);text-align: center;">
        6 word  stories, made with love by Malte Ian lauterbach.
        <br>
        <a href="https://www.reddit.com/r/sixwordstories"> </br>
        Some texts from: <a href="https://www.reddit.com/r/sixwordstories"/</a> 
    </div>
    '''.format(text, text=text))
    
#run the app
app.run()   # return '<div style="font-size:36px; font-family: monospace; position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%);">{}</div>'.format(text)

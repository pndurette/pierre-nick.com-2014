from flask import Flask, g

#app = Flask(__name__,
#            static_folder="./static",
#            template_folder="./templates")

app = Flask(__name__)

import views

# Set a secret key (needed by Flask for sessions)
app.secret_key = '^%Yvt$dsg&j8&h%G$Fgdg%3*%&$#C$32$b'

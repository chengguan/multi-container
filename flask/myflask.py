from flask import Flask, request, render_template
import datetime
import base64
import io
import qrcode

app = Flask(__name__)

@app.route("/")
def hello():
    return render_template("index.html", time=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

@app.route("/qrrequest")
def qr_request():
    return render_template("qrrequest.html")

@app.route("/showqr", methods=['POST', 'GET'])
def show_qr():
    if request.method == 'GET':
        # Get the foreground and background color from input argument. Apply back and white if not found.
        fg_color = request.args.get('fgcolor', '#000000')
        bg_color = request.args.get('bgcolor', '#ffffff')
        input_qr_data = request.args.get('qrdata', '')
        box_size = int(request.args.get('resize', '5'))

        if box_size < 1:
            box_size = 1

        qr = qrcode.QRCode(version=1,
                        error_correction=qrcode.constants.ERROR_CORRECT_L,
                        box_size=box_size,
                        border=4,)
        
        qr.add_data(input_qr_data)
        qr.make(fit=True)
        img = qr.make_image(fill_color=fg_color, back_color=bg_color)

        #img = qrcode.make(request.args.get('qrdata', ''))

        data = io.BytesIO()
        img.save(data, "JPEG")
        encoded_img_data = base64.b64encode(data.getvalue())

        return render_template("showqr.html", 
            img_data=encoded_img_data.decode('utf-8'), 
            qrdata=input_qr_data,
            box_size=box_size,
            fgcolor=fg_color,
            bgcolor=bg_color)

@app.route("/about")
def about():
    return render_template("about.html")

@app.errorhandler(404)
def page_not_found(error):
    return render_template('page_not_found.html', error=error), 404

if __name__ == "__main__":
    app.run(host='0.0.0.0')
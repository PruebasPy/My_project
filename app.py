from flask import Flask, request
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

app = Flask(__name__)

@app.route('/')
def registro():
    return open('registro.html').read()

@app.route('/submit', methods=['POST'])
def submit():
    nombre = request.form['nombre']
    documento = request.form['documento']
    fecha_nacimiento = request.form['fecha_nacimiento']
    edad = request.form['edad']
    lugar_nacimiento = request.form['lugar_nacimiento']
    direccion = request.form['direccion']
    correo = request.form['correo']
    telefono = request.form['telefono']
    
    # Crear el mensaje de notificación con todos los datos del formulario
    mensaje = f'''
    Nombre: {nombre}
    Tipo y Número de Documento: {documento}
    Fecha de Nacimiento: {fecha_nacimiento}
    Edad: {edad}
    Lugar de Nacimiento: {lugar_nacimiento}
    Dirección: {direccion}
    Correo Electrónico: {correo}
    Teléfono: {telefono}
    '''
    
    # Envía el correo de notificación con todos los datos del formulario
    enviar_correo('cuentaparaproyectospython@gmail.com', 'Nuevo Registro', mensaje)
    
    # Envía el correo de confirmación al usuario
    enviar_correo(correo, 'Registro Exitoso', '¡Gracias por registrarte!')

    return 'Registro exitoso'

def enviar_correo(destinatario, asunto, mensaje):
    remitente = 'proyectosdeprogramacionpruebas@gmail.com'
    password = 'gesc fwrj hkgy fqmt'

    msg = MIMEMultipart()
    msg['From'] = remitente
    msg['To'] = destinatario
    msg['Subject'] = asunto

    msg.attach(MIMEText(mensaje, 'plain'))

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(remitente, password)
    server.sendmail(remitente, destinatario, msg.as_string())
    server.quit()

if __name__ == '__main__':
    app.run()
  GNU nano 2.7.4                                      Arquivo: dev/gpio.py                                                   


@app.route('/gate')
def open_gate():
    GPIO.output(gate, GPIO.LOW)
    sleep(0.5)
    GPIO.output(gate, GPIO.HIGH)
    return '{"status" : "gate unlocked"}'

@app.route('/lighton')
def lighton():
    GPIO.output(light, GPIO.LOW)
    return '{"status" : "light on"}'

@app.route('/lightoff')
def lightoff():
    GPIO.output(light, GPIO.HIGH)
    return '{"status" : "light off"}'

@app.route('/reboot')
def reboot():
    system('systemctl reboot')
    return '{"status" : "system rebooting"}'

if __name__ == '__main__':
    app.run(host='0.0.0.0')



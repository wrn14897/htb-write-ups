from flask import Flask, Response, session, render_template
import functools, random, string, os, re

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'tlci0GhK8n5A18K1GTx6KPwfYjuuftWw')


def calc(recipe):
    # maybe we should leverage this garage dict for mapping functional call
    global garage
    # restrict the use of __builtins__ by giving value None to the '__builtins__'
    builtins, garage = {'__builtins__': None}, {}
    try:
        print('EXECUTE...')
        exec(recipe, builtins, garage)
    except:
        # DEBUG recipe
        raise


def GFW(func): # Great Firewall of the observable universe and it's infinite timelines
    @functools.wraps(func)
    def federation(*args, **kwargs):
        ingredient = session.get('ingredient', None)
        measurements = session.get('measurements', None)

        recipe = '%s = %s' % (ingredient, measurements)
        print(f'recipe: \n{recipe}')
        if ingredient and measurements and len(recipe) >= 20:
            regex = re.compile('|'.join(map(re.escape, ['[', '(', '_', '.'])))
            matches = regex.findall(recipe)

            if matches:
                print('BLOCK !!!!')
                return render_template('index.html', blacklisted='Morty you dumbass: ' + ', '.join(set(matches)))
            if len(recipe) > 300:
                return func(*args, **kwargs) # ionic defibulizer can't handle more bytes than that

            print('HACK !!!!')
            calc(recipe)
            # return render_template('index.html', calculations=garage[ingredient])
            return func(*args, **kwargs) # rick deterrent

        # we don't wanna go here since session will be reset
        ingredient = session['ingredient'] = ''.join(random.choice(string.ascii_lowercase) for _ in range(10))
        measurements = session['measurements'] = ''.join(map(str, [random.randint(1, 69), random.choice(['+', '-', '*']), random.randint(1,69)]))
        print('calc: %s = %s' % (ingredient, measurements))
        calc('%s = %s' % (ingredient, measurements))
        return render_template('index.html', calculations=garage[ingredient])
    return federation


@app.route('/')
@GFW
def index():
    return render_template('index.html')


@app.route('/debug')
def debug():
    return Response(open(__file__).read(), mimetype='text/plain')


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

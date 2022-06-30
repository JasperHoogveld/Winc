# Do not modify these lines
__winc_id__ = '7b9401ad7f544be2a23321292dd61cb6'
__human_name__ = 'arguments'

# Add your code after this line


from asyncio.windows_events import NULL
#from readline import get_current_history_length


def greet(name, greeting_template = "Hello, <name>!"):
    if greeting_template == NULL:
        greeting = "Hello, " + name + "!"
    else:
        greeting = greeting_template.replace('<name>', name)
    return greeting

def force(mass, body = 'earth'):
    gravity = gravity_per_body[body] * mass
    return gravity

def pull(m1, m2, d):
    G = 6.674*(10**-11)
    grav_pull = G * ((m1 * m2) / d ** 2)
    return grav_pull

gravity_per_body = {
        'sun': float(round(274, 1)),
        'jupiter': float(round(24.92, 1)),
        'neptune': float(round(11.15, 1)),
        'saturn': float(round(10.44, 1)),
        'earth': float(round(9.798, 1)),
        'uranus': float(round(8.87, 1)),
        'venus': float(round(8.87, 1)),
        'mars': float(round(3.71, 1)),
        'mercury': float(round(3.7, 1)),
        'moon': float(round(1.62, 1)),
        'pluto': float(round(0.58, 1))
    }


#print(greet('jasper', "What's up, <name>!"))
#print(force(100000, 'jupiter'))
print(pull(800, 1500, 3))

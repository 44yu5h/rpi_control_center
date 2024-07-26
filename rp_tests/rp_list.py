# flake8: noqa
from gettext import gettext as _

names = [
    'RP_GPIO',
    'RP_I2C',
    'RP_SPI',
    'RP_CAM',
    'RP_AUDIO',
    'RP_SETTINGS',
]

tooltips = {
    'RP_GPIO': _('GPIO'),
    'RP_I2C': _('I2C'),
    'RP_SPI': _('SPI'),
    'RP_CAM': _('Camera'),
    'RP_AUDIO': _('Audio'),
    'RP_SETTINGS': _('Settings'),
}

gpio = [
    '3V3',   '5V',
    '2',     '5V',
    '3',     'GND',
    '4',     '14',
    'GND',   '15',
    '17',    '18',
    '27',    'GND',
    '22',    '23',
    '3V3',   '24',
    '10',    'GND',
    '9',     '25',
    '11',    '8',
    'GND',   '7',
    'EEP',   'EEP',
    '5',     'GND',
    '6',     '12',
    '13',    'GND',
    '19',    '16',
    '26',    '20',
    'GND',   '21',
]

disabled_gpio = [
    'EEP',
    '5V',
    'GND',
    '3V3',
]

settings = {
    'i2c': _('I2C Interface'),
    'spi': _('SPI Interface'),
    'camera': _('Camera Interface'),
    'vnc': _('VNC Server'),
    'ssh': _('SSH Server'),
    'autologin': _('Autologin'),
    'boot_splash': _('Boot Splash Screen'),
    'boot_cli': _('Boot into CLI'),
}

settings_status = {
    # 1 = on, 0 = off
    'i2c': 0,
    'spi': 0,
    'camera': 1,
    'vnc': 1,
    'ssh': 1,
    'autologin': 0,
    'boot_splash': 1,
    'boot_cli': 0,
}

# advanced_settings_jumbo = {
#     'Boot Behaviour': ('do_boot_behaviour', 'CLI', 'CLI with Autologin', 'GUI', 'GUI with Autologin'),
# }

# advanced_settings_toggle = {
#     'Boot Splash Screen' : 'do_boot_splash',
# }

boxes_settings_layout = [
    'b1', 'b2', 'b3', 'b4', 'b5', 'b6',
]

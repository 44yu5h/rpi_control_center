import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gdk

from gettext import gettext as _

import rp_tests.rp_list as rp_list
import digitalio
import board

def gui():
    scrolled_window = Gtk.ScrolledWindow()
    mainVbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
    mainVbox.set_margin_bottom(60)
    scrolled_window.add(mainVbox)
    scrolled_window.set_policy(hscrollbar_policy=Gtk.PolicyType.AUTOMATIC, vscrollbar_policy=Gtk.PolicyType.AUTOMATIC)
    secVbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
    gpioTopRow = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)
    gpioBottomRow = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)
    gpioBottomRow.set_halign(Gtk.Align.CENTER)
    gpioTopRow.set_halign(Gtk.Align.CENTER)
            
    # Set the background color of the canvas
    scrolled_window.override_background_color(Gtk.StateType.NORMAL, Gdk.RGBA(.92, .92, .92, 1))        

    gpiotxt=Gtk.Label()
    gpiotxt.set_markup('<span font="25">GPIO Pins Control</span>') 
    gpiotxt.set_use_markup(True)
    gpiotxt.show()
    
    # load css
    css = b"""
    button.5v, button.5v:checked, button.5v:active,
    button.3v3, button.3v3:checked, button.3v3:active{
        color: #FFF;
        background-color: #FF616D;
    }
    button.gnd, button.gnd:checked, button.gnd:active {
        background-color: #000;
        color: #FFF;
    }
    button.eep, button.eep:checked, button.eep:active {
        color: #000;
        background-color: #FFF;
    }
    .gpio-tb{
        border: none;
        color: #FFF;
        border-radius: 50px;
        font-size: 18px;
    }

    .gpio-tb:checked, .gpio-tb:active{
        background-color: #A3F5FF;
        color: #000;
            }
            
    #secVbox{
        border-radius: 25px;
    }
    """
    
    style_provider = Gtk.CssProvider()
    style_provider.load_from_data(css)
    Gtk.StyleContext.add_provider_for_screen(
        Gdk.Screen.get_default(),
        style_provider,
        Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION
)
    
    # create toggle buttons
    for index, pin in enumerate(rp_list.gpio):
        btn = Gtk.ToggleButton()
        btn.get_style_context().add_class('gpio-tb')
        btn.set_halign(Gtk.Align.START)
        btn.set_label(pin)
        btn.set_margin_start(5)
        btn.set_margin_top(5)
        btn.set_margin_end(5)
        btn.set_margin_bottom(5)
        if index % 2 == 0:
            gpioBottomRow.pack_start(btn, False, False, 0)
        else:
            gpioTopRow.pack_start(btn, False, False, 0) 
        btn.set_size_request(60, 60) 
        
        # other settings 
        if pin in rp_list.disabled_gpio:
            btn.get_style_context().add_class(pin.lower())
            
        if not pin in rp_list.disabled_gpio:
            btn.connect("toggled", on_gpio_toggle, 'D' + pin)
                    
        btn.show()
            
    # mainVbox items
    mainVbox.pack_start(gpiotxt, False, False, 100)
    hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)
    mainVbox.pack_start(hbox, False, False, 0)
    hbox.pack_start(secVbox, False, False, 0)
    hbox.set_halign(Gtk.Align.CENTER)
    hbox.set_margin_bottom(50)
    hbox.show()
    mainVbox.show()
    
    # hbox items
    secVbox.pack_start(gpioTopRow, False, False, 0)
    secVbox.pack_start(gpioBottomRow, False, False, 0)
    gpioBottomRow.set_margin_bottom(20)
    gpioTopRow.set_margin_start(25)
    gpioTopRow.set_margin_end(25)
    gpioTopRow.set_margin_top(25)
    secVbox.set_name("secVbox")
    secVbox.override_background_color(Gtk.StateType.NORMAL, Gdk.RGBA(.7, .7, .7, 1))
    gpioBottomRow.show()
    gpioTopRow.show()
    secVbox.show()
    scrolled_window.show()
    return scrolled_window



def on_gpio_toggle(button, pin_no):
    pin = digitalio.DigitalInOut(getattr(board, pin_no))
    pin.direction = digitalio.Direction.OUTPUT
    pin.value = 1 if button.get_active() else 0
    print('ok on/off')
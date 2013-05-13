claypellet
==========

Pebble application execution harness, aimed mostly at layout preview and basic
functionality prototyping.

The name comes from the fact that claypellet is more malleable than a Pebble
and also significatly less solid and robust.

This is very experimental at present. I have implemented just enough to a few
watchface apps running. If you need any help getting it working or have
suggestions for features, I generally hang out in #pebble on the freenode IRC
network.

License
-------

The code uses the MIT license. See the LICENSE file for details.

Most of the C code is pulled straight out of the Pebble SDK header files and
modified slightly to build the requisite CFFI hooks. Some of the resource
management code was reverse-engineered from the Pebble SDK resource packaging
tools. Also, the core of this is an implementation of a certain amount of the
Pebble application environment and API. Since the SDK apparently has no license
but is distributed freely to anyone with an account on
[developer.getpebble.com](http://developer.getpebble.com/), I'm assuming that
it's okay to use it like this.

Making it work
--------------

You'll need to have the [pebble SDK](http://developer.getpebble.com/)
installed. From there it gets a little hairy.

You'll need the current development branch of
[cffi](http://cffi.readthedocs.org/) -- a bug I discovered while getting this
project going has been fixed there but not in the v0.6, which is the current
release version at the time of writing.

You'll also need [pygame](http://pygame.org/) which I'm using for the display.

With all the dependencies installed, you should be able to run the following
commands in you project directory to get your app running in the simulator:

    /path/to/claypebble/compile_pebble_app.sh
    /path/to/claypebble/run_pebble_app.py

This assumes that you have a standard project layout with all the source files
in `src/*.c` and built files in `build/`.

If you're using OSX, you might need to drop a copy of `pebble_app.h` in the
current directory and modify it to change `((section (".pbl_header")))` into
`((section ("__DATA,.pbl_header")))`. (I had to do this, anyway. I haven't
tested on any other operating systems, so YMMV.)

How to use it
-------------

You can call `run_pebble_app.py -h` to get a list of parameters available. The
most exciting param (and the only one without a useful default) is `--firmware`
which allows you to specify a Pebble firmware file (perhaps acquired using some
[fine tools on the internet](https://github.com/xndcn/pebble-firmware-utils))
to read system fonts from. Without this, text using system fonts will not be
rendered.

Once you have your app running in claypebble, you can push some buttons on your
keyboard to make things happen.

  * `esc` or `q` to quit.
  * `r` to reload the app. You'll have to run `compile_pebble_app.sh` to
    recompile if you've made any changes.
  * `s` to take a screenshot. (Written to the current directory with a
    timestamped filename.)

TODO
----

There are a bunch of documented API functions still unimplemented:

  * All animation-related APIs.
  * A few graphics APIs, including paths, lines and pixels.
  * All "hardware" APIs: backlight, buttons, vibration.
  * Raw resource access.
  * Some miscellaneous functions here and there not mentioned above.

All documented functions have commented C function signatures in `harness.py`
so they should be fairly easy to find. All functions declared in `pebble_os.h`
have callback hooks defined and stub implementations in the generated C and
Python code. I've implemented a few undocumented API functions because some
apps I tried to run used them.

System font support requires a separate download of a Pebble firmware bundle.
There should probably be a fallback font (or set of fonts) for when this isn't
available, but for now we just give up and don't draw text with fonts we can't
find.

I haven't really decided how best to do button input, but binding to arrow keys
seems like a good plan. This hasn't been a priority since I've only been
testing with watchface apps and none of them use input of any kind.

Simulating communication seems like it'll be hard. Maybe someone else wants to
give that a go?

Bugs and issues
---------------

This project is very incomplete. I plan to add more functionality in whatever
direction strikes my fancy as and when I get around to it. Feel free to
contribute if there's something you particularly want it to do.

While I think the basic approach is reasonable for first-pass prototyping stuff
like layout tweaks, but claypellet will never be a replacement for actually
testing your code on the device. The CPU architecture and libc implementations
are just too different.

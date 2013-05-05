claypellet
==========

Pebble application execution harness, aimed mostly at layout preview.

This is very experimental at present. I have implemented just enough to get one
of my basic watchface apps working.

The name comes from the fact that claypellet is more malleable than a Pebble
and also significatly less solid and robust.

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

To compile your app into a library than can be loaded by claypellet, you need
to `./waf build` and then invoke something along the lines of the following:

    gcc -c -shared -std=c99 -I. -I./include -I./build -o libpeb.so src/thing.c

If you're using OSX, you might need to drop a copy of `pebble_app.h` in the
current directory and modify it to change `((section (".pbl_header")))` into
`((section ("__DATA,.pbl_header")))`. (I had to do this, anyway. I haven't
tested on any other operating systems, so YMMV.)

Bugs and issues
---------------

This project is very incomplete. I plan to add more functionality in whatever
direction strikes my fancy as and when I get around to it. Feel free to
contribute if there's something you particularly want it to do.

While I think the basic approach is reasonable for first-pass prototyping stuff
like layout tweaks, but claypellet will never be a replacement for actually
testing your code on the device. The CPU architecture and libc implementations
are just too different.

<h1>Comodi</h1>

<h2>About</h2>
<div>
	<p>Comodi is a program written in <strong>Python 3</strong> made with and for the Raspberry Pi. It uses a char LCD display, current support is only a 20x4 display, to display various amounts of information to the user.
	</p>

	<p>
	This is my first Python and Raspberry Pi project, feel free to help me out by forking this repository, reporting bugs and propose features to the program.
	</p>
</div>

<h2>Configure</h2>
<div>
<p>
Comodi requires the a working installation and configuration of <a href="http://lirc.org">LIRC</a> and <a href="http://www.pygame.org">PyGame</a>. More information about those products is on their websites. A full guide on how to get Comodi setup can be found <a href="https://github.com/Dreeass/Comodi-Python/wiki/Setting-up-Comodi">here</a>.
</p>

The following keys need to be configured in LIRC for Comodi to work as desired:
<dl>
<dt>KEY_POWER</dt>
	<dd>Turn display on/off.</dd>
<dt>KEY_1</dt>
	<dd>Switch to menu 1.</dd>
<dt>KEY_2</dt>
	<dd>Switch to menu 2.</dd>
<dt>KEY_3</dt>
	<dd>Switch to menu 3.</dd>
<dt>KEY_PREVIOUSSONG</dt>
	<dd>Go to the previous song or rewind song.</dd>
<dt>KEY_PLAYPAUSE</dt>
	<dd>Play or pause the song.</dd>
<dt>KEY_NEXTSONG</dt>
	<dd>Go to the next song.</dd>
<dt>KEY_VOLUMEDOWN</dt>
	<dd>Lower the volume, min. 0.</dd>
<dt>KEY_VOLUMEUP</dt>
	<dd>Turn the volume up, max. 10.</dd>
<dt>KEY_PROG1</dt>
	<dd>Enable alarm 1.</dd>
<dt>KEY_PROG2</dt>
	<dd>Enable alarm 2.</dd>
</dl>

</div>

<h2>License</h2>

<div>
<p>
Python program for the Raspberry Pi to make use of char LCD display.<br />
Copyright (C) 2013  Andreas Backx
</p>

<p>
This program is free software: you can redistribute it and/or modify<br />
it under the terms of the GNU General Pubdtc dtcense as pubdtshed by<br />
the Free Software Foundation, either version 3 of the dtcense, or<br />
(at your option) any later version.
</p>

<p>
This program is distributed in the hope that it will be useful,<br />
but WITHOUT ANY WARRANTY; without even the impdted warranty of<br />
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the<br />
GNU General Pubdtc dtcense for more details.
</p>

<p>
You should have received a copy of the GNU General Pubdtc dtcense<br />
along with this program.  If not, see <a>http://www.gnu.org/dtcenses/</a>.
</p>
</div>

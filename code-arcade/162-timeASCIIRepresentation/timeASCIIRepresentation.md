<p>John has always liked analog clocks more than digital ones. He's been dreaming about turning his digital clock into an analog one for as long as he can remember, and now he met you, a great programmer, so his dream is about to come true.</p>
<p>The screen of his digital clock is a simple <code>17 × 17</code> rectangle of pixels. It always shows four digits: the first two stand for hours and second two for minutes (John's clock uses the 24-hour format). Each digit is located in a <code>17 × 4</code> rectangle, with the leftmost column always empty, and the other three columns filled according to this pattern with the proper scaling:</p>
<p><img src="https://codesignal.s3.amazonaws.com/tasks/timeASCIIRepresentation/img/digits.png?_tm=1624642316915" alt /></p>
<p>After the first two digits there is a separating column containing one symbol <code>':'</code> at its center.</p>
<p>Now John asks you to make his clock show time in the format similar to analog clocks. Here's how: an analog clock can be represented as a circle (the clock's borders) and two segments (the clock's hands). To show it on the <code>17 × 17</code> screen, you should light the pixels on it so that the pixel with coordinates <code>(x, y)</code> is enabled if and only if the minimal distance to the circle or one of the segments is less than <code>sqrt(0.5)</code>.</p>
<p>John wants you to implement the function that changes the digital representation to the analog one as described above. Given a <code>17 × 17</code> rectangle <code>dtime</code> representing digital time representation, return the analog representation of the same time.</p>
<p>Please note that for the early prototype you have to develop, both of the clock's hands should have the same length.</p>
<p><span class="markdown--header" style="color:#2b3b52;font-size:1.4em">Example</span></p>
<p>For</p>
<pre><code>
dtime = [
  ['.', <b><font color="red">'*'</font></b>, <b><font color="red">'*'</font></b>, <b><font color="red">'*'</font></b>, '.', '.', <b><font color="red">'*'</font></b>, '.', '.', '.', <b><font color="red">'*'</font></b>, <b><font color="red">'*'</font></b>, <b><font color="red">'*'</font></b>, '.', <b><font color="red">'*'</font></b>, <b><font color="red">'*'</font></b>, <b><font color="red">'*'</font></b>],
  ['.', <b><font color="red">'*'</font></b>, '.', <b><font color="red">'*'</font></b>, '.', '.', <b><font color="red">'*'</font></b>, '.', '.', '.', '.', '.', <b><font color="red">'*'</font></b>, '.', <b><font color="red">'*'</font></b>, '.', <b><font color="red">'*'</font></b>],
  ['.', <b><font color="red">'*'</font></b>, '.', <b><font color="red">'*'</font></b>, '.', '.', <b><font color="red">'*'</font></b>, '.', '.', '.', '.', '.', <b><font color="red">'*'</font></b>, '.', <b><font color="red">'*'</font></b>, '.', <b><font color="red">'*'</font></b>],
  ['.', <b><font color="red">'*'</font></b>, '.', <b><font color="red">'*'</font></b>, '.', '.', <b><font color="red">'*'</font></b>, '.', '.', '.', '.', '.', <b><font color="red">'*'</font></b>, '.', <b><font color="red">'*'</font></b>, '.', <b><font color="red">'*'</font></b>],
  ['.', <b><font color="red">'*'</font></b>, '.', <b><font color="red">'*'</font></b>, '.', '.', <b><font color="red">'*'</font></b>, '.', '.', '.', '.', '.', <b><font color="red">'*'</font></b>, '.', <b><font color="red">'*'</font></b>, '.', <b><font color="red">'*'</font></b>],
  ['.', <b><font color="red">'*'</font></b>, '.', <b><font color="red">'*'</font></b>, '.', '.', <b><font color="red">'*'</font></b>, '.', '.', '.', '.', '.', <b><font color="red">'*'</font></b>, '.', <b><font color="red">'*'</font></b>, '.', <b><font color="red">'*'</font></b>],
  ['.', <b><font color="red">'*'</font></b>, '.', <b><font color="red">'*'</font></b>, '.', '.', <b><font color="red">'*'</font></b>, '.', '.', '.', '.', '.', <b><font color="red">'*'</font></b>, '.', <b><font color="red">'*'</font></b>, '.', <b><font color="red">'*'</font></b>],
  ['.', <b><font color="red">'*'</font></b>, '.', <b><font color="red">'*'</font></b>, '.', '.', <b><font color="red">'*'</font></b>, '.', '.', '.', '.', '.', <b><font color="red">'*'</font></b>, '.', <b><font color="red">'*'</font></b>, '.', <b><font color="red">'*'</font></b>],
  ['.', <b><font color="red">'*'</font></b>, '.', <b><font color="red">'*'</font></b>, '.', '.', <b><font color="red">'*'</font></b>, '.', <b><font color="red">':'</font></b>, '.', <b><font color="red">'*'</font></b>, <b><font color="red">'*'</font></b>, <b><font color="red">'*'</font></b>, '.', <b><font color="red">'*'</font></b>, '.', <b><font color="red">'*'</font></b>],
  ['.', <b><font color="red">'*'</font></b>, '.', <b><font color="red">'*'</font></b>, '.', '.', <b><font color="red">'*'</font></b>, '.', '.', '.', '.', '.', <b><font color="red">'*'</font></b>, '.', <b><font color="red">'*'</font></b>, '.', <b><font color="red">'*'</font></b>],
  ['.', <b><font color="red">'*'</font></b>, '.', <b><font color="red">'*'</font></b>, '.', '.', <b><font color="red">'*'</font></b>, '.', '.', '.', '.', '.', <b><font color="red">'*'</font></b>, '.', <b><font color="red">'*'</font></b>, '.', <b><font color="red">'*'</font></b>],
  ['.', <b><font color="red">'*'</font></b>, '.', <b><font color="red">'*'</font></b>, '.', '.', <b><font color="red">'*'</font></b>, '.', '.', '.', '.', '.', <b><font color="red">'*'</font></b>, '.', <b><font color="red">'*'</font></b>, '.', <b><font color="red">'*'</font></b>],
  ['.', <b><font color="red">'*'</font></b>, '.', <b><font color="red">'*'</font></b>, '.', '.', <b><font color="red">'*'</font></b>, '.', '.', '.', '.', '.', <b><font color="red">'*'</font></b>, '.', <b><font color="red">'*'</font></b>, '.', <b><font color="red">'*'</font></b>],
  ['.', <b><font color="red">'*'</font></b>, '.', <b><font color="red">'*'</font></b>, '.', '.', <b><font color="red">'*'</font></b>, '.', '.', '.', '.', '.', <b><font color="red">'*'</font></b>, '.', <b><font color="red">'*'</font></b>, '.', <b><font color="red">'*'</font></b>],
  ['.', <b><font color="red">'*'</font></b>, '.', <b><font color="red">'*'</font></b>, '.', '.', <b><font color="red">'*'</font></b>, '.', '.', '.', '.', '.', <b><font color="red">'*'</font></b>, '.', <b><font color="red">'*'</font></b>, '.', <b><font color="red">'*'</font></b>],
  ['.', <b><font color="red">'*'</font></b>, '.', <b><font color="red">'*'</font></b>, '.', '.', <b><font color="red">'*'</font></b>, '.', '.', '.', '.', '.', <b><font color="red">'*'</font></b>, '.', <b><font color="red">'*'</font></b>, '.', <b><font color="red">'*'</font></b>],
  ['.', <b><font color="red">'*'</font></b>, <b><font color="red">'*'</font></b>, <b><font color="red">'*'</font></b>, '.', '.', <b><font color="red">'*'</font></b>, '.', '.', '.', <b><font color="red">'*'</font></b>, <b><font color="red">'*'</font></b>, <b><font color="red">'*'</font></b>, '.', <b><font color="red">'*'</font></b>, <b><font color="red">'*'</font></b>, <b><font color="red">'*'</font></b>]
]
</code></pre>
<p>the output should be</p>
<pre><code>
solution(dtime) = [
  ['.', '.', '.', '.', <b><font color="red">'*'</font></b>, <b><font color="red">'*'</font></b>, <b><font color="red">'*'</font></b>, <b><font color="red">'*'</font></b>, <b><font color="red">'*'</font></b>, <b><font color="red">'*'</font></b>, <b><font color="red">'*'</font></b>, <b><font color="red">'*'</font></b>, <b><font color="red">'*'</font></b>, '.', '.', '.', '.'],
  ['.', '.', '.', <b><font color="red">'*'</font></b>, <b><font color="red">'*'</font></b>, '.', '.', '.', '.', '.', '.', '.', <b><font color="red">'*'</font></b>, <b><font color="red">'*'</font></b>, '.', '.', '.'],
  ['.', '.', <b><font color="red">'*'</font></b>, <b><font color="red">'*'</font></b>, '.', '.', '.', '.', '.', '.', '.', '.', '.', <b><font color="red">'*'</font></b>, <b><font color="red">'*'</font></b>, '.', '.'],
  ['.', <b><font color="red">'*'</font></b>, <b><font color="red">'*'</font></b>, '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', <b><font color="red">'*'</font></b>, <b><font color="red">'*'</font></b>, <b><font color="red">'*'</font></b>, '.'],
  [<b><font color="red">'*'</font></b>, <b><font color="red">'*'</font></b>, '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', <b><font color="red">'*'</font></b>, '.', '.', <b><font color="red">'*'</font></b>, <b><font color="red">'*'</font></b>],
  [<b><font color="red">'*'</font></b>, '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', <b><font color="red">'*'</font></b>, '.', '.', '.', '.', <b><font color="red">'*'</font></b>],
  [<b><font color="red">'*'</font></b>, '.', '.', '.', '.', '.', '.', '.', '.', '.', <b><font color="red">'*'</font></b>, '.', '.', '.', '.', '.', <b><font color="red">'*'</font></b>],
  [<b><font color="red">'*'</font></b>, '.', '.', '.', '.', '.', '.', '.', '.', <b><font color="red">'*'</font></b>, '.', '.', '.', '.', '.', '.', <b><font color="red">'*'</font></b>],
  [<b><font color="red">'*'</font></b>, '.', '.', '.', '.', '.', '.', '.', <b><font color="red">'*'</font></b>, '.', '.', '.', '.', '.', '.', '.', <b><font color="red">'*'</font></b>],
  [<b><font color="red">'*'</font></b>, '.', '.', '.', '.', '.', '.', '.', <b><font color="red">'*'</font></b>, '.', '.', '.', '.', '.', '.', '.', <b><font color="red">'*'</font></b>],
  [<b><font color="red">'*'</font></b>, '.', '.', '.', '.', '.', '.', '.', <b><font color="red">'*'</font></b>, '.', '.', '.', '.', '.', '.', '.', <b><font color="red">'*'</font></b>],
  [<b><font color="red">'*'</font></b>, '.', '.', '.', '.', '.', '.', '.', <b><font color="red">'*'</font></b>, '.', '.', '.', '.', '.', '.', '.', <b><font color="red">'*'</font></b>],
  [<b><font color="red">'*'</font></b>, <b><font color="red">'*'</font></b>, '.', '.', '.', '.', '.', '.', <b><font color="red">'*'</font></b>, '.', '.', '.', '.', '.', '.', <b><font color="red">'*'</font></b>, <b><font color="red">'*'</font></b>],
  ['.', <b><font color="red">'*'</font></b>, <b><font color="red">'*'</font></b>, '.', '.', '.', '.', '.', <b><font color="red">'*'</font></b>, '.', '.', '.', '.', '.', <b><font color="red">'*'</font></b>, <b><font color="red">'*'</font></b>, '.'],
  ['.', '.', <b><font color="red">'*'</font></b>, <b><font color="red">'*'</font></b>, '.', '.', '.', '.', <b><font color="red">'*'</font></b>, '.', '.', '.', '.', <b><font color="red">'*'</font></b>, <b><font color="red">'*'</font></b>, '.', '.'],
  ['.', '.', '.', <b><font color="red">'*'</font></b>, <b><font color="red">'*'</font></b>, '.', '.', '.', <b><font color="red">'*'</font></b>, '.', '.', '.', <b><font color="red">'*'</font></b>, <b><font color="red">'*'</font></b>, '.', '.', '.'],
  ['.', '.', '.', '.', <b><font color="red">'*'</font></b>, <b><font color="red">'*'</font></b>, <b><font color="red">'*'</font></b>, <b><font color="red">'*'</font></b>, <b><font color="red">'*'</font></b>, <b><font color="red">'*'</font></b>, <b><font color="red">'*'</font></b>, <b><font color="red">'*'</font></b>, <b><font color="red">'*'</font></b>, '.', '.', '.', '.']
]
</code></pre>
<p>(Enabled pixels are painted red to make them more visible).</p>
<p>Here is the geometrical representation of an analog clock showing time <code>01:30</code>. Enabled pixel are painted red.</p>
<p><img src="https://codesignal.s3.amazonaws.com/tasks/timeASCIIRepresentation/img/example.png?_tm=1624642317217" alt /></p>
<p><span class="markdown--header" style="color:#2b3b52;font-size:1.4em">Input/Output</span></p>
<ul>
<li>
<p><strong>[execution time limit] 4 seconds (py3)</strong></p>
</li>
<li>
<p><strong>[input] array.array.char dtime</strong></p>
<p>Digital time representation, where <code>dtime[x][y]</code> is equal to <code>'*'</code> if the pixel with coordinates <code>(x, y)</code> is enabled and <code>'.'</code> otherwise. It is guaranteed that the given time is correct, and that <code>dtime[8][8] = ':'</code>.</p>
<p><em>Guaranteed constraints:</em><br />
<code>dtime.length = 17</code>,<br />
<code>dtime[i].length = 17</code>.</p>
</li>
<li>
<p><strong>[output] array.array.char</strong></p>
<p>Representation of the same time on the same rectangle, but in an analog clock format.</p>
</li>
</ul>
<p><strong>[Python 3] Syntax Tips</strong></p>
<pre><code class="language-python"><span class="hljs-comment"># Prints help message to the console</span>
<span class="hljs-comment"># Returns a string</span>
<span class="hljs-keyword">def</span> <span class="hljs-title function_">helloWorld</span>(<span class="hljs-params">name</span>):
    <span class="hljs-built_in">print</span>(<span class="hljs-string">"This prints to the console when you Run Tests"</span>)
    <span class="hljs-keyword">return</span> <span class="hljs-string">"Hello, "</span> + name

</code></pre>

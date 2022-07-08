<p>You are implementing a command-line version of the Paint app. Since the command line doesn't support colors, you are using different characters to represent pixels. Your current goal is to support <code>rectangle x1 y1 x2 y2</code> operation, which draws a rectangle that has an upper left corner at <code>(x1, y1)</code> and a lower right corner at <code>(x2, y2)</code>. Here the <code>x</code>-axis points from left to right, and the <code>y</code>-axis points from top to bottom.</p>
<p>Given the initial canvas state and the array that represents the coordinates of the two corners, return the canvas state after the operation is applied. For the details about how rectangles are painted, see the example.</p>
<p><span class="markdown--header" style="color:#2b3b52;font-size:1.4em">Example</span></p>
<p>For</p>
<pre><code>canvas = [['a', 'a', 'a', 'a', 'a', 'a', 'a', 'a'],
          ['a', 'a', 'a', 'a', 'a', 'a', 'a', 'a'],
          ['a', 'a', 'a', 'a', 'a', 'a', 'a', 'a'],
          ['b', 'b', 'b', 'b', 'b', 'b', 'b', 'b'],
          ['b', 'b', 'b', 'b', 'b', 'b', 'b', 'b']]
</code></pre>
<p>and <code>rectangle = [1, 1, 4, 3]</code>, the output should be</p>
<pre><code>solution(canvas, rectangle) = [['a', 'a', 'a', 'a', 'a', 'a', 'a', 'a'],
                  					['a', '*', '-', '-', '*', 'a', 'a', 'a'],
                  					['a', '|', 'a', 'a', '|', 'a', 'a', 'a'],
                  					['b', '*', '-', '-', '*', 'b', 'b', 'b'],
                  					['b', 'b', 'b', 'b', 'b', 'b', 'b', 'b']]
</code></pre>
<p>Here is the rectangle, colored for illustration:</p>
<pre><code>
[['a', 'a', 'a', 'a', 'a', 'a', 'a', 'a'],
['a', <b><font color="red">'*'</font></b>, <b><font color="red">'-'</font></b>, <b><font color="red">'-'</font></b>, <b><font color="red">'*'</font></b>, 'a', 'a', 'a'],
['a', <b><font color="red">'|'</font></b>, 'a', 'a', <b><font color="red">'|'</font></b>, 'a', 'a', 'a'],
['b', <b><font color="red">'*'</font></b>, <b><font color="red">'-'</font></b>, <b><font color="red">'-'</font></b>, <b><font color="red">'*'</font></b>, 'b', 'b', 'b'],
['b', 'b', 'b', 'b', 'b', 'b', 'b', 'b']]
</code></pre>
<p>Note that rectangle sides are depicted as <code>-</code>s and <code>|</code>s, asterisks (<code>*</code>) stand for its corners and all of the other "pixels" remain the same.</p>
<p><span class="markdown--header" style="color:#2b3b52;font-size:1.4em">Input/Output</span></p>
<ul>
<li>
<p><strong>[execution time limit] 4 seconds (py3)</strong></p>
</li>
<li>
<p><strong>[input] array.array.char canvas</strong></p>
<p>A non-empty rectangular matrix of characters.</p>
<p><em>Guaranteed constraints:</em><br />
<code>2 ≤ canvas.length ≤ 10</code>,<br />
<code>2 ≤ canvas[0].length ≤ 10</code>.</p>
</li>
<li>
<p><strong>[input] array.integer rectangle</strong></p>
<p>Array of four integers - <code>[x1, y1, x2, y2]</code>.</p>
<p><em>Guaranteed constraints:</em><br />
<code>0 ≤ x1 &lt; x2 &lt; canvas[i].length</code>,<br />
<code>0 ≤ y1 &lt; y2 &lt; canvas.length</code>.</p>
</li>
<li>
<p><strong>[output] array.array.char</strong></p>
</li>
</ul>
<p><strong>[Python 3] Syntax Tips</strong></p>
<pre><code class="language-python"><span class="hljs-comment"># Prints help message to the console</span>
<span class="hljs-comment"># Returns a string</span>
<span class="hljs-keyword">def</span> <span class="hljs-title function_">helloWorld</span>(<span class="hljs-params">name</span>):
    <span class="hljs-built_in">print</span>(<span class="hljs-string">"This prints to the console when you Run Tests"</span>)
    <span class="hljs-keyword">return</span> <span class="hljs-string">"Hello, "</span> + name

</code></pre>

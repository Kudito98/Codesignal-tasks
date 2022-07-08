<p>Little Ratiorg was tired of being bullied by other bots and mighty CodeFighters, so he joined the Ninja Bots Training camp. Any bot that manages to solve all the challenges becomes an ultimate master of algorithms, and that is exactly what Ratiorg wants.</p>
<p>Ratiorg aced the very first challenge, and is ready to begin the second. The little bot is given a <code>canvas</code>, each pixel of which has some color. Ratiorg should apply several <em>flood fill</em> <code>operations</code> to the canvas, and show the resulting image to the judges. Each <em>flood fill</em> operation is given as an array of three elements <code>[x, y, color]</code>, where <code>(x, y)</code> is the coordinates of the pixel to which the operation is applied, and <code>color</code> is the color with which the pixel and its area should be painted. The area that should be painted along with the initial pixel is defined as follows:</p>
<ul>
<li>Initially, only the pixel to which the operation was applied should be painted.</li>
<li>Consider all pixels that are adjacent to the initial one (i.e. directly above, below, to the left or to the right of it). If the difference between the color of this pixel and the color of the initial one is not greater than <code>d</code>, this pixel should also be painted.
<ul>
<li>For each pixel painted on this step consider all its neighbors in the same manner.</li>
</ul>
</li>
</ul>
<p>Your task is to help the judges check Ratiorg's performance. Given <code>canvas</code>, <code>operations</code> and the value of <code>d</code>, return the state of the image after all operations have been applied.</p>
<p><span class="markdown--header" style="color:#2b3b52;font-size:1.4em">Example</span></p>
<p>For</p>
<pre><code>canvas = [[0, 1, 5, 2, 4, 2, 6],
          [5, 2, 4, 6, 2, 0, 0],
          [3, 3, 3, 7, 8, 3, 2],
          [2, 1, 1, 0, 0, 0, 0]]
</code></pre>
<p><code>operations = [[0, 0, 10], [1, 3, 3]]</code>, and <code>d = 3</code>,<br />
the output should be</p>
<pre><code>solution(canvas, operations, d) = [[10, 10,  3,  2,  4, 10, 6 ],
                                     [ 5, 10,  3,  3, 10, 10, 10],
                                     [10, 10, 10,  3,  3, 10, 10],
                                     [10, 10, 10, 10, 10, 10, 10]]
</code></pre>
<p>Here's how the canvas should be painted:<br />
<img src="https://codesignal.s3.amazonaws.com/tasks/painterBot/img/example.png?_tm=1624663146990" alt /></p>
<p><span class="markdown--header" style="color:#2b3b52;font-size:1.4em">Input/Output</span></p>
<ul>
<li>
<p><strong>[execution time limit] 19 seconds (py3)</strong></p>
</li>
<li>
<p><strong>[input] array.array.integer canvas</strong></p>
<p>A rectangular matrix representing the canvas.</p>
<p><em>Guaranteed constraints:</em><br />
<code>1 ≤ canvas.length ≤ 100</code>,<br />
<code>1 ≤ canvas[0].length ≤ 100</code>,<br />
<code>0 ≤ canvas[i][j] ≤ 255</code>.</p>
</li>
<li>
<p><strong>[input] array.array.integer operations</strong></p>
<p>Operations to be performed. Each operation is given in the format <code>[x, y, color]</code>, where <code>(x, y)</code> is the coordinates of the initial pixes (0-based indices of row and column, respectively) and <code>color</code> is the fill color.</p>
<p><em>Guaranteed constraints:</em><br />
<code>0 ≤ operations.length ≤ 100</code>,<br />
<code>operations[i].length = 3</code>,<br />
<code>0 ≤ operations[i][0] &lt; canvas.length</code>,<br />
<code>0 ≤ operations[i][1] &lt; canvas[0].length</code>,<br />
<code>0 ≤ operations[i][2] ≤ 255</code>.</p>
</li>
<li>
<p><strong>[input] integer d</strong></p>
<p>The value that defines the <em>flood fill</em> area.</p>
<p><em>Guaranteed constraints:</em><br />
<code>0 ≤ d ≤ 255</code>.</p>
</li>
<li>
<p><strong>[output] array.array.integer</strong></p>
<p>The final state of the canvas.</p>
</li>
</ul>
<p><strong>[Python 3] Syntax Tips</strong></p>
<pre><code class="language-python"><span class="hljs-comment"># Prints help message to the console</span>
<span class="hljs-comment"># Returns a string</span>
<span class="hljs-keyword">def</span> <span class="hljs-title function_">helloWorld</span>(<span class="hljs-params">name</span>):
    <span class="hljs-built_in">print</span>(<span class="hljs-string">"This prints to the console when you Run Tests"</span>)
    <span class="hljs-keyword">return</span> <span class="hljs-string">"Hello, "</span> + name

</code></pre>

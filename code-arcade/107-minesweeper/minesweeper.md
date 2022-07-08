<p>In the popular <strong>Minesweeper</strong> game you have a board with some mines and those cells that don't contain a mine have a number in it that indicates the total number of mines in the neighboring cells. Starting off with some arrangement of mines we want to create a <strong>Minesweeper</strong> game setup.</p>
<p><span class="markdown--header" style="color:#2b3b52;font-size:1.4em">Example</span></p>
<p>For</p>
<pre><code>matrix = [[true, false, false],
          [false, true, false],
          [false, false, false]]
</code></pre>
<p>the output should be</p>
<pre><code>solution(matrix) = [[1, 2, 1],
                       [2, 1, 1],
                       [1, 1, 1]]
</code></pre>
<p>Check out the image below for better understanding:</p>
<p><img src="https://codesignal.s3.amazonaws.com/tasks/minesweeper/img/example.png?_tm=1624662247096" alt /></p>
<p><span class="markdown--header" style="color:#2b3b52;font-size:1.4em">Input/Output</span></p>
<ul>
<li>
<p><strong>[execution time limit] 4 seconds (py3)</strong></p>
</li>
<li>
<p><strong>[input] array.array.boolean matrix</strong></p>
<p>A non-empty rectangular matrix consisting of boolean values - <code>true</code> if the corresponding cell contains a mine, <code>false</code> otherwise.</p>
<p><em>Guaranteed constraints:</em><br />
<code>2 ≤ matrix.length ≤ 100</code>,<br />
<code>2 ≤ matrix[0].length ≤ 100</code>.</p>
</li>
<li>
<p><strong>[output] array.array.integer</strong></p>
<p>Rectangular matrix of the same size as <code>matrix</code> each cell of which contains an integer equal to the number of mines in the neighboring cells. Two cells are called neighboring if they share at least one corner.</p>
</li>
</ul>
<p><strong>[Python 3] Syntax Tips</strong></p>
<pre><code class="language-python"><span class="hljs-comment"># Prints help message to the console</span>
<span class="hljs-comment"># Returns a string</span>
<span class="hljs-keyword">def</span> <span class="hljs-title function_">helloWorld</span>(<span class="hljs-params">name</span>):
    <span class="hljs-built_in">print</span>(<span class="hljs-string">"This prints to the console when you Run Tests"</span>)
    <span class="hljs-keyword">return</span> <span class="hljs-string">"Hello, "</span> + name

</code></pre>

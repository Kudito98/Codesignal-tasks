<p>Imagine a white rectangular grid of <code>n</code> rows and <code>m</code> columns divided into two parts by a diagonal line running from the upper left to the lower right corner. Now let's paint the grid in two colors according to the following rules:</p>
<ul>
<li>A cell is painted black if it has at least one point in common with the diagonal;</li>
<li>Otherwise, a cell is painted white.</li>
</ul>
<p>Count the number of cells painted black.</p>
<p><span class="markdown--header" style="color:#2b3b52;font-size:1.4em">Example</span></p>
<ul>
<li>
<p>For <code>n = 3</code> and <code>m = 4</code>, the output should be<br />
<code>solution(n, m) = 6</code>.</p>
<p>There are <code>6</code> cells that have at least one common point with the diagonal and therefore are painted black.</p>
<p><img src="https://codesignal.s3.amazonaws.com/tasks/countBlackCells/img/example1.jpg?_tm=1583178294051" alt /></p>
</li>
<li>
<p>For <code>n = 3</code> and <code>m = 3</code>, the output should be<br />
<code>solution(n, m) = 7</code>.</p>
<p><code>7</code> cells have at least one common point with the diagonal and are painted black.</p>
<p><img src="https://codesignal.s3.amazonaws.com/tasks/countBlackCells/img/example2.jpg?_tm=1583178294302" alt /></p>
</li>
</ul>
<p><span class="markdown--header" style="color:#2b3b52;font-size:1.4em">Input/Output</span></p>
<ul>
<li>
<p><strong>[execution time limit] 4 seconds (py3)</strong></p>
</li>
<li>
<p><strong>[input] integer n</strong></p>
<p>The number of rows.</p>
<p><em>Guaranteed constraints:</em><br />
<code>1 ≤ n ≤ 10<sup>5</sup></code>.</p>
</li>
<li>
<p><strong>[input] integer m</strong></p>
<p>The number of columns.</p>
<p><em>Guaranteed constraints:</em><br />
<code>1 ≤ m ≤ 10<sup>5</sup></code>.</p>
</li>
<li>
<p><strong>[output] integer</strong></p>
<p>The number of black cells.</p>
</li>
</ul>
<p><strong>[Python 3] Syntax Tips</strong></p>
<pre><code class="language-python"><span class="hljs-comment"># Prints help message to the console</span>
<span class="hljs-comment"># Returns a string</span>
<span class="hljs-keyword">def</span> <span class="hljs-title function_">helloWorld</span>(<span class="hljs-params">name</span>):
    <span class="hljs-built_in">print</span>(<span class="hljs-string">"This prints to the console when you Run Tests"</span>)
    <span class="hljs-keyword">return</span> <span class="hljs-string">"Hello, "</span> + name

</code></pre>

<p>Given a rectangular matrix and an integer <code>column</code>, return an array containing the elements of the <code>column<sup>th</sup></code> column of the given matrix (the leftmost column is the <code>0<sup>th</sup></code> one).</p>
<p><strong>Example</strong></p>
<p>For</p>
<pre><code>matrix = [[1, 1, 1, 2], 
          [0, 5, 0, 4], 
          [2, 1, 3, 6]]
</code></pre>
<p>and <code>column = 2</code>, the output should be<br />
<code>solution(matrix, column) = [1, 0, 3]</code>.</p>
<p><span class="markdown--header" style="color:#2b3b52;font-size:1.4em">Input/Output</span></p>
<ul>
<li>
<p><strong>[execution time limit] 4 seconds (py3)</strong></p>
</li>
<li>
<p><strong>[input] array.array.integer matrix</strong></p>
<p>2-dimensional array of integers representing a rectangular matrix.</p>
<p><em>Guaranteed constraints:</em><br />
<code>1 ≤ matrix.length ≤ 500</code>,<br />
<code>1 ≤ matrix[i].length ≤ 500</code>,<br />
<code>0 ≤ matrix[i][j] ≤ 10<sup>5</sup></code>.</p>
</li>
<li>
<p><strong>[input] integer column</strong></p>
<p>An integer not greater than the number of <code>matrix</code> columns.</p>
<p><em>Guaranteed constraints:</em><br />
<code>0 ≤ column ≤ matrix[i].length - 1</code>.</p>
</li>
<li>
<p><strong>[output] array.integer</strong></p>
</li>
</ul>
<p><strong>[Python 3] Syntax Tips</strong></p>
<pre><code class="language-python"><span class="hljs-comment"># Prints help message to the console</span>
<span class="hljs-comment"># Returns a string</span>
<span class="hljs-keyword">def</span> <span class="hljs-title function_">helloWorld</span>(<span class="hljs-params">name</span>):
    <span class="hljs-built_in">print</span>(<span class="hljs-string">"This prints to the console when you Run Tests"</span>)
    <span class="hljs-keyword">return</span> <span class="hljs-string">"Hello, "</span> + name

</code></pre>

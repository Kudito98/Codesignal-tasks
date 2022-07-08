<p>Given a rectangular matrix and integers <code>a</code> and <code>b</code>, consider the union of the <em>a<sup>th</sup></em> row and the <em>b<sup>th</sup></em> (both <em>0-based</em>) column of the matrix (i.e. all cells that belong either to the <em>a<sup>th</sup></em> row or to the <em>b<sup>th</sup></em> column, or to both). Return sum of all elements of that union.</p>
<p><strong>Example</strong></p>
<p>For</p>
<pre><code>matrix = [[1, 1, 1, 1], 
          [2, 2, 2, 2], 
          [3, 3, 3, 3]]
</code></pre>
<p><code>a = 1</code>, and <code>b = 3</code>, the output should be<br />
<code>solution(matrix, a, b) = 12</code>.</p>
<p>Here <code>(2 + 2 + 2 + 2) + (1 + 3) = 12</code>.</p>
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
<code>1 ≤ matrix[0].length ≤ 500</code>,<br />
<code>1 ≤ matrix[i][j] ≤ 10<sup>5</sup></code>.</p>
</li>
<li>
<p><strong>[input] integer a</strong></p>
<p>A non-negative integer less than the number of matrix rows.</p>
<p><em>Guaranteed constraints:</em><br />
<code>0 ≤ a &lt; matrix.length</code>.</p>
</li>
<li>
<p><strong>[input] integer b</strong></p>
<p>A non-negative integer less than the number of matrix columns.</p>
<p><em>Guaranteed constraints:</em><br />
<code>0 ≤ b &lt; matrix[i].length</code>.</p>
</li>
<li>
<p><strong>[output] integer</strong></p>
</li>
</ul>
<p><strong>[Python 3] Syntax Tips</strong></p>
<pre><code class="language-python"><span class="hljs-comment"># Prints help message to the console</span>
<span class="hljs-comment"># Returns a string</span>
<span class="hljs-keyword">def</span> <span class="hljs-title function_">helloWorld</span>(<span class="hljs-params">name</span>):
    <span class="hljs-built_in">print</span>(<span class="hljs-string">"This prints to the console when you Run Tests"</span>)
    <span class="hljs-keyword">return</span> <span class="hljs-string">"Hello, "</span> + name

</code></pre>

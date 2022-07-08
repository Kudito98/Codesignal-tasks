<p>Given a rectangular matrix of integers, check if it is possible to rearrange its rows in such a way that all its columns become strictly increasing sequences (read from top to bottom).</p>
<p><span class="markdown--header" style="color:#2b3b52;font-size:1.4em">Example</span></p>
<ul>
<li>
<p>For</p>
<pre><code>matrix = [[2, 7, 1], 
          [0, 2, 0], 
          [1, 3, 1]]
</code></pre>
<p>the output should be<br />
<code>solution(matrix) = false</code>;</p>
</li>
<li>
<p>For</p>
<pre><code>matrix = [[6, 4], 
          [2, 2], 
          [4, 3]]
</code></pre>
<p>the output should be<br />
<code>solution(matrix) = true</code>.</p>
</li>
</ul>
<p><span class="markdown--header" style="color:#2b3b52;font-size:1.4em">Input/Output</span></p>
<ul>
<li>
<p><strong>[execution time limit] 4 seconds (py3)</strong></p>
</li>
<li>
<p><strong>[input] array.array.integer matrix</strong></p>
<p>A 2-dimensional array of integers.</p>
<p><em>Guaranteed constraints:</em><br />
<code>1 ≤ matrix.length ≤ 10</code>,<br />
<code>1 ≤ matrix[0].length ≤ 10</code>,<br />
<code>-300 ≤ matrix[i][j] ≤ 300</code>.</p>
</li>
<li>
<p><strong>[output] boolean</strong></p>
</li>
</ul>
<p><strong>[Python 3] Syntax Tips</strong></p>
<pre><code class="language-python"><span class="hljs-comment"># Prints help message to the console</span>
<span class="hljs-comment"># Returns a string</span>
<span class="hljs-keyword">def</span> <span class="hljs-title function_">helloWorld</span>(<span class="hljs-params">name</span>):
    <span class="hljs-built_in">print</span>(<span class="hljs-string">"This prints to the console when you Run Tests"</span>)
    <span class="hljs-keyword">return</span> <span class="hljs-string">"Hello, "</span> + name

</code></pre>

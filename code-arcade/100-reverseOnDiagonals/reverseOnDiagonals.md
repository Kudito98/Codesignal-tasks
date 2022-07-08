<p>The <em>longest diagonals</em> of a square matrix are defined as follows:</p>
<ul>
<li>the first <em>longest diagonal</em> goes from the top left corner to the bottom right one;</li>
<li>the second <em>longest diagonal</em> goes from the top right corner to the bottom left one.</li>
</ul>
<p>Given a square matrix, your task is to reverse the order of elements on both of its <em>longest diagonals</em>.</p>
<p><span class="markdown--header" style="color:#2b3b52;font-size:1.4em">Example</span></p>
<p>For</p>
<pre><code>matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]
</code></pre>
<p>the output should be</p>
<pre><code>solution(matrix) = [[9, 2, 7],
                              [4, 5, 6],
                              [3, 8, 1]]
</code></pre>
<p><span class="markdown--header" style="color:#2b3b52;font-size:1.4em">Input/Output</span></p>
<ul>
<li>
<p><strong>[execution time limit] 4 seconds (py3)</strong></p>
</li>
<li>
<p><strong>[input] array.array.integer matrix</strong></p>
<p><em>Guaranteed constraints:</em><br />
<code>1 ≤ matrix.length ≤ 100</code>,<br />
<code>matrix.length = matrix[i].length</code>,<br />
<code>1 ≤ matrix[i][j] ≤ 10<sup>5</sup></code>.</p>
</li>
<li>
<p><strong>[output] array.array.integer</strong></p>
<p>Matrix with the order of elements on its <em>longest diagonals</em> reversed.</p>
</li>
</ul>
<p><strong>[Python 3] Syntax Tips</strong></p>
<pre><code class="language-python"><span class="hljs-comment"># Prints help message to the console</span>
<span class="hljs-comment"># Returns a string</span>
<span class="hljs-keyword">def</span> <span class="hljs-title function_">helloWorld</span>(<span class="hljs-params">name</span>):
    <span class="hljs-built_in">print</span>(<span class="hljs-string">"This prints to the console when you Run Tests"</span>)
    <span class="hljs-keyword">return</span> <span class="hljs-string">"Hello, "</span> + name

</code></pre>

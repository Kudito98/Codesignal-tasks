<p>Given a rectangular matrix containing only digits, calculate the number of different <code>2 × 2</code> squares in it.</p>
<p><span class="markdown--header" style="color:#2b3b52;font-size:1.4em">Example</span></p>
<p>For</p>
<pre><code>matrix = [[1, 2, 1],
          [2, 2, 2],
          [2, 2, 2],
          [1, 2, 3],
          [2, 2, 1]]
</code></pre>
<p>the output should be<br />
<code>solution(matrix) = 6</code>.</p>
<p>Here are all <code>6</code> different <code>2 × 2</code> squares:</p>
<ul>
<li>1 2<br />
2 2</li>
<li>2 1<br />
2 2</li>
<li>2 2<br />
2 2</li>
<li>2 2<br />
1 2</li>
<li>2 2<br />
2 3</li>
<li>2 3<br />
2 1</li>
</ul>
<p><span class="markdown--header" style="color:#2b3b52;font-size:1.4em">Input/Output</span></p>
<ul>
<li>
<p><strong>[execution time limit] 4 seconds (py3)</strong></p>
</li>
<li>
<p><strong>[input] array.array.integer matrix</strong></p>
<p><em>Guaranteed constraints:</em><br />
<code>1 ≤ matrix.length ≤ 100</code>,<br />
<code>1 ≤ matrix[i].length ≤ 100</code>,<br />
<code>0 ≤ matrix[i][j] ≤ 9</code>.</p>
</li>
<li>
<p><strong>[output] integer</strong></p>
<p>The number of different <code>2 × 2</code> squares in <code>matrix</code>.</p>
</li>
</ul>
<p><strong>[Python 3] Syntax Tips</strong></p>
<pre><code class="language-python"><span class="hljs-comment"># Prints help message to the console</span>
<span class="hljs-comment"># Returns a string</span>
<span class="hljs-keyword">def</span> <span class="hljs-title function_">helloWorld</span>(<span class="hljs-params">name</span>):
    <span class="hljs-built_in">print</span>(<span class="hljs-string">"This prints to the console when you Run Tests"</span>)
    <span class="hljs-keyword">return</span> <span class="hljs-string">"Hello, "</span> + name

</code></pre>

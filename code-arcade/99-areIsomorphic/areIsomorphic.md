<p>Two two-dimensional arrays are <em>isomorphic</em> if they have the same number of rows and each pair of respective rows contains the same number of elements.</p>
<p>Given two two-dimensional arrays, check if they are isomorphic.</p>
<p><span class="markdown--header" style="color:#2b3b52;font-size:1.4em">Example</span></p>
<ul>
<li>
<p>For</p>
<pre><code>array1 = [[1, 1, 1],
          [0, 0]]
</code></pre>
<p>and</p>
<pre><code>array2 = [[2, 1, 1],
          [2, 1]]
</code></pre>
<p>the output should be<br />
<code>solution(array1, array2) = true</code>;</p>
</li>
<li>
<p>For</p>
<pre><code>array1 = [[2],
          []]
</code></pre>
<p>and</p>
<pre><code>array2 = [[2]]
</code></pre>
<p>the output should be<br />
<code>solution(array1, array2) = false</code>.</p>
</li>
</ul>
<p><span class="markdown--header" style="color:#2b3b52;font-size:1.4em">Input/Output</span></p>
<ul>
<li>
<p><strong>[execution time limit] 4 seconds (py3)</strong></p>
</li>
<li>
<p><strong>[input] array.array.integer array1</strong></p>
<p><em>Guaranteed constraints:</em><br />
<code>1 ≤ array1.length ≤ 5</code>,<br />
<code>0 ≤ array1[i].length ≤ 5</code>,<br />
<code>0 ≤ array1[i][j] ≤ 50</code>.</p>
</li>
<li>
<p><strong>[input] array.array.integer array2</strong></p>
<p><em>Guaranteed constraints:</em><br />
<code>1 ≤ array2.length ≤ 5</code>,<br />
<code>0 ≤ array2[i].length ≤ 5</code>,<br />
<code>0 ≤ array2[i][j] ≤ 50</code>.</p>
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

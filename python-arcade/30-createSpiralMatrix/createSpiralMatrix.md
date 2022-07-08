<p>A <em>spiral matrix</em> is a square matrix of size <code>n × n</code>. It contains all the integers in range from <code>1</code> to <code>n * n</code> so that number <code>1</code> is written in the bottom right corner, and all other numbers are written in increasing order spirally in the counterclockwise direction.</p>
<p>Given the size of the matrix <code>n</code>, your task is to create a <em>spiral matrix</em>.</p>
<p><span class="markdown--header" style="color:#2b3b52;font-size:1.4em">Example</span></p>
<p>For <code>n = 3</code>, the output should be</p>
<pre><code>solution(n) = [[5, 4, 3],
                         [6, 9, 2],
                         [7, 8, 1]]
</code></pre>
<p><span class="markdown--header" style="color:#2b3b52;font-size:1.4em">Input/Output</span></p>
<ul>
<li>
<p><strong>[execution time limit] 4 seconds (py3)</strong></p>
</li>
<li>
<p><strong>[input] integer n</strong></p>
<p>Matrix size, a positive integer.</p>
<p><em>Guaranteed constraints:</em><br />
<code>3 ≤ n ≤ 75</code>.</p>
</li>
<li>
<p><strong>[output] array.array.integer</strong></p>
<p>A <em>spiral matrix</em> of size <code>n</code>.</p>
</li>
</ul>
<p><strong>[Python 3] Syntax Tips</strong></p>
<pre><code class="language-python"><span class="hljs-comment"># Prints help message to the console</span>
<span class="hljs-comment"># Returns a string</span>
<span class="hljs-keyword">def</span> <span class="hljs-title function_">helloWorld</span>(<span class="hljs-params">name</span>):
    <span class="hljs-built_in">print</span>(<span class="hljs-string">"This prints to the console when you Run Tests"</span>)
    <span class="hljs-keyword">return</span> <span class="hljs-string">"Hello, "</span> + name

</code></pre>

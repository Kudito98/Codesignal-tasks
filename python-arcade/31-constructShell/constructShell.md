<p>A 2D list <code>lst</code> of size <code>2 * n - 1</code> is called a <em>shell</em> if it is filled with zeros and has the following configuration:</p>
<ul>
<li><code>lst[0]</code> contains one element;</li>
<li><code>lst[1]</code> contains two elements;</li>
<li>...</li>
<li><code>lst[n - 2]</code> contains <code>n - 1</code> elements;</li>
<li><code>lst[n - 1]</code> contains <code>n</code> elements;</li>
<li><code>lst[n]</code> contains <code>n - 1</code> elements;</li>
<li>...</li>
<li><code>lst[2 * n - 3]</code> contains two elements;</li>
<li><code>lst[2 * n - 2]</code> contains one element.</li>
</ul>
<p>Given an integer <code>n</code>, return a <em>shell</em> list.</p>
<p><span class="markdown--header" style="color:#2b3b52;font-size:1.4em">Example</span></p>
<p>For <code>n = 3</code>, the output should be</p>
<pre><code>solution(n) = [[0],
                     [0, 0],
                     [0, 0, 0],
                     [0, 0],
                     [0]]
</code></pre>
<p><span class="markdown--header" style="color:#2b3b52;font-size:1.4em">Input/Output</span></p>
<ul>
<li>
<p><strong>[execution time limit] 4 seconds (py3)</strong></p>
</li>
<li>
<p><strong>[input] integer n</strong></p>
<p>An integer defining the size of the <em>shell</em>.</p>
<p><em>Guaranteed constraints:</em><br />
<code>1 ≤ n ≤ 30</code>.</p>
</li>
<li>
<p><strong>[output] array.array.integer</strong></p>
<p>A <em>shell</em>.</p>
</li>
</ul>
<p><strong>[Python 3] Syntax Tips</strong></p>
<pre><code class="language-python"><span class="hljs-comment"># Prints help message to the console</span>
<span class="hljs-comment"># Returns a string</span>
<span class="hljs-keyword">def</span> <span class="hljs-title function_">helloWorld</span>(<span class="hljs-params">name</span>):
    <span class="hljs-built_in">print</span>(<span class="hljs-string">"This prints to the console when you Run Tests"</span>)
    <span class="hljs-keyword">return</span> <span class="hljs-string">"Hello, "</span> + name

</code></pre>

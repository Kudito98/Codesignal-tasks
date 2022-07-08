<p>Consider integer numbers from <code>0</code> to <code>n - 1</code> written down along the circle in such a way that the distance between any two neighboring numbers is equal (note that <code>0</code> and <code>n - 1</code> are neighboring, too).</p>
<p>Given <code>n</code> and <code>firstNumber</code>, find the number which is written in the radially opposite position to <code>firstNumber</code>.</p>
<p><span class="markdown--header" style="color:#2b3b52;font-size:1.4em">Example</span></p>
<p>For <code>n = 10</code> and <code>firstNumber = 2</code>, the output should be<br />
<code>solution(n, firstNumber) = 7</code>.</p>
<p><img src="https://codesignal.s3.amazonaws.com/tasks/circleOfNumbers/img/example.png?_tm=1624652347469" alt /></p>
<p><span class="markdown--header" style="color:#2b3b52;font-size:1.4em">Input/Output</span></p>
<ul>
<li>
<p><strong>[execution time limit] 4 seconds (py3)</strong></p>
</li>
<li>
<p><strong>[input] integer n</strong></p>
<p>A positive <strong>even</strong> integer.</p>
<p><em>Guaranteed constraints:</em><br />
<code>4 ≤ n ≤ 20</code>.</p>
</li>
<li>
<p><strong>[input] integer firstNumber</strong></p>
<p><em>Guaranteed constraints:</em><br />
<code>0 ≤ firstNumber ≤ n - 1</code>.</p>
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

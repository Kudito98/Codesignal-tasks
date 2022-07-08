<p>You need to sum up a bunch of fractions that have different <code>denominators</code>. In order to do this, you need to find the least common denominator of all the fractions. As a professional programmer, you know that the least common denominator is in fact their <a href="keyword://lcm" target="_blank">LCM</a>.</p>
<p>For the given list of <code>denominators</code>, find the least common denominator by finding their <em>LCM</em>.</p>
<p><span class="markdown--header" style="color:#2b3b52;font-size:1.4em">Example</span></p>
<p>For <code>denominators = [2, 3, 4, 5, 6]</code>, the output should be<br />
<code>solution(denominators) = 60</code>.</p>
<p><span class="markdown--header" style="color:#2b3b52;font-size:1.4em">Input/Output</span></p>
<ul>
<li>
<p><strong>[execution time limit] 4 seconds (py3)</strong></p>
</li>
<li>
<p><strong>[input] array.integer denominators</strong></p>
<p>The list of denominators, where each denominator is a positive integer.</p>
<p><em>Guaranteed constraints:</em><br />
<code>1 ≤ denominators.length ≤ 10</code>,<br />
<code>2 ≤ denominators[i] ≤ 50</code>.</p>
</li>
<li>
<p><strong>[output] integer</strong></p>
<p>The least common denominator.</p>
</li>
</ul>
<p><strong>[Python 3] Syntax Tips</strong></p>
<pre><code class="language-python"><span class="hljs-comment"># Prints help message to the console</span>
<span class="hljs-comment"># Returns a string</span>
<span class="hljs-keyword">def</span> <span class="hljs-title function_">helloWorld</span>(<span class="hljs-params">name</span>):
    <span class="hljs-built_in">print</span>(<span class="hljs-string">"This prints to the console when you Run Tests"</span>)
    <span class="hljs-keyword">return</span> <span class="hljs-string">"Hello, "</span> + name

</code></pre>

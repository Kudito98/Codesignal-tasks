<p>Let's define <em>digit degree</em> of some positive integer as the number of times we need to replace this number with the sum of its digits until we get to a one digit number.</p>
<p>Given an integer, find its digit degree.</p>
<p><span class="markdown--header" style="color:#2b3b52;font-size:1.4em">Example</span></p>
<ul>
<li>For <code>n = 5</code>, the output should be<br />
<code>solution(n) = 0</code>;</li>
<li>For <code>n = 100</code>, the output should be<br />
<code>solution(n) = 1</code>.<br />
<code>1 + 0 + 0 = 1</code>.</li>
<li>For <code>n = 91</code>, the output should be<br />
<code>solution(n) = 2</code>.<br />
<code>9 + 1 = 10</code> -&gt; <code>1 + 0 = 1</code>.</li>
</ul>
<p><span class="markdown--header" style="color:#2b3b52;font-size:1.4em">Input/Output</span></p>
<ul>
<li>
<p><strong>[execution time limit] 4 seconds (py3)</strong></p>
</li>
<li>
<p><strong>[input] integer n</strong></p>
<p><em>Guaranteed constraints:</em><br />
<code>5 ≤ n ≤ 10<sup>9</sup></code>.</p>
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

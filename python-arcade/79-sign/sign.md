<p>Although Python does provide a bunch of useful built-in functions, some of them are simply missing for no apparent reason. One example of such function is a <code>solution</code> function implemented in many other languages. <code>solution(x)</code> returns <code>1</code> if <code>x</code> is positive, <code>-1</code> if <code>x</code> is negative, and <code>0</code> if <code>x</code> is equal to zero.</p>
<p>You decided to build your own package of useful functions, and would like to start with the <code>solution</code> function. Given the value of <code>x</code>, return the result of applying the <code>solution</code> function to it.</p>
<p><span class="markdown--header" style="color:#2b3b52;font-size:1.4em">Example</span></p>
<p>For <code>x = -34</code>, the output should be<br />
<code>solution(x) = -1</code>.</p>
<p><code>-34</code> is a negative number, thus the output should be <code>-1</code>.</p>
<p><span class="markdown--header" style="color:#2b3b52;font-size:1.4em">Input/Output</span></p>
<ul>
<li>
<p><strong>[execution time limit] 4 seconds (py3)</strong></p>
</li>
<li>
<p><strong>[input] integer x</strong></p>
<p>The argument of the <code>sign</code> function.</p>
<p><em>Guaranteed constraints:</em><br />
<code>-50 ≤ x ≤ 50</code>.</p>
</li>
<li>
<p><strong>[output] integer</strong></p>
<p>The value of <code>sign(x)</code>.</p>
</li>
</ul>
<p><strong>[Python 3] Syntax Tips</strong></p>
<pre><code class="language-python"><span class="hljs-comment"># Prints help message to the console</span>
<span class="hljs-comment"># Returns a string</span>
<span class="hljs-keyword">def</span> <span class="hljs-title function_">helloWorld</span>(<span class="hljs-params">name</span>):
    <span class="hljs-built_in">print</span>(<span class="hljs-string">"This prints to the console when you Run Tests"</span>)
    <span class="hljs-keyword">return</span> <span class="hljs-string">"Hello, "</span> + name

</code></pre>

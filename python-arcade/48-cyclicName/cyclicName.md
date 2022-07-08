<p>You've come up with a really cool <code>name</code> for your future startup company, and already have an idea about its logo. This logo will represent a circle, with the prefix of a <a href="keyword://cyclic-string" target="_blank">cyclic string</a> formed by the company name written around it.</p>
<p>The length <code>n</code> of the prefix you need to take depends on the size of the logo. You haven't yet decided on it, so you'd like to try out various options. Given the <code>name</code> of your company, return the prefix of the corresponding <em>cyclic string</em> containing <code>n</code> characters.</p>
<p><span class="markdown--header" style="color:#2b3b52;font-size:1.4em">Example</span></p>
<p>For <code>name = "nicecoder"</code> and <code>n = 15</code>, the output should be<br />
<code>solution(name, n) = "nicecoderniceco"</code>.</p>
<p><span class="markdown--header" style="color:#2b3b52;font-size:1.4em">Input/Output</span></p>
<ul>
<li>
<p><strong>[execution time limit] 4 seconds (py3)</strong></p>
</li>
<li>
<p><strong>[input] string name</strong></p>
<p>The name of your future startup.</p>
<p><em>Guaranteed constraints:</em><br />
<code>1 ≤ name.length ≤ 20</code>.</p>
</li>
<li>
<p><strong>[input] integer n</strong></p>
<p>The length of the <em>cyclic string</em> prefix.</p>
<p><em>Guaranteed constraints:</em><br />
<code>name.length ≤ n ≤ 50</code>.</p>
</li>
<li>
<p><strong>[output] string</strong></p>
<p>Prefix of size <code>n</code> of the <em>cyclic string</em> formed by <code>name</code>.</p>
</li>
</ul>
<p><strong>[Python 3] Syntax Tips</strong></p>
<pre><code class="language-python"><span class="hljs-comment"># Prints help message to the console</span>
<span class="hljs-comment"># Returns a string</span>
<span class="hljs-keyword">def</span> <span class="hljs-title function_">helloWorld</span>(<span class="hljs-params">name</span>):
    <span class="hljs-built_in">print</span>(<span class="hljs-string">"This prints to the console when you Run Tests"</span>)
    <span class="hljs-keyword">return</span> <span class="hljs-string">"Hello, "</span> + name

</code></pre>

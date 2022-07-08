<p>You're given a <a href="keyword://substring" target="_blank">substring</a> <code>s</code> of some <a href="keyword://cyclic-string" target="_blank">cyclic string</a>. What's the length of the smallest possible string that can be concatenated to itself many times to obtain this cyclic string?</p>
<p><span class="markdown--header" style="color:#2b3b52;font-size:1.4em">Example</span></p>
<p>For <code>s = "cabca"</code>, the output should be<br />
<code>solution(s) = 3</code>.</p>
<p><code>"cabca"</code> is a substring of a cycle string <code>"abcabcabcabc..."</code> that can be obtained by concatenating <code>"abc"</code> to itself. Thus, the answer is <code>3</code>.</p>
<p><span class="markdown--header" style="color:#2b3b52;font-size:1.4em">Input/Output</span></p>
<ul>
<li>
<p><strong>[execution time limit] 4 seconds (py3)</strong></p>
</li>
<li>
<p><strong>[input] string s</strong></p>
<p><em>Guaranteed constraints:</em><br />
<code>3 ≤ s.length ≤ 15</code>.</p>
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

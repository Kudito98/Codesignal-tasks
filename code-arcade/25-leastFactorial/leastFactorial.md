<p>Given an integer <code>n</code>, find the <em>minimal</em> <code>k</code> such that</p>
<ul>
<li><code>k = m!</code> (where <code>m! = 1 * 2 * ... * m</code>) for some integer <code>m</code>;</li>
<li><code>k &gt;= n</code>.</li>
</ul>
<p>In other words, find the smallest factorial which is not less than <code>n</code>.</p>
<p><span class="markdown--header" style="color:#2b3b52;font-size:1.4em">Example</span></p>
<p>For <code>n = 17</code>, the output should be<br />
<code>solution(n) = 24</code>.</p>
<p><code>17 &lt; 24 = 4! = 1 * 2 * 3 * 4</code>, while <code>3! = 1 * 2 * 3 = 6 &lt; 17</code>).</p>
<p><span class="markdown--header" style="color:#2b3b52;font-size:1.4em">Input/Output</span></p>
<ul>
<li>
<p><strong>[execution time limit] 4 seconds (py3)</strong></p>
</li>
<li>
<p><strong>[input] integer n</strong></p>
<p>A positive integer.</p>
<p><em>Guaranteed constraints:</em><br />
<code>1 ≤ n ≤ 120</code>.</p>
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

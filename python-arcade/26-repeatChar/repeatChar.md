<p>To make debug output more understandable, you often separate sets of logs by a single line of the same character. Since you use this method very often, you'd like to write a function that would handle printing the separator.</p>
<p>Implement a function that, given a character <code>ch</code> and the number of times it should be repeated <code>n</code>, returns a string of <code>n</code> characters <code>ch</code>.</p>
<p><span class="markdown--header" style="color:#2b3b52;font-size:1.4em">Example</span></p>
<p>For <code>ch = '*'</code> and <code>n = 20</code>, the output should be<br />
<code>solution(ch, n) = "********************"</code>.</p>
<p><span class="markdown--header" style="color:#2b3b52;font-size:1.4em">Input/Output</span></p>
<ul>
<li>
<p><strong>[execution time limit] 4 seconds (py3)</strong></p>
</li>
<li>
<p><strong>[input] char ch</strong></p>
<p>The character that should be repeated.</p>
</li>
<li>
<p><strong>[input] integer n</strong></p>
<p>The number of times the given character should be repeated.</p>
<p><em>Guaranteed constraints:</em><br />
<code>1 ≤ n ≤ 100</code>.</p>
</li>
<li>
<p><strong>[output] string</strong></p>
<p>A string consisting of <code>n</code> characters <code>ch</code>.</p>
</li>
</ul>
<p><strong>[Python 3] Syntax Tips</strong></p>
<pre><code class="language-python"><span class="hljs-comment"># Prints help message to the console</span>
<span class="hljs-comment"># Returns a string</span>
<span class="hljs-keyword">def</span> <span class="hljs-title function_">helloWorld</span>(<span class="hljs-params">name</span>):
    <span class="hljs-built_in">print</span>(<span class="hljs-string">"This prints to the console when you Run Tests"</span>)
    <span class="hljs-keyword">return</span> <span class="hljs-string">"Hello, "</span> + name

</code></pre>

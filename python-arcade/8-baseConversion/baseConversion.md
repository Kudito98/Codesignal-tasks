<p>Your university professor decided to have a little fun and asked the class to implement a function that, given a number <code>n</code> and a base <code>x</code>, converts the number from base <code>x</code> to base <code>16</code>. To make things more interesting, he announced that the first student to write the solution will have to answer fewer question than the rest of the class during the final exam.</p>
<p>Laughing devilishly, you asked if it was okay to use a language of your choice, and the unsuspecting professor answered "yes". It's settled then: Python is your language of choice!</p>
<p>Now you're bound to win. Implement a function that, given an integer number <code>n</code> and a base <code>x</code>, converts <code>n</code> from base <code>x</code> to base <code>16</code>.</p>
<p><span class="markdown--header" style="color:#2b3b52;font-size:1.4em">Example</span></p>
<p>For <code>n = "1302"</code> and <code>x = 5</code>, the output should be<br />
<code>solution(n, x) = "ca"</code>.</p>
<p>Here's why:<br />
<code>1302<sub>5</sub> = 202<sub>10</sub> = ca<sub>16</sub></code>.</p>
<p><span class="markdown--header" style="color:#2b3b52;font-size:1.4em">Input/Output</span></p>
<ul>
<li>
<p><strong>[execution time limit] 4 seconds (py3)</strong></p>
</li>
<li>
<p><strong>[input] string n</strong></p>
<p>A valid non-negative integer in base <code>x</code>. The string is guaranteed to consist of digits and lowercase English letters.</p>
<p><em>Guaranteed constraints:</em><br />
<code>1 &lt; n.length ≤ 10</code>.</p>
</li>
<li>
<p><strong>[input] integer x</strong></p>
<p>The base of <code>n</code>.</p>
<p><em>Guaranteed constraints:</em><br />
<code>2 ≤ x ≤ 36</code>.</p>
</li>
<li>
<p><strong>[output] string</strong></p>
<p>The value of <code>n</code> in base <code>16</code>. The string should contain only digits and lowercase English letters <code>'a' - 'f'</code>.</p>
</li>
</ul>
<p><strong>[Python 3] Syntax Tips</strong></p>
<pre><code class="language-python"><span class="hljs-comment"># Prints help message to the console</span>
<span class="hljs-comment"># Returns a string</span>
<span class="hljs-keyword">def</span> <span class="hljs-title function_">helloWorld</span>(<span class="hljs-params">name</span>):
    <span class="hljs-built_in">print</span>(<span class="hljs-string">"This prints to the console when you Run Tests"</span>)
    <span class="hljs-keyword">return</span> <span class="hljs-string">"Hello, "</span> + name

</code></pre>

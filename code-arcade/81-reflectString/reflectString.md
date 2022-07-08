<p>Define an <em>alphabet reflection</em> as follows: <code>a</code> turns into <code>z</code>, <code>b</code> turns into <code>y</code>, <code>c</code> turns into <code>x</code>, ..., <code>n</code> turns into <code>m</code>, <code>m</code> turns into <code>n</code>, ..., <code>z</code> turns into <code>a</code>.</p>
<p>Define a <em>string reflection</em> as the result of applying the alphabet reflection to each of its characters.</p>
<p>Reflect the given string.</p>
<p><span class="markdown--header" style="color:#2b3b52;font-size:1.4em">Example</span></p>
<p>For <code>inputString = "name"</code>, the output should be<br />
<code>solution(inputString) = "mznv"</code>.</p>
<p><span class="markdown--header" style="color:#2b3b52;font-size:1.4em">Input/Output</span></p>
<ul>
<li>
<p><strong>[execution time limit] 4 seconds (py3)</strong></p>
</li>
<li>
<p><strong>[input] string inputString</strong></p>
<p>A string of lowercase characters.</p>
<p><em>Guaranteed constraints:</em><br />
<code>3 ≤ inputString.length ≤ 1000</code>.</p>
</li>
<li>
<p><strong>[output] string</strong></p>
</li>
</ul>
<p><strong>[Python 3] Syntax Tips</strong></p>
<pre><code class="language-python"><span class="hljs-comment"># Prints help message to the console</span>
<span class="hljs-comment"># Returns a string</span>
<span class="hljs-keyword">def</span> <span class="hljs-title function_">helloWorld</span>(<span class="hljs-params">name</span>):
    <span class="hljs-built_in">print</span>(<span class="hljs-string">"This prints to the console when you Run Tests"</span>)
    <span class="hljs-keyword">return</span> <span class="hljs-string">"Hello, "</span> + name

</code></pre>

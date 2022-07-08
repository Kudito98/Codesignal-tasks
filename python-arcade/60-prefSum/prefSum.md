<p>There is a great technique that allows finding sums of consecutive elements in the given array extremely fast. It is based on the usage of <a href="keyword://prefix-sums" target="_blank">prefix sums</a>. Given array <code>a</code>, your task is to calculate all its prefix sums.</p>
<p><span class="markdown--header" style="color:#2b3b52;font-size:1.4em">Example</span></p>
<p>For <code>a = [1, 2, 3]</code>, the output should be<br />
<code>solution(a) = [1, 3, 6]</code>.</p>
<p>Here's how the <em>prefix sums</em> can be calculated: <code>[1, 1 + 2, 1 + 2 + 3] = [1, 3, 6]</code>.</p>
<p><span class="markdown--header" style="color:#2b3b52;font-size:1.4em">Input/Output</span></p>
<ul>
<li>
<p><strong>[execution time limit] 4 seconds (py3)</strong></p>
</li>
<li>
<p><strong>[input] array.integer a</strong></p>
<p><em>Guaranteed constraints:</em><br />
<code>2 ≤ a.length ≤ 3 · 10<sup>4</sup></code>,<br />
<code>-1000 ≤ a[i] ≤ 1000</code>.</p>
</li>
<li>
<p><strong>[output] array.integer</strong></p>
</li>
</ul>
<p><strong>[Python 3] Syntax Tips</strong></p>
<pre><code class="language-python"><span class="hljs-comment"># Prints help message to the console</span>
<span class="hljs-comment"># Returns a string</span>
<span class="hljs-keyword">def</span> <span class="hljs-title function_">helloWorld</span>(<span class="hljs-params">name</span>):
    <span class="hljs-built_in">print</span>(<span class="hljs-string">"This prints to the console when you Run Tests"</span>)
    <span class="hljs-keyword">return</span> <span class="hljs-string">"Hello, "</span> + name

</code></pre>

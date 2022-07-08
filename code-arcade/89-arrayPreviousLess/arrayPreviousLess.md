<p>Given array of integers, for each position <code>i</code>, search among the previous positions for the last (from the left) position that contains a smaller value. Store this value at position <code>i</code> in the answer. If no such value can be found, store <code>-1</code> instead.</p>
<p><strong>Example</strong></p>
<p>For <code>items = [3, 5, 2, 4, 5]</code>, the output should be<br />
<code>solution(items) = [-1, 3, -1, 2, 4]</code>.</p>
<p><span class="markdown--header" style="color:#2b3b52;font-size:1.4em">Input/Output</span></p>
<ul>
<li>
<p><strong>[execution time limit] 4 seconds (py3)</strong></p>
</li>
<li>
<p><strong>[input] array.integer items</strong></p>
<p>Non-empty array of positive integers.</p>
<p><em>Guaranteed constraints:</em><br />
<code>3 ≤ items.length ≤ 15</code>,<br />
<code>1 ≤ items[i] ≤ 200</code>.</p>
</li>
<li>
<p><strong>[output] array.integer</strong></p>
<p>Array containing answer values computed as described above.</p>
</li>
</ul>
<p><strong>[Python 3] Syntax Tips</strong></p>
<pre><code class="language-python"><span class="hljs-comment"># Prints help message to the console</span>
<span class="hljs-comment"># Returns a string</span>
<span class="hljs-keyword">def</span> <span class="hljs-title function_">helloWorld</span>(<span class="hljs-params">name</span>):
    <span class="hljs-built_in">print</span>(<span class="hljs-string">"This prints to the console when you Run Tests"</span>)
    <span class="hljs-keyword">return</span> <span class="hljs-string">"Hello, "</span> + name

</code></pre>

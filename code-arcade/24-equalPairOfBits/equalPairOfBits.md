<p>You're given two integers, <code>n</code> and <code>m</code>. Find position of the rightmost pair of equal bits in their binary representations (it is guaranteed that such a pair exists), counting from right to left.</p>
<p>Return the value of <code>2<sup>position_of_the_found_pair</sup></code> (0-based).</p>
<p><strong>Example</strong></p>
<p>For <code>n = 10</code> and <code>m = 11</code>, the output should be<br />
<code>solution(n, m) = 2</code>.</p>
<p><code>10<sub>10</sub> = 10<b><font color="red">1</font></b>0<sub>2</sub></code>, <code>11<sub>10</sub> = 10<b><font color="red">1</font></b>1<sub>2</sub></code>, the position of the rightmost pair of equal bits is the bit at position <code>1</code> (0-based) from the right in the binary representations.<br />
So the answer is <code>2<sup>1</sup> = 2</code>.</p>
<p><span class="markdown--header" style="color:#2b3b52;font-size:1.4em">Input/Output</span></p>
<ul>
<li>
<p><strong>[execution time limit] 4 seconds (py3)</strong></p>
</li>
<li>
<p><strong>[input] integer n</strong></p>
<p><em>Guaranteed constraints:</em><br />
<code>0 ≤ n ≤ 2<sup>30</sup></code>.</p>
</li>
<li>
<p><strong>[input] integer m</strong></p>
<p><em>Guaranteed constraints:</em><br />
<code>0 ≤ m ≤ 2<sup>30</sup></code>.</p>
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

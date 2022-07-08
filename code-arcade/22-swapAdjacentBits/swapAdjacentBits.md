<p>You're given an arbitrary 32-bit integer <code>n</code>. Take its binary representation, split bits into it in pairs (bit number <code>0</code> and <code>1</code>, bit number <code>2</code> and <code>3</code>, etc.) and swap bits in each pair. Then return the result as a decimal number.</p>
<p><span class="markdown--header" style="color:#2b3b52;font-size:1.4em">Example</span></p>
<ul>
<li>
<p>For <code>n = 13</code>, the output should be<br />
<code>solution(n) = 14</code>.</p>
<p><code>13<sub>10</sub> = 1101<sub>2</sub> ~&gt; {11}{01}<sub>2</sub> ~&gt; 1110<sub>2</sub> = 14<sub>10</sub></code>.</p>
</li>
<li>
<p>For <code>n = 74</code>, the output should be<br />
<code>solution(n) = 133</code>.</p>
<p><code>74<sub>10</sub> = 01001010<sub>2</sub> ~&gt; {01}{00}{10}{10}<sub>2</sub> ~&gt; 10000101<sub>2</sub> = 133<sub>10</sub></code>.<br />
Note the preceding zero written in front of the initial number: since both numbers are 32-bit integers, they have <code>32</code> bits in their binary representation. The preceding zeros in other cases don't matter, so they are omitted. Here, however, it does make a difference.</p>
</li>
</ul>
<p><span class="markdown--header" style="color:#2b3b52;font-size:1.4em">Input/Output</span></p>
<ul>
<li>
<p><strong>[execution time limit] 4 seconds (py3)</strong></p>
</li>
<li>
<p><strong>[input] integer n</strong></p>
<p><em>Guaranteed constraints:</em><br />
<code>0 ≤ n &lt; 2<sup>30</sup></code>.</p>
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
